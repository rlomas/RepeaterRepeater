export GOOGLE_APPLICATION_CREDENTIALS=$PWD/"raspberry-pi-key.json"

# if [ $# -eq 0 ]
# then
#    echo "No arguments supplied"
#    echo "Please provide relative path to .flac or .wav file you wish to analyze"
# else
    # echo "File to analyze: $1"
    python3 ../record.py
    python3 fileConvert.py "test1.wav"
    filename="test1.flac"
    # code=$?
    # filename=$1
    # echo $filename
    # if [ $code -eq 1 ]
    # then
    #    echo "Invalid file extension"
    #    echo "Please provide relative path to .wav or .flac file you wish to analyze"
    #    exit 1
    #elif [ $code -eq 2 ]
    #then
    #    filename="$(echo $filename | cut -d'.' -f 1).flac"
    #    echo "New File to analyze: $filename"
    #fi

    # Runs through googleAPI
    API_OUT="$(python3 googleAPICall.py --input_file "$filename")"

    echo $API_OUT
#    if [ "$API_OUT" == "authentication needed" ]:
#    then
#        echo $API_OUT
#        exit 1
#    fi
#    then
#        echo "Authentication needed"
#
#        gcloud config set project repeaterrepeater-1550350494511
#        gcloud projects add-iam-policy-binding repeaterrepeater-1550350494511 --member "serviceAccount:amyjbaer@repeaterrepeater-1550350494511.iam.gserviceaccount.com" --role "roles/owner"
#        gcloud iam service-accounts keys create RepeaterRepeater-90d8f74733ea.json --iam-account amyjbaer@repeaterrepeater-1550350494511.iam.gserviceaccount.com
#
#        echo "Run this command:"
#        echo 'export GOOGLE_APPLICATION_CREDENTIALS=$PWD/"RepeaterRepeater-90d8f74733ea.json"'
#        echo "And run again"
#        exit 1
#    fi

    # Process google output
    PROCESSOR_OUT="$(python processor.py "$API_OUT")"

    echo "Text Found: " $PROCESSOR_OUT

    # Speak the processed output
    ./textToSpeech.sh "$PROCESSOR_OUT"
# fi
