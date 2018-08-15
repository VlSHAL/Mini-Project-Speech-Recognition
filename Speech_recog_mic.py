import speech_recognition as sr

#creating a Recognizer class object
recognizer = sr.Recognizer()
#to get the list of all available microphones
sr.Microphone.list_microphone_names()
#create an object of Microphone class and assign the req microphone index from the above list
mic = sr.Microphone(device_index=1)

with mic as source:
    #clean any unnecessary noise
    recognizer.adjust_for_ambient_noise(source)
    #using listen method , to capture data until pause in speaking is detected
    audio = recognizer.listen(source)

print(recognizer.recognize_google(audio, language='en-US'))
