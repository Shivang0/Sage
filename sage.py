import urllib
import urllib.request
from bs4 import BeautifulSoup
import requests
from bs4 import BeautifulSoup
from urlextract import URLExtract
import threading
import cred
import exclude
import argparse
import sys
from colorama import init
from termcolor import colored
import random



parser = argparse.ArgumentParser(description="Find S3 Buckets from an Organization's Github")
parser.add_argument('-org', help='Enter the name of the organization.', required=True)
parser.add_argument('-q', help='Query to Search for Buckets. Default: s3.amazonaws.com', default='s3.amazonaws.com')
parser.add_argument('-o', help='Output to a file.')
parser.add_argument('-p', type=int, help='Number of Pages to scrape for S3 Buckets.', default=100)

args = parser.parse_args()

init()

headers = {
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
}

exclude = ['http://s3.amazonaws.com/doc/2006-03-01/', 'https://github-cloud.s3.amazonaws.com', 'https://codon-buildpacks.s3.amazonaws.com/']

login_data = cred.credentials

def banner():
    print('''
    _____ ___   ____________
  / ___//   | / ____/ ____/
  \__ \/ /| |/ / __/ __/   
 ___/ / ___ / /_/ / /___   
/____/_/  |_\____/_____/
                        v1.0
    Scrape S3 Buckets from GitHub
    Developed by @notmarshmllow
    ''')

banner()

with requests.Session() as s:
    url = 'https://github.com/session'
    r = s.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'html5lib')
    login_data['timestamp_secret'] = soup.find('input', attrs={'name':'timestamp_secret'})['value']
    login_data['timestamp'] = soup.find('input', attrs={'name':'timestamp'})['value']
    login_data['authenticity_token'] = soup.find('input', attrs={'name':'authenticity_token'})['value']

    r = s.post(url, data=login_data, headers=headers)


organization = args.org
organization = organization.lower()
query = args.q
pages = args.p
pages=int(pages)

random_text = ['get yourself some coffee.', 'take a nap.', 'have some tea.', 'get some food.', 'play a game.', 'take a break.', 'read a blog.', 'star me on GitHub ;)']


z = random.choice(random_text)
print(f'\nFetching all repositories of {organization}. By the time, you might {z}')

def main():
    x = 1
    while x <= pages:
        url_org = f'https://github.com/search?p={x}&q=org%3A{organization}+{query}&type=code'



        page = s.get(url_org).text
        soup = BeautifulSoup(page, 'html5lib')

        url_list = []

        for link in soup.findAll('a'):
            inside_file = link.get('href')
            if f'/{organization}/' in inside_file:
                full_url = 'https://github.com' + inside_file
                head = full_url.partition('#')
                url_list.append(head[0])
                
        final_url_list = set(url_list)
        final_url_list = list(final_url_list)


        total_repositories = len(final_url_list)

        print(f'\nFetched {total_repositories} repositories from page {x} that contain S3 Buckets .')
        print("\n")
        if total_repositories == 0 and x < 2:
            print(colored("Make sure your credentials are properly configured.", 'red'))
            sys.exit(1)
        if total_repositories ==0:
            print('Cannot find more S3 Buckets.')
            sys.exit(1)


        for i in (final_url_list):
            inner_url = i
            inner_url_fetch = s.get(inner_url).text
            extractor = URLExtract()
            for bucketurl in extractor.gen_urls(inner_url_fetch):
                if bucketurl not in exclude and 's3.amazonaws.com' in bucketurl:
                    try:
                        check_takeover = requests.get(bucketurl)
                        status = check_takeover.status_code
                        o1 = (f'[{status}] - {bucketurl}\n')
                        if args.o:
                            file = open(args.o, 'a')
                            file.write(o1)
                        print(f'[{status}] - {bucketurl} ')
                    except:
                        pass
                    try:
                        check_takeover_response = check_takeover.content
                        check_takeover_response = str(check_takeover_response)
                        if 'NoSuchBucket' in check_takeover_response:
                            s3_text = (colored('[S3 Bucket Takeover]', 'green'))
                            o2 = (f'{s3_text} : {bucketurl}\n')
                            print(f'{s3_text} : {bucketurl}')
                            if args.o:
                                file=open(args.o, 'a')
                                file.write(o2)

                    except:
                        pass

                    
        x=x+1


t = threading.Thread(target=main)
t.start()
