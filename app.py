# app.py
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from bot.core import responder_mensagem

app = Flask(__name__)

@app.route("/webhook", methods=['POST'])
def webhook():
    # Extrai a mensagem recebida do WhatsApp
    mensagem_entrada = request.form.get('Body')

    # Usa a função do core.py para gerar a resposta
    resposta_texto = responder_mensagem(mensagem_entrada)

    # Cria a resposta no formato que o Twilio entende
    resposta = MessagingResponse()
    resposta.message(resposta_texto)

    return str(resposta)

if __name__ == "__main__":
    # Inicia o servidor Flask localmente
    app.run(debug=True)
