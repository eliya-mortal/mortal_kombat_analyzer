import asyncio
from analyzer import run_analysis_all
import datetime

def schedule_analysis_loop(application):
    async def loop_task():
        while True:
            print(f"Running scheduled analysis at {datetime.datetime.now()}")
            await run_analysis_all()
            await asyncio.sleep(300)  # هر 5 دقیقه

    application.create_task(loop_task())