export GOOGLE_APPLICATION_CREDENTIALS=$PWD/"key.json"

if [ $# -eq 0 ]
then
    echo "No arguments supplied"
    echo "Please provide relative path to .flac or .wav file you wish to analyze"
else
    echo "File to analyze: $1"

    # Runs through googleAPI
    ./googleAPICallV2.sh "$1"

    # Process google output
    PROCESSOR_OUT="$(python3 processorv2.py "googleOutput.json")"

    echo "Text Found: " $PROCESSOR_OUT

    # Speak the processed output
    ./textToSpeech.sh "$PROCESSOR_OUT"
fi
