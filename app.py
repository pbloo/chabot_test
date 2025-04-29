from flask import Flask, request, jsonify
from bot.core import responder_mensagem

app = Flask(__name__)

@app.route("/mensagem", methods=["POST"])
def receber_mensagem():
    dados = request.json
    mensagem = dados.get("mensagem","")

    resposta = responder_mensagem(mensagem)
    return jsonify({"resposta": resposta})

if __name__ == "__main__":
    app.run (debug=True)