from gtts import gTTS
import os

text = "you gay motherfucker "
language = "en"

myobj = gTTS(text=text, lang=language, slow=False)
myobj.save("welcome.mp3")
os.system("afplay welcome.mp3")
