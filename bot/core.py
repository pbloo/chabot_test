# bot/core.py

# Este arquivo define a lógica do bot (o que responder ao cliente)

def process_whatsapp_message(message, sender):
    """
    Recebe a mensagem e o número do cliente e retorna a resposta adequada.
    """
    # Remove espaços em branco e coloca em minúsculo
    msg = message.strip().lower()

    # Se for a primeira interação ou mensagem inicial
    if msg in ['oi', 'olá', 'bom dia', 'boa tarde', 'boa noite']:
        return (
            "Olá! 👋 Para agilizar seu atendimento, escolha uma das opções abaixo. "
            "Digite apenas o número da opção:\n\n"
            "1 - Status do meu pedido 📦\n"
            "2 - Troca ou devolução 🔁\n"
            "3 - Falar com um atendente 👩‍💻\n"
            "4 - Encerrar atendimento ❌"
        )

    # Verifica a opção escolhida
    elif msg == '1':
        return "Você selecionou *Status do pedido*. Por favor, informe o número do pedido."

    elif msg == '2':
        return "Você escolheu *Troca ou devolução*. Por favor, nos diga qual o motivo da solicitação."

    elif msg == '3':
        return "Estamos transferindo você para um atendente humano. Por favor, aguarde um momento."

    elif msg == '4':
        return "Atendimento encerrado. Agradecemos o contato! 🙏"

    # Caso o cliente digite algo inesperado
    else:
        return (
            "Desculpe, não entendi sua mensagem. Por favor, digite apenas o número da opção desejada:\n"
            "1 - Status do meu pedido\n"
            "2 - Troca ou devolução\n"
            "3 - Falar com um atendente\n"
            "4 - Encerrar atendimento"
        )
