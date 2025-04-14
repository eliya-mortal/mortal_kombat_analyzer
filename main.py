import asyncio
from telegram.ext import Application, CommandHandler
from handlers import (
    start, get_report, get_5_0, get_karakter_match, get_odd_stats,
    help_command, about_command
)
from config import BOT_TOKEN as TOKEN


async def loop_task(bot):
    while True:
        await run_analysis_all(bot)
        await asyncio.sleep(300)  # هر 5 دقیقه


async def daily_task(bot):
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
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("about", about_command))

    # اجرای تسک‌های جداگانه با bot
    bot = app.bot
    asyncio.create_task(loop_task(bot))
    asyncio.create_task(daily_task(bot))

    # شروع ربات
    await app.run_polling()


if __name__ == "__main__":
    asyncio.run(main())