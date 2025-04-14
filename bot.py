    from telegram import Update
    from telegram.ext import Application, CommandHandler, ContextTypes
    import os

    DATA_DIR = "data"

    # فرمان /start
    async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text("سلام! ربات تحلیل‌گر Mortal Kombat فعال شد.")

    # فرمان /report
    async def report(update: Update, context: ContextTypes.DEFAULT_TYPE):
        filepath = os.path.join(DATA_DIR, "daily_report.pdf")
        if os.path.exists(filepath):
            await update.message.reply_document(document=open(filepath, "rb"))
        else:
            await update.message.reply_text("گزارش روزانه هنوز آماده نشده.")

    # فرمان /getfile_5_0
    async def getfile_5_0(update: Update, context: ContextTypes.DEFAULT_TYPE):
        filepath = os.path.join(DATA_DIR, "full_5_0_matches.pdf")
        if os.path.exists(filepath):
            await update.message.reply_document(document=open(filepath, "rb"))
        else:
            await update.message.reply_text("فایلی برای بازی‌های ۵-۰ موجود نیست.")

    # فرمان /getfile_karaktermatch
    async def getfile_karaktermatch(update: Update, context: ContextTypes.DEFAULT_TYPE):
        filepath = os.path.join(DATA_DIR, "karakter_match_analysis.pdf")
        if os.path.exists(filepath):
            await update.message.reply_document(document=open(filepath, "rb"))
        else:
            await update.message.reply_text("تحلیل بازی‌های مشابه یافت نشد.")

    # فرمان /getfile_zarib
    async def getfile_zarib(update: Update, context: ContextTypes.DEFAULT_TYPE):
        filepath = os.path.join(DATA_DIR, "zarib_analysis.pdf")
        if os.path.exists(filepath):
            await update.message.reply_document(document=open(filepath, "rb"))
        else:
            await update.message.reply_text("فایل تحلیل ضرایب یافت نشد.")

    # ثبت همه فرمان‌ها
    def register_handlers(app: Application):
        app.add_handler(CommandHandler("start", start))
        app.add_handler(CommandHandler("report", report))
        app.add_handler(CommandHandler("getfile_5_0", getfile_5_0))
        app.add_handler(CommandHandler("getfile_karaktermatch", getfile_karaktermatch))
        app.add_handler(CommandHandler("getfile_zarib", getfile_zarib))