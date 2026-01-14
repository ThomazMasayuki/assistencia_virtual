from speech_to_text import ouvir
from text_to_speech import falar
from commands import executar_comando

falar("Olá! Sou o assistente virtual do Thomaz Masayuki. O que você deseja hoje?")

while True:
    comando = ouvir()
    
    if comando:
        if "sair" in comando:
            falar("Até mais!")
            break

        resposta = executar_comando(comando)
        print(resposta)
        falar(resposta)
