from gtts import gTTS

text = input("Enter Your Text\n>>>\t")
language = 'en'
tts = gTTS(text=text, lang=language, slow=False)

tts.save("speech.mp3")
