from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
import os
from dotenv import load_dotenv

from agents.chat_agent import generate_reply
from agents.sales_agent import handle_sales
from utils.memory import add_message, get_conversation

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN environment variable is not set.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.message.chat_id)
    message = update.message.text

    sales_reply = handle_sales(user_id, message)
    if sales_reply:
        await update.message.reply_text(sales_reply)
        return

    add_message(user_id, "User", message)
    conversation = get_conversation(user_id)

    reply = generate_reply(message, conversation)

    add_message(user_id, 'AI', reply)

    await update.message.reply_text(reply)

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
app.run_polling()