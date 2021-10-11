######Cloned with changes from other github profile###########
############Updated By: Puneet Bawa##############################

from os import walk
import os
import matplotlib.pyplot as plt
import sys
try:
        link = sys.argv[1]
except IndexError:
        scriptName = sys.argv[0]
        print "Usage: python " + scriptName + " linkOfVideo"
        exit()
#Change this path with yours.
#Also make sure that youtube-dl and ffmpeg installed.
#Previous versions of youtube-dl can be slow for downloading audio. Make sure you have downloaded the latest version from webpage.
#https://github.com/rg3/youtube-dl
mypath = "/home/puneet/research/audios_conv_youtube"
os.chdir(mypath)
os.system("youtube-dl --extract-audio " + link)

vidID= link.split("=")[1]
print "VidID = " + vidID
f = []
for (dirpath, dirnames, filenames) in walk(mypath):
    f.extend(filenames)
    break
for i in range(0, len(f)):
        if ".opus" in f[i] and vidID in f[i]:
                vidName = f[i]
                print vidName
                cmdstr = "ffmpeg -i \"" + vidName + "\" -f wav -ar 16000 -flags bitexact \"" + vidName[:-5] + ".wav"  + "\""
                print cmdstr
                os.system(cmdstr)
                os.remove(vidName) #Will remove original opus file. Comment it if you want to keep that file.
