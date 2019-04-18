while [ true ]
do 
    # for google auth
    export GOOGLE_APPLICATION_CREDENTIALS=/home/pi/RepeaterRepeater/Speech_Transcription/raspberry-pi-key.json

    # get current mode
    MODE=$(cat currentMode.txt)

    # Record on Raspberry Pi
    MODE=$(python3 record.py $MODE)

    # Start Yellow for processing
    python3 color.py WHITE &

    # Get PID of color.py process
    to_kill=$!

    if [ "$MODE" == "timeout" ] ; then
        ./textToSpeech.sh "Recording timed out. Please push the record button to end your recording."
    else
        if [[ $? -ne 0 ]] ; then
            kill 0
            exit 1
        fi

        # Runs through googleAPI
        ./googleAPICallV2.sh "test1.wav"

        # Process google output
        PROCESSOR_OUT="$(python3 processorv2.py "googleOutput.json" "$MODE")"

        echo "Text Found: " $PROCESSOR_OUT

        # Speak the processed output
        ./textToSpeech.sh "$PROCESSOR_OUT"
    fi

    kill $to_kill
done
