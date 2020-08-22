#YOUTUBE VIDEO TO WAV CONVERTER

#youtube2wav.py
The script allows the download for the videos uploaded on YouTube and using ffmpeg the clean wav files are generated.

Check requirements.txt 

	1) install youtube-dl
	2) install ffmpeg

The script using ffmpeg also allows the conversion into the required sampling frequency (Note: -ar 16000 to be put after the input file)

Usage: python youtube2wav.py link
Example: python youtube2wav.py https://www.youtube.com/watch?v=ZgIzch1Pqj4
