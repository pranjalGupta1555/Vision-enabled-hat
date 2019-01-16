from gtts import gTTS
tts = gTTS(text="obstacle", lang='en', slow=False)
tts.save('obstacle.mp3')
