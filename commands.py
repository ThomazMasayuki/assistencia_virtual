import wikipedia
import webbrowser

wikipedia.set_lang("pt")

def executar_comando(texto):
    if "wikipedia" in texto:
        termo = texto.replace("pesquisar", "").replace("wikipedia", "")
        resultado = wikipedia.summary(termo, sentences=2)
        return resultado

    elif "youtube" in texto:
        webbrowser.open("https://www.youtube.com")
        return "Abrindo o YouTube"
    
    elif "gmail" in texto:
        webbrowser.open_new("https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox")
        return "Abrindo o seu gmail, Thomaz"
    
    elif "google" in texto:
        query = "ver as notícias de hoje"
        url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
        webbrowser.open_new(url)
        return "Mostrando as notícias de hoje"

    else:
        return "Não entendi o comando"
