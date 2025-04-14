from telegram import Update
from telegram.ext import ContextTypes
from file_sender import send_pdf_file


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام! به ربات تحلیل Mortal Kombat خوش اومدی.")


async def get_report(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for version in ["mk11", "mkx"]:
        await send_pdf_file(update, context, f"data/{version}/daily_report.pdf", f"گزارش روزانه ({version.upper()})")


async def get_5_0(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for version in ["mk11", "mkx"]:
        await send_pdf_file(update, context, f"data/{version}/5_0_matches.csv", f"لیست بازی‌های 5-0 ({version.upper()})")


async def get_karakter_match(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for version in ["mk11", "mkx"]:
        await send_pdf_file(update, context, f"data/{version}/similar_character_matches.pdf", f"بازی‌های مشابه کاراکترها ({version.upper()})")


async def get_odd_stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for version in ["mk11", "mkx"]:
        await send_pdf_file(update, context, f"data/{version}/zarib_analysis.pdf", f"تحلیل ضرایب راند اول ({version.upper()})")


# اگر نیاز به دستور خاص‌تری هست (مثلاً ارسال فایل matches.pdf یا چیزی مشابه)، بگو تا اضافه کنم.
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "دستورهای موجود:\n"
        "/getfile_5_0 - دریافت بازی‌های 5-0\n"
        "/getfile_100 - دریافت آمار ضریب‌ها\n"
        "/getfile_karaktermatch - دریافت بازی‌های مشابه کاراکتر\n"
        "/report - دریافت گزارش روزانه\n"
        "/help - راهنما\n"
        "/about - درباره ربات"
    )

async def about_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("این ربات برای تحلیل بازی‌های Mortal Kombat ساخته شده و هر شب گزارش کامل ارائه می‌دهد.")