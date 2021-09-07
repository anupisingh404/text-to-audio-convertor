from gtts import gTTS

from playsound import playsound

audio = "speech.mp3"
language = 'en'
sp = gTTS(text = "guruji aalsi hain kanjoos hain guruji anupi ko ice cream aur chocolate dena hai khareed ke",
       lang = language,slow = False)
sp.save(audio)
playsound(audio)
