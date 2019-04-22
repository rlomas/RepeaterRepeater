
import argparse
from google.cloud import storage


parser = argparse.ArgumentParser()
parser.add_argument('--bucket_name', type=str, help='Bucket to be uploaded to')
parser.add_argument('--src_file', type=str, help='src_file name')
parser.add_argument('--dst_file', type=str, help='dst_file name')



def main():
	args = parser.parse_args()
	bucket_name = args.bucket_name
	src_file = args.src_file
	dst_file = args.dst_file
	upload_blob(bucket_name,src_file,dst_file)


# [START storage_upload_file]
def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print('File {} uploaded to {}.'.format(
        source_file_name,
        destination_blob_name))
# [END storage_upload_file]



if __name__ == '__main__':
    
    main()
