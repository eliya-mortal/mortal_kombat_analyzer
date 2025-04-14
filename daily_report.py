import asyncio
from file_sender import send_daily_reports
import datetime

def schedule_daily_report(application):
    async def report_task():
        while True:
            now = datetime.datetime.now()
            target = now.replace(hour=23, minute=59, second=0, microsecond=0)
            if now > target:
                target = target + datetime.timedelta(days=1)
            wait_seconds = (target - now).total_seconds()
            await asyncio.sleep(wait_seconds)
            print(f"Running daily report at {datetime.datetime.now()}")
            await send_daily_reports()

    application.create_task(report_task())