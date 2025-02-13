import google.generativeai as genai
import datetime
import pyttsx3
import speech_recognition as sr

def main():

    falar = True
    ligar_microfone = True

    genai.configure(api_key='AIzaSyDMoVjou1LTo5_UL2d0SWxYhDnvGA7h7X4')  # Configura a chave da API do Google

    model = genai.GenerativeModel('gemini-pro')  # Escolhe o modelo de IA generativa

    chat = model.start_chat(history=[])  # Inicia uma conversa

    # Configuração da voz
    if falar:
        engine = pyttsx3.init()  # Inicializa o mecanismo de sintetização de voz

        voices = engine.getProperty('voices')  # Obtém as vozes disponíveis
        engine.setProperty('rate', 180)  # Configura a velocidade da fala

        print('\n Lista de vozes - Verifique o número \n')  # Exibe uma lista de vozes disponíveis

        for indice, vozes in enumerate(voices):
            print(indice, vozes.name)  # Exibe o índice e o nome da voz

        voz = 0

        engine.setProperty('voice', voices[voz].id)  # Define a voz

        if ligar_microfone:
            r = sr.Recognizer()  # Inicializa o reconhecedor de fala
            mic = sr.Microphone()  # Inicializa o microfone

    bem_vindo = '// Bem vindo ao seu assistente virtual //'
    print(len(bem_vindo)*'#')
    print(bem_vindo)
    print(len(bem_vindo)*'#')
    print('// Digite "sair" para encerar //')
    print('')

    while True:
        if ligar_microfone:
            with mic as fonte:
                r.adjust_for_ambient_noise(fonte) # Ajustar de acordo com o ambiente
                print('Fale algo ou diga(desligar)')
                audio = r.listen(fonte) # Ouvir a fala
                print('Reconhecendo')
            try:
                texto = r.recognize_google(audio, language='pt-BR') # Trsnsformar apartir do google
                if texto:
                    print(f'Você disse: {texto}')
            except Exception as e:
                print("Não entendi o que você disse. Erro:", e)
                texto = ""
                continue  # Volta para o início do loop para tentar novamente
        else:
            texto = input("Escreva sua mensagem (ou #sair): ")


        if texto.lower() == "desligar":  # Condição para encerrar o programa se o texto for 'desligar'
            break  # Sai do loop while se 'desligar' for digitado

        response = chat.send_message(texto)  # Envia a mensagem para o modelo de IA e recebe uma resposta
        print("Tati:", response.text, "\n")  # Exibe a resposta do modelo

        if falar:  # Verifica se a opção de falar está habilitada
            text_to_speak = response.text.replace('#', '').replace('*', '')  # Remove '#' e '*' da resposta
            engine.say(text_to_speak)  # Sintetiza a resposta em fala
            engine.runAndWait()  # Aguarda a finalização da fala

    print("Encerrando Chat")  # Exibe mensagem de encerramento ao sair do loop while



if __name__ == '__main__':
    main()
