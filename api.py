import sounddevice as sd
import wavio
import base64
import requests
import os

def gravarAudio(nomeArquivo, duracaoSegundos):
    print("Gravando...")
    audio = sd.rec(int(duracaoSegundos * 44100), samplerate=44100, channels=1, dtype='int16')
    sd.wait()
    # print("Gravação concluída!")
    wavio.write(nomeArquivo, audio, 44100, sampwidth=2)
    # return audio

def analisarAudio(audio, apiKey):
    print("Analizando o audio...")
    audioData = open(nomeArquivo, 'rb').read()
    audioDataBase64 = base64.b64encode(audioData).decode('utf-8')
    # print(audioDataBase64)


    url = "https://shazam.p.rapidapi.com/songs/detect"



    # print(audio_data, "Conteúdo do arquivo:")

    headers = {
        "content-type": "text/plain",
        "x-rapidapi-host": "shazam.p.rapidapi.com",
        "x-rapidapi-key": "Enter_apiKey_here"
    }

    data = audioDataBase64
    # print(data)

    try:
        response = requests.request("POST",url, data=data, headers=headers)
        response.raise_for_status()
        # print("Resposta da API:", response.text)
        song = response.json()
        return [
            song['track']['title'],song['track']['subtitle']
        ]
    except requests.exceptions.RequestException as e:
        print("Erro fazendo request na API:", e)
        return None

nomeArquivo = "gravacao.wav"
duracaoSegundos = 5
apiKey = "Enter_apiKey_here" 

audio = gravarAudio(nomeArquivo, duracaoSegundos)

resultadoAnalise = analisarAudio(audio, apiKey)

if resultadoAnalise is not None:
    print("...")
    print(resultadoAnalise)
else:
    print("Problemas com a API")