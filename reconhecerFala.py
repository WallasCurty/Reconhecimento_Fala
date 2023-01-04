import speech_recognition as sr

rec = sr.Recognizer()

#Listar os microfones 
#print(sr.Microphone().list_microphone_names())
with sr.Microphone() as mic:
    rec.adjust_for_ambient_noise(mic)
    print("Pode falar que eu vou gravar !!")
    audio = rec.listen(mic)
    texto = rec.recognize_google(audio,language="pt-BR")
