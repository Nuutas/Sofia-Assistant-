#_______________________________________________________________________________________________________________

#                                       Importar Bibliotecas Essenciais


import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pywhatkit
import pyrebase
import time

#_______________________________________________________________________________________________________________




#_______________________________________________________________________________________________________________

#                                   Configuração de acesso à Base de dados 

firebaseConfig = {

  "apiKey": "AIzaSyDNaTvko4yDXDkYa9HlgcAEZ6Didfb_MKg",
  "authDomain": "sofia-f9db2.firebaseapp.com",
  "databaseURL": "https://sofia-f9db2-default-rtdb.firebaseio.com",
  "projectId": "sofia-f9db2",
  "storageBucket": "sofia-f9db2.appspot.com",
  "messagingSenderId": "350447787600",
  "appId": "1:350447787600:web:b612b74f4e449d7af0fb55",
  "measurementId": "G-0X86N1YWRQ"

}

#_______________________________________________________________________________________________________________




#_______________________________________________________________________________________________________________

#                                    Inicialização da Base de dados e do Audio 

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()    

audio = sr.Recognizer()
pc = pyttsx3.init()

#_______________________________________________________________________________________________________________





#_______________________________________________________________________________________________________________


#                                          Defenição da Função "talk"

def talk(text):
    pt_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_ptPT_Helia"

    rate = pc.getProperty('rate')
    volume = pc.getProperty('volume')
    voice = pc.getProperty('voice')

    pc.setProperty('voice', pt_voice_id)
    pc.setProperty('rate', 135)

    pc.say(text)
    pc.runAndWait()
    pc.setProperty(audio, "portugal") 

#_______________________________________________________________________________________________________________




#_______________________________________________________________________________________________________________

#                                         Defenição da Função "take_command"

def take_command():
    r = sr.Recognizer()

    while True:
        with sr.Microphone() as source:
            print('A ouvir :')
            audio = r.listen(source)

        try:
            comando = r.recognize_google(audio, language='pt-pt')
            comando = comando.lower()
            print(comando)

            if 'sofia' in comando:
                comando = comando.replace('sofia', '')
                return comando

        except sr.UnknownValueError:
            print("Não foi possível reconhecer a fala")
        except sr.RequestError as e:
            print(f"Não foi possível conectar ao serviço de reconhecimento de fala; {e}")

        time.sleep(0.5) # aguarda um segundo antes de tentar novamente


#_______________________________________________________________________________________________________________




#_______________________________________________________________________________________________________________

#                                        Defenição da Função "run_sofia"


def run_sofia():

   
    comando = take_command()

    if comando != None:
    #------------------------------------------Apresentação--------------------------------------------

        if 'apresenta-te' in comando:
            talk('Sou uma assistennte de voz, no prujéto, de aptedídão profissional, chamado Sofia!')
            pc.runAndWait()
        
        if 'quem és' in comando:
            talk('Sou uma assistennte de voz, no prujéto, de aptedídão profissional, chamado Sofia!')
            pc.runAndWait()
            

        #--------------------------------------------Abstract-------------------------------------------------

            
        #--------------Pessoal----------------
            
        if 'onde moras' in comando:
            talk('Não tenho um local de residência, já que sou um programa de computador.')
            pc.runAndWait()

        elif 'onde vives' in comando:
            talk('Não tenho um local de residência, já que sou um programa de computador.')
            pc.runAndWait()

        if 'como estás' in comando:
            talk('Estou bem, obrigada por perguntar!')
            pc.runAndWait()

        if 'como te sentes' in comando:
            talk('Estou bem, obrigada por perguntar!')
            pc.runAndWait()
            
        #---------------Horas------------------
        
        if 'que horas são' in comando:
            now = datetime.datetime.now()
            hora = now.strftime("%H:%M")
            talk(f"São {hora}")
            pc.runAndWait()

        if 'diz-me as horas' in comando:
            now = datetime.datetime.now()
            hora = now.strftime("%H:%M")
            talk(f"São {hora}")
            pc.runAndWait()

        if 'são que horas' in comando:
            now = datetime.datetime.now()
            hora = now.strftime("%H:%M")
            talk(f"São {hora}")
            pc.runAndWait()

        if 'diz as horas' in comando:
            now = datetime.datetime.now()
            hora = now.strftime("%H:%M")
            talk(f"São {hora}")
            pc.runAndWait()

        #----------------Data------------------    

        if 'que dia é hoje' in comando:
            now = datetime.datetime.now()
            data = now.strftime("%d/%m/%Y")
            talk("Hoje é" + data)
            pc.runAndWait()

        if 'hoje é que dia' in comando:
            now = datetime.datetime.now()
            data = now.strftime("%d/%m/%Y")
            talk("Hoje é" + data)
            pc.runAndWait()
    
        if 'em que data estamos' in comando:
            now = datetime.datetime.now()
            data = now.strftime("%d/%m/%Y")
            talk("Hoje é" + data)
            pc.runAndWait()
            
        #--------------------------------------------Funçôes----------------------------------------------------
    
        if 'que funções dispões' in comando:
            talk('')
            pc.runAndWait()

        if 'o que fazes' in comando:
            talk('')
            pc.runAndWait()

        if 'que funções fazes' in comando:
            talk('')
            pc.runAndWait()

        if 'fazes o quê' in comando:
            talk('')
            pc.runAndWait()

            
        #----------------------------------------Comandos (LIGAR)--------------------------------------------------

        if 'liga a luz do quarto 1' in comando:
            db.child("551EVh").set(2)
            talk('Ligado')
            pc.runAndWait()

        if 'liga a luz do quarto 2' in comando:
            db.child("6ez3O4").set(2)
            talk('Ligado')
            pc.runAndWait()

        if 'liga a luz do quarto 3' in comando:
            db.child("75Pd67").set(2)
            talk('Ligado')
            pc.runAndWait()

        if 'liga a luz da sala' in comando:
            db.child("458Xps").set(2)
            talk('Ligado')
            pc.runAndWait()
            
        #----------------------------------------Comandos (DESLIGAR)--------------------------------------------------

        if 'desliga a luz do quarto 1' in comando:
            db.child("551EVh").set(0)
            talk('Desligado')
            pc.runAndWait()

        if 'desliga a luz do quarto 2' in comando:
            db.child("6ez3O4").set(0)
            talk('Desligado')
            pc.runAndWait()

        if 'desliga a luz do quarto 3' in comando:
            db.child("75Pd67").set(0)
            talk('Desligado')
            pc.runAndWait()

        if 'desliga a luz da sala' in comando:
            db.child("458Xps").set(0)
            talk('Desligado')
            pc.runAndWait()

        #----------------------------------------Comandos (TEMPERATURA)------------------------------------------------

            

        #--------------------MEDIA------------------------

        if 'como está o tempo em casa' in comando:
            talk('Desligado')
            pc.runAndWait()

        if 'tempo em casa' in comando:
            talk('Desligado')
            pc.runAndWait()

        if 'como é está o tempo em casa' in comando:
            talk('Desligado')
            pc.runAndWait()

        if 'que tempo está em casa' in comando:
            talk('Desligado')
            pc.runAndWait()

        if 'qual é o tempo em casa' in comando:
            talk('Desligado')
            pc.runAndWait()
    
    #----------------------------------------Tratamento de erros-------------------------------------------------
    
#_______________________________________________________________________________________________________________




#_______________________________________________________________________________________________________________


#                                       Configuração de um ciclo loop

while True:
        run_sofia()


#_______________________________________________________________________________________________________________

