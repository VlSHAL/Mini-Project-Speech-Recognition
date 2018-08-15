import speech_recognition as sr

#creating a Recognizer class object
recognizer = sr.Recognizer()
#loading an audiofile into an object of the AudioFile class
audiofile = sr.AudioFile('welcome_to_rubiks_code_dot_net.wav')

with audiofile as source:
    #remove any unnecessary noise from the background
    recognizer.adjust_for_ambient_noise(source)
    #record each chunk into an object of AudioData class
    audio = recognizer.record(source)
#executing the method 
print(recognizer.recognize_google(audio))
