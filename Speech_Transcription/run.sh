while [ true ]
do 
    # for google auth
    export GOOGLE_APPLICATION_CREDENTIALS=$PWD/"raspberry-pi-key.json"

    # Record on Raspberry Pi
    python3 record.py

    if [[ $? -ne 0 ]] ; then
        kill 0
        exit 1
    fi

    # Start Yellow for processing
    python3 color.py CYAN &

    # Get PID of color.py process
    to_kill=$!

    # Runs through googleAPI
    ./googleAPICallV2.sh "test.wav"

    # Process google output
    PROCESSOR_OUT="$(python3 processorv2.py "googleOutput.json")"

    echo "Text Found: " $PROCESSOR_OUT

    # Speak the processed output
    ./textToSpeech.sh "$PROCESSOR_OUT"

    kill $to_kill
done
