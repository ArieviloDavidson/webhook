# Teste de Webhooks com Python (APENAS ENVIO)

Este projeto permite testar webhooks localmente usando o arquivo `main.py`.

## Pré-requisitos

- Python 3.x instalado
- Bibliotecas necessárias (instale com `pip install -r requirements.txt`)

## Como usar

1. **Clone o repositório**:

    ```bash
    git clone <url-do-repositorio>
    cd webhook
    ```

2. **Execute o código localmente com sua URL de um site de testes, por exemplo webhook.site:**

    ```bash
    python main.py
    ```

3. **Valide o recebimento do POST no site:**

    - Acesse o site de testes (ex: webhook.site) e verifique se a requisição POST foi recebida corretamente.

4. **Verifique os logs/saída do terminal** para conferir se o webhook foi recebido corretamente.

    - Código 200 é o esperado.

## Personalização

- Edite o arquivo `main.py` para adaptar o tratamento dos dados enviados conforme sua necessidade.

## Observações

- Em breve atualizações para recebimentos de webhook.

## Suporte

Em caso de dúvidas, consulte o código-fonte ou abra uma issue no repositório.