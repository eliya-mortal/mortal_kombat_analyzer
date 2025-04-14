
import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from analyzer_bot import run_analysis_all, send_daily_reports
from handlers import (
    start,
    get_report,
    get_5_0,
    get_karakter_match,
    get_odd_stats,
)
from config import BOT_TOKEN as TOKEN


async def loop_task():
    while True:
        await run_analysis_all(bot)
        await asyncio.sleep(300)  # هر 5 دقیقه


async def daily_task():
    while True:
        now = asyncio.get_event_loop().time()
        target = ((24 * 60 * 60) - 60)  # ساعت 23:59
        await asyncio.sleep(target - (now % (24 * 60 * 60)))
        await send_daily_reports(bot)


async def main():
    app = Application.builder().token(TOKEN).build()

    # ثبت دستورات
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("report", get_report))
    app.add_handler(CommandHandler("getfile_5_0", get_5_0))

    app.add_handler(CommandHandler("getfile_karaktermatch", get_karakter_match))
    app.add_handler(CommandHandler("getfile_oddstats", get_odd_stats))

    # اجرای تسک‌های جداگانه
    asyncio.create_task(loop_task())
    asyncio.create_task(daily_task())

    # شروع ربات
    await app.run_polling()


if __name__ == "__main__":
    try:
        asyncio.run(main())
except RuntimeError
        loop = asyncio.get.event_loop()
        loop.run_until_complete(main())
