# DocBrain AI

Chatbot inteligente baseado em RAG (Retrieval-Augmented Generation) utilizando Ollama e embeddings para responder perguntas com base em documentos.

## 🚀 Funcionalidades

- Leitura de documentos PDF
- Geração de embeddings
- Busca contextual inteligente
- Respostas baseadas no conteúdo dos arquivos
- Integração com modelos locais via Ollama
- Sistema preparado para futuras integrações:
  - WhatsApp Web
  - Gemini API
  - Telegram

## 🛠️ Tecnologias

- Python
- Ollama
- LangChain
- FAISS
- PyPDF
- Embeddings
- IA Generativa

## 📂 Estrutura

```bash
chatbot/
│
├── datas/
├── embeddings/
├── models/
├── main.py
├── requirements.txt
└── README.md
```

## ⚙️ Instalação

Clone o projeto:

```bash
git clone https://github.com/yVictor0/knowledge-rag-assistant.git
```

Entre na pasta:

```bash
cd knowledge-rag-assistant
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute o projeto:

```bash
python main.py
```

## 🧠 Como funciona

O sistema:
1. Lê os documentos
2. Cria embeddings vetoriais
3. Armazena o contexto
4. Busca informações relevantes
5. Gera respostas usando IA

## 📌 Objetivos futuros

- Integração com WhatsApp Web
- Suporte à Gemini API
- Interface web
- Memória de conversa
- Suporte multimodal

## 👨‍💻 Autor

Yan Victor