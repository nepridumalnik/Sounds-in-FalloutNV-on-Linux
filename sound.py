import os
from pydub import AudioSegment

for root, dirs, files in os.walk("~/"): 
    for file in files:
        if file.endswith(".mp3"):
             text = os.path.join(root, file)
             sound = AudioSegment.from_mp3(text)
             sound.export(text[:-4]+'.wav', format="wav")
             print(text[:-4]+'.wav'+' converted')
             text = text[:-4]+'.wav'
             sound = AudioSegment.from_mp3(text)
             sound.export(text[:-4]+'.mp3', format="mp3")
             print(text[:-4]+'.wav'+' deleted')
             os.remove(text)
