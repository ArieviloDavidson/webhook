# Teste de Recebimento de Webhooks com Python e Flask

Este projeto demonstra como criar um servidor local com Python e Flask para receber e processar requisições de webhooks, utilizando Ngrok para exposição à internet e Insomnia para testes de envio.

## Pré-requisitos

- Python 3.x instalado.
- **Ngrok** para expor seu servidor local. [Faça o download aqui](https://ngrok.com/download).
- Um cliente de API como o **Insomnia** (usado neste guia) ou Postman.
- Bibliotecas necessárias (instale com `pip install -r requirements.txt`)

## Como Usar

1. **Clone o repositório**:

    ```bash
    git clone <url-do-repositorio>
    cd webhook
    cd receive_webhook
    ```

2. **Inicie o Servidor Flask**

    - Execute o main.py para iniciar seu servidor local. Por padrão, ele rodará na porta 5000.
    ```bash
    python main.py
    ```
    - Observação: Mantenha este terminal rodando. Ele mostrará os logs de recebimento dos webhooks.

3. **Exponha seu Servidor com Ngrok**
    - Abra um novo terminal e inicie o Ngrok para criar um túnel para a porta 5000.
    ```bash
    ngrok http 5000
    ```
    - O Ngrok gerará uma URL pública. Copie a URL https da linha "Forwarding". Ela será algo como: https://aleatorio.ngrok-free.app.

4. **Envie um Webhook de Teste com Insomnia (Postman ou qualquer outra método de sua escolha)**

    - Crie uma nova requisição do tipo POST.
    - No campo da URL, cole a sua URL do Ngrok e adicione a rota definida no Flask (ex: /meu-webhook).
    - Vá para a aba Body e selecione o formato JSON.
    ```bash
    JSON
    {
    "nome": "Davidson Oliveira",
    "evento": "compra_aprovada",
    "id_usuario": "usr_12345",
    "valor": 99.90
    }
    ```

5. **Valide o Recebimento**
    - Se tudo correu bem, você terá a confirmação em três lugares:

    5.1 **No Insomnia:** Você verá a resposta da sua aplicação Flask no painel de resposta, com o status 200 OK.
    ```bash
    {
    "status": "sucesso",
    "mensagem": "Dados recebidos com sucesso!"
    }
    ```
    5.2 **No terminal do Flask:** Você verá as mensagens que definimos no print(), confirmando que os dados foram recebidos e processados no seu código Python.

    5.3 **No terminal do Ngrok:** Você verá um log da requisição POST com o status 200 OK.

## Personalização
- Edite o arquivo main.py para adaptar o tratamento dos dados recebidos. Você pode mudar a rota (de /receive_data para outra de sua preferência) ou adicionar lógicas mais complexas dentro da função para salvar os dados em um banco de dados, chamar outra API, etc.

## Observações
- O servidor iniciado com python main.py é um servidor de desenvolvimento. Para um ambiente de produção, utilize um servidor WSGI como Gunicorn ou uWSGI.

## Suporte

Em caso de dúvidas, consulte o código-fonte ou abra uma issue no repositório.