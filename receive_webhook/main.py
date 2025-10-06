# O que é um webhook?
# Um webhook é uma maneira de um aplicativo fornecer informações em tempo real para outros aplicativos.
# Ele é um "gancho" que permite que um aplicativo envie dados automaticamente para outro aplicativo quando um evento específico ocorre.

# Nesse exemplo, vou usar o site webhook.site para criar um webhook e receber um envio POST dele.

from flask import Flask, request, jsonify

# Criando a aplicação Flask
app = Flask(__name__)
# O 'methods=['POST']' significa que esta rota só aceita requisições do tipo POST.
@app.route('/receive_data', methods=['POST'])

# Função que será executada quando o webhook for chamado.
def webhook_receive():
    print("🚀 Webhook recebido!")

    # Por padrão, os dados enviados em um webhook podem estar em diferentes formatos, mas o mais comum é JSON.
    # Vamos verificar isso no parametro 'request' do Flask.
    if request.is_json:
        data = request.get_json()
        print("Dados recebidos (JSON):")
        print(data)
        
        # Vamos fazer algo simples com os dados recebidos.
        if 'nome' in data:
            print(f"Olá, {data['nome']}!")

        # Retorna uma resposta de sucesso em JSON
        return jsonify({"status": "sucesso", "mensagem": "Dados recebidos com sucesso!"}), 200
    else:
        # Se os dados não forem JSON
        data = request.data.decode('utf-8')
        print("Dados recebidos (não-JSON):")
        print(data)
        return jsonify({"status": "sucesso", "mensagem": "Dados brutos recebidos com sucesso!"}), 200

# Uma espécie de While True para manter o servidor rodando.
if __name__ == '__main__':
    # Por padrão roda na porta 5000
    app.run(debug=True)