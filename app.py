from flask import Flask, jsonify, request

USUARIOS = [
    {
        'cpf': 10000000000,
        'nome': 'Tulio',
        'data_nascimento': '20-12-2002'
    }
]

app = Flask(__name__)

@app.route("/usuarios/", methods=["POST"])
def criar_usuario():
    usuario = request.get_json()
    USUARIOS.append(usuario)
    return jsonify(USUARIOS)

@app.route("/usuarios/<int:cpf>/", methods=["GET"])
def obter_usuario(cpf):
    for usuario in USUARIOS:
        if usuario.get('cpf') == cpf:
            return jsonify(usuario)
        else: return jsonify({"erro": "Usuário não encontrado"})

if __name__ == "__main__":
    app.run(port=5000, host='localhost', debug=True)