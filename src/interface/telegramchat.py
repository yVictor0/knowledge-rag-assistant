from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from src.services.ia import responder as chatbotgenai
from src.core.vector_store import criar_index
from main import build_base  # 👈 reaproveita seu main
import asyncio

TOKEN = "8677155401:AAE1_gvE4uPsY-qd0a_oOIZE352vlRNvgTU"

# 🔥 tenta carregar base automaticamente
try:
    index, dados = criar_index()
except FileNotFoundError:
    print("Base Não Encontrada")
    if build_base():
        index, dados = criar_index()
    else:
        raise Exception("Erro ao criar base.")

# memória por usuário
historicos = {}


async def start(update, context):
    await update.message.reply_text("Olá! Sou a assistente da clínica 🤖")


import asyncio

async def responder(update, context):
    user_id = update.message.chat_id
    pergunta = update.message.text.strip()

    if user_id not in historicos:
        historicos[user_id] = []

    historico = historicos[user_id]

    msg = await update.message.reply_text("Pensando")

    try:
        print("Chamando")

        resposta = await asyncio.to_thread(
            chatbotgenai, pergunta, index, dados, historico
        )

        print("IA respondeu")

        historico.append(f"Usuário: {pergunta}")
        historico.append(f"Assistente: {resposta}")

        await msg.edit_text(resposta)

    except Exception as e:
        print("ERRO:", e)
        await msg.edit_text("Deu erro aqui")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, responder))

print("Bot rodando")
app.run_polling()