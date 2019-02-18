TEXT="$1"
gtts-cli "$TEXT" --output out.mp3
mpg123 -q out.mp3
rm out.mp3