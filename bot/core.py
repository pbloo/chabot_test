def responder_mensagem(mensagem):
    mensagem = mensagem.lower()

    if "horário" in mensagem:
        return "Nosso horário de atendimento é de segunda a sexta, das 9h às 18h."
    elif "email" in mensagem:
        return "Você pode enviar um e-mail para pablofabiano.oliveira@gmail.com"
    elif "suporte" in mensagem:
        return "Estou aqui para ajudar! Qual é o problema?"
    else:
        return "Desculpe, não entendi. Você pode reformular sua dúvida?"