# 📦 Rastreador de Encomendas Inteligente com Alertas via WhatsApp

Este é um projeto em Python desenvolvido para monitorar o status de rastreamento de encomendas e enviar notificações automáticas e instantâneas diretamente para o WhatsApp do utilizador sempre que houver uma alteração no estado do envio.

|Foi implementado um **sistema de gestão de estados local**, que impede o envio de notificações duplicadas ou repetidas, otimizando o consumo de recursos e o envio de mensagens.

## 🚀 Funcionalidades

- **Monitorização Automatizada:** Estrutura preparada para ler atualizações de objetos postados.
- **Gestão de Histórico** O script guarda o último estado num arquivo local (`historico.txt`) e compara com a nova leitura. O alerta só é disparado se o status atual for diferente do anterior.
- **Notificação em Tempo Real:** Integração com a API do Twilio para disparo de mensagens formatadas no WhatsApp.
- **Segurança da Informação:** Uso de variáveis de ambiente (`.env`) para proteção total de credenciais sensíveis (Account SID e Auth Token), seguindo as boas práticas de mercado.

## 🛠️ Tecnologias Utilizadas

- **Python 3.10+**
- **Twilio SDK:** Para a integração e envio de mensagens para o WhatsApp.
- **Python-dotenv:** Para a gestão segura de variáveis de ambiente.
- **Os (Módulo Nativo):** Para manipulação de arquivos locais e controlo de fluxo.

## 📁 Estrutura do Projeto

```text
rastreador_correios/
│
├── venv/                  # Ambiente virtual isolado
├── .env                  # Chaves secretas (Ignorado no Git)
├── .gitignore            # Configuração de exclusão do Git
├── historico.txt         # Arquivo de controlo de estado local (Ignorado no Git)
└── rastreador_objeto.py  # Código principal com a lógica do sistema
