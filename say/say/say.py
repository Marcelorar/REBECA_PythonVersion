#
#R.E.B.E.C.A. Alpha 1.0
#
import speech_recognition  
import speech
import time

#from gittalk import core as c

#c.say(text='hola',rate_adjust=50,volume_adjust=10)
#instancia de listeners  
r = speech_recognition.Recognizer()
#escuchar
with speech_recognition.Microphone() as dato: 
        print("Te escucho") 
        audio = r.listen(dato)
        print('procesando tu voz, solo me tomara unos segundos...')
#hablado a texto
try:
    print("Dijiste " + r.recognize_google(audio))    
    speech.say("Dijiste " + r.recognize_google(audio))
except LookupError:                            
    print("Perdon, no te entendí")
    speech.say("Perdón, ni te entendí")

  






 
