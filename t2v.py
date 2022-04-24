from gtts import gtts
import os
text = input("enter txt")
lang = "en"
speech = gTTS(text=text, lang=lang, slow=False)
speech.save("voice.mp3")
os.system("mpg321 voice.mp3")