# Sage
Sage - Fast Scraping Tool to quicly find all S3 Buckets from organization's GitHub Repositories and find S3 Bucket Takeover.

![alt_text](https://github.com/notmarshmllow/Sage/blob/main/image.png)

# INSTALLATION

Requirement: Python: 3.7+

1. `git clone https://github.com/notmarshmllow/sage.git`
2. `cd Sage\`
3. `pip install -r requirements.txt`
4. `python3 sage.py -h`

# USAGE
Sage takes the name of the organization and tries to find all S3 Buckets in the Orgnization's GitHub Repositories.

Following usage example show simplest tasks you can acomplish with `Sage`.

# CREDENTIALS

Please update you GitHub Login credentials in `cred.py` file.
Make sure you do not have two-factor authentication (2FA) turned ON. This may cause issues for tool to run.

Credentials are required to use the tool or else the tool will not run.

# ORGANIZATION'S NAME

The `-org` switch takes the Organization's name and finds all the S3 Buckets associated with the Organization in the Organization's Repository.

`python3 sage.py -org Google`

# NUMBER OF PAGES TO SCRAPE

The `-p` switch takes integer as input. It accepts the number of pages to scrape (default: 100)

`python3 sage.py -org Google -p 8`


# OUTPUT TO A FILE

The `-o` switch prints output to a file.

`python3 sage.py -org Google -p 8 -o facebook_s3.txt`

# S3 Bucket Takoover

Sage finds all the S3 Buckets of an organization and also finds out any unclaimed Buckets.

If a bucket is vulnerable, Sage display that the Takeover of the Bucket is possible.


#  EXCLUDE

If you find any repetative or irreleant bucket that isn't associated with your target but still is being scrapped, you can include it in the exclude list in `sage.py` file. This will make sure that the bucket name isn't shown in the Output anymore.




All developments to Sage are highly welcomed and much appreciated!

Sage- Developed by [@notmarshmllow](https://twitter.com/notmarshmllow):heart:
