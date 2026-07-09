import os

import urllib3
from dotenv import load_dotenv
from twilio.rest import Client

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

load_dotenv(override=True)

def simular_api_correios():
    """
    Simula uma requisição à API dos Correios para buscar o status de uma encomenda.
    Para testar o script, basta alterar o texto da 'descricao' abaixo!"""
    # TESTE AQUI: Mude este texto depois  para ver o WhatsApp funcionar.
    return {
        "codigo": "AN310228949BR",
        "serico": "Correios",
        "ultimo_status": {
            "data": "2023-09-01",
            "hora": "10:00",
            "local": "Porto Alegre",
            "descricao": "Objeto em deslocamento para Porto Alegre.",
        }
    }

def verificar_rastreamento():
    dados = simular_api_correios()

    codigo = dados["codigo"]
    status_atual = dados["ultimo_status"]["descricao"]
    data = dados["ultimo_status"]["data"]
    local = dados["ultimo_status"]["local"]

    arquivo_historico = "historico.txt"

    if not os.path.exists(arquivo_historico):
        with open(arquivo_historico, "w", encoding="utf-8") as f:
            f.write("")
    
    with open(arquivo_historico, "r", encoding="utf-8") as f:
        status_anterior = f.read().strip()
    
    print(f"Status atual da API: {status_atual}")
    print(f"Status anterior do arquivo: {status_anterior}")

    if status_atual != status_anterior:
        print("ATENÇAO: O status mudou! atualizando historico e enviando mensagem...")

        with open(arquivo_historico, "w", encoding="utf-8") as f:
            f.write(status_atual)

                   
        texto_alerta = (
            f" Atualizaçao da encomenda {codigo}\n"
            f" Status: {status_atual}\n"
            f" Data: {data}\n"
            f" Local: {local}"
        )

        client = Client(os.getenv("TWILIO_ACCOUNT_SID"), os.getenv("TWILIO_AUTH_TOKEN"))
        client.messages.create(
            from_=os.getenv("TWILIO_PHONE_NUMBER"),
            body=texto_alerta,
            to=os.getenv("PHONE_NUMBER")
        )



        print("whatsapp enviado com sucesso!")
    else:
        print("Nao houve atualizacao no status da encomenda.")


verificar_rastreamento()