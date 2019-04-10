while [ true ]
do 
    # for google auth
    export GOOGLE_APPLICATION_CREDENTIALS=$PWD/"raspberry-pi-key.json"

    # get current mode
    MODE=$(cat currentMode.txt)

    # Record on Raspberry Pi
    MODE=$(python3 record.py $MODE)

    if [[ $? -ne 0 ]] ; then
        kill 0
        exit 1
    fi

    # Start Yellow for processing
    python3 color.py WHITE &

    # Get PID of color.py process
    to_kill=$!

    # Runs through googleAPI
    ./googleAPICallV2.sh "test1.wav"

    # Process google output
    PROCESSOR_OUT="$(python3 processorv2.py "googleOutput.json")"

    echo "Text Found: " $PROCESSOR_OUT

    COMMAND="$MODE$PROCESSOR_OUT"

    # Speak the processed output
    ./textToSpeech.sh "$COMMAND"

    kill $to_kill
done
