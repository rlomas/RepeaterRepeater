from google.cloud import storage

# Explicitly use service account credentials by specifying the private key
# file.
storage_client = storage.Client.from_service_account_json('raspberry-pi-key.json')