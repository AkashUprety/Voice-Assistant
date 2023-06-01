# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 10:18:31 2023

@author: ASUS
"""
import googletrans
import speech_recognition
import gtts
import playsound

#print(googletrans.LANGUAGES)

input_lng="hi"
output_lng="en"

recognizer = speech_recognition.Recognizer()
with speech_recognition.Microphone() as source:
    print("Speak Now")
    voice = recognizer.listen(source)
    text = recognizer.recognize_google(voice,language=input_lng)
    print(text)

translator = googletrans.Translator()
translation = translator.translate(text,dest=output_lng)
print(translation.text)
converted_audio = gtts.gTTS(translation.text, lang=output_lng)
converted_audio.save("hello.mp3")
playsound.playsound("hello.mp3")