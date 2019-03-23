import argparse
from google.cloud import storage


parser = argparse.ArgumentParser()
parser.add_argument('--bucket_name', type=str, help='Bucket to be deleted from')
parser.add_argument('--blob_name', type=str, help='blob name')

def main():
	args = parser.parse_args()
	bucket_name = args.bucket_name
	blob_name = args.blob_name
	delete_blob(bucket_name,blob_name)




def delete_blob(bucket_name, blob_name):
    """Deletes a blob from the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(blob_name)

    blob.delete()

    print('Blob {} deleted.'.format(blob_name))





if __name__ == '__main__':
    
    main()