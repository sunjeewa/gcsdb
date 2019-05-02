from google.cloud import storage
import google.api_core.exceptions
import logging


PROJECT="cr-dev"
BUCKET="{}-db".format(PROJECT)

client = storage.Client(project=PROJECT)


class GCSDB():
    bucket = None

    def __init__(self, table):

        if self.bucket_exists():
            try:
                blob = self.bucket.get_blob(table)
                return(blob.download_as_string())
            except google.api_core.exceptions.NotFound as e:
                logging.error(e)
        else:
            logging.error("bucket not available")

   
    def bucket_exists(self):
        try:
            self.bucket = client.get_bucket(BUCKET)
            return self.bucket
        except google.api_core.exceptions.NotFound as e:
            # Create bucket 
            client.create_bucket(BUCKET)
            self.bucket = client.get_bucket(BUCKET)
            return self.bucket
        



db = GCSDB("users.csv")

"""
from google.cloud import storage
client = storage.Client()
# https://console.cloud.google.com/storage/browser/[bucket-id]/
bucket = client.get_bucket('bucket-id-here')
# Then do other things...
blob = bucket.get_blob('remote/path/to/file.txt')
print(blob.download_as_string())
blob.upload_from_string('New contents!')
blob2 = bucket.blob('remote/path/storage.txt')
blob2.upload_from_filename(filename='/local/path.txt')
"""
