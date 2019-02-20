if [ $# -eq 0 ] 
then
    echo "No arguments supplied"
    echo "Please provide relative path to .flac or .wav file you wish to analyze"
else
    echo "File to analyze: $1"

    python3 fileConvert.py $1
    code=$?
    filename=$1
    echo $filename
    if [ $code -eq 1 ]
    then
        echo "Invalid file extension"
        echo "Please provide relative path to .wav or .flac file you wish to analyze"
        exit 1
    elif [ $code -eq 2 ]
    then 
        filename="$(echo $filename | cut -d'.' -f 1).flac"
        echo "New File to analyze: $filename"
    fi

    # Runs through googleAPI
    API_OUT="$(python3 googleAPICall.py --input_file "$filename")"

    # Process google output
    PROCESSOR_OUT="$(python processor.py "$API_OUT")"

    echo "Text Found: " $PROCESSOR_OUT

    # Speak the processed output
    ./textToSpeech.sh "$PROCESSOR_OUT"
fi