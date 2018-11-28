import os
from pydub import AudioSegment

for root, dirs, files in os.walk("/home/muser/.local/share/Steam/steamapps/common/Fallout New Vegas enplczru/"):
    for file in files:
        if file.endswith(".mp3"):
             text = os.path.join(root, file)
             print(text[:-4]+'.wav')
             sound = AudioSegment.from_mp3(text)
             sound.export(text[:-4]+'.wav', format="wav")
             os.remove(text)
             
for root, dirs, files in os.walk("/home/muser/.local/share/Steam/steamapps/common/Fallout New Vegas enplczru/"):
    for file in files:
        if file.endswith(".wav"):
             text = os.path.join(root, file)
             print(text[:-4]+'.mp3')
             sound = AudioSegment.from_mp3(text)
             sound.export(text[:-4]+'.mp3', format="mp3")
             os.remove(text)
