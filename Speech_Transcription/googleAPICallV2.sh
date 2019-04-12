#export GOOGLE_APPLICATION_CREDENTIALS=$PWD/"key.json"

if [ $# -eq 0 ]
then
    echo "No arguments supplied"
    echo "Please provide relative path to .flac or .wav file you wish to analyze"
else

    code=$?
    filename=$1

    BASENAME=${filename##*/}
    echo $BASENAME

    #upload filename to google storage
    python uploadFile.py --bucket_name test-repeater-repeater --src_file $1 --dst_file brad_demo/$BASENAME

    #make file public (may not need this)
    # gsutil acl ch -u AllUsers:R gs://test-repeater-repeater/brad_demo/$BASENAME

    #edit json file to include name of file (use jq)
    python3 changeJSON.py --audio_file gs://test-repeater-repeater/brad_demo/$BASENAME

    #run curl command and send to proccessor (need to change -d)
    curl -s -H "Content-Type: application/json"     https://speech.googleapis.com/v1p1beta1/speech:recognize?key=raspberry-pi-key.json      -d @brad_request_final.json > googleOutput.json

    #delete file from google storage
    python deleteFile.py --bucket_name test-repeater-repeater --blob_name brad_demo/$BASENAME

fi
