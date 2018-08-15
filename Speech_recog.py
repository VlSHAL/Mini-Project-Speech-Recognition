import speech_recognition as sr


recognizer = se.Recognizer()
audiofile = sr.AudioFile('')

with audiofile as source:
    recognizer.adjust_for_ambient_noise(source)
    audio = recognizer.record(source)

recognizer.recognize_google(audio)
