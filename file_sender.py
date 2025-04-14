import os
import pandas as pd
from fpdf import FPDF
from telegram import Update, Bot
from telegram.ext import ContextTypes
from datetime import datetime

# توکن ربات و آی‌دی عددی کاربر
BOT_TOKEN = "7268093859:AAGqBfvKNsmcfEHRRJBIk58k-9W6qv4zJzM"
USER_ID = 639020566
bot = Bot(token=BOT_TOKEN)

def send_document(chat_id, document, caption=""):
    return bot.send_document(chat_id=chat_id, document=document, caption=caption)

def generate_pdf_from_dataframe(df, title, filename):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=title, ln=True, align='C')
    pdf.ln(10)

    for col in df.columns:
        pdf.cell(40, 10, col, border=1)
    pdf.ln()

    for index, row in df.iterrows():
        for item in row:
            pdf.cell(40, 10, str(item), border=1)
        pdf.ln()

    pdf.output(filename)
    return filename

# این تابع برای استفاده در handlers
async def send_pdf_file(update: Update, context: ContextTypes.DEFAULT_TYPE, file_path: str, caption: str = ""):
    try:
        if os.path.exists(file_path):
            with open(file_path, "rb") as file:
                await update.message.reply_document(document=file, caption=caption)
        else:
            await update.message.reply_text(f"فایل پیدا نشد: {file_path}")
    except Exception as e:
        await update.message.reply_text(f"خطا در ارسال فایل: {e}")