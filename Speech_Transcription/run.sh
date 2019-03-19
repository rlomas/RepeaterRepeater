# for google auth : WILL ONLY WORK ON RASPBERRY PI
export GOOGLE_APPLICATION_CREDENTIALS=$PWD/"raspberry-pi-key.json"

# Record on Raspberry Pi
python3 ../record.py

# Convert file to flace
python3 fileConvert.py "test1.wav"

# Runs through googleAPI
API_OUT="$(python3 googleAPICall.py --input_file "test1.flac")"

echo $API_OUT

# Process google output
PROCESSOR_OUT="$(python processor.py "$API_OUT")"

echo "Text Found: " $PROCESSOR_OUT

# Speak the processed output
./textToSpeech.sh "$PROCESSOR_OUT"