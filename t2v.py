from gtts import gtts
text = input("enter txt")
lang = "en"
speech = gTTS(text=text, lang=lang, slow=False)
speech.save("voice.mp3")
