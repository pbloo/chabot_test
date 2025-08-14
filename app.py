from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from bot.core import process_whatsapp_message  # Importando a função do bot para processar a mensagem

app = Flask(__name__)

# Rota para capturar mensagens do Twilio
@app.route('/webhook', methods=['POST'])
def webhook():
    """Processa a mensagem recebida e envia a resposta do bot"""
    # Obtém a mensagem do cliente
    message = request.form.get('Body')
    sender = request.form.get('From')
    
    # Processa a mensagem e obtém a resposta
    response_message = process_whatsapp_message(message, sender)

    # Cria uma resposta Twilio
    response = MessagingResponse()
    response.message(response_message)

    return str(response)

if __name__ == '__main__':
    app.run(debug=True)