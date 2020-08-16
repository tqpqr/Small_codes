from gtts import gTTS

phrases = ["Voila! Your text is readed by voice!", "And separate sentances in this list are saved as separate files!"]
for i in phrases:
    tts = gTTS(text=i, lang='en')
    tts.save("C:/TTS_Sentances/"+i+".mp3")
