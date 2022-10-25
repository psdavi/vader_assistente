import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pywhatkit


audio = sr.Recognizer()
maquina = pyttsx3.init()

def executa_comando():
    try:
        with sr.Microphone() as source:
            print('Ouvindo..')
            voz = audio.listen(source)
            comando = audio.recognize_google(voz, language='pt')
            comando = comando.lower()
            if 'vader' in comando:
                comando = comando.replace('vader', '')
                maquina.say(comando)
                maquina.runAndWait()

    except:
        print('Microfone não está ok')

    return comando

def comando_voz_usuario():
    comando = executa_comando()
#PESQUISA PELO DIA ATUAL
    if 'que dia' in comando:
        dia = datetime.datetime.now().strftime('%d:%m:%y')
        maquina.say('Hoje é ' + dia)
        print('Hoje é ' + dia)
        maquina.runAndWait()
#PESQUISA UMA BREVE HISTÓRIA DO FERIADO
#FALAR "procure por um feriado" + nome do feriado, "Ex: Dia do trabalhador"
    elif 'procure por feriado' in comando:
        procurar = comando.replace('procure por feriado', '')
        wikipedia.set_lang('pt')
        resultado = wikipedia.summary(procurar,2)
        print(resultado)
        maquina.say(resultado)
        maquina.runAndWait()
    elif 'próximo feriado' in comando:
        procurar = comando.replace('próximo feriado', '')
        maquina.runAndWait()
comando_voz_usuario()









