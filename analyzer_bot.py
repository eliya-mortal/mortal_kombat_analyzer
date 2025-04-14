import os
import csv
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from telegram import Bot
from melbet_scraper import get_mk11_data, get_mkx_data

# توابع ساخت PDFها برای هر نسخه
def analyze_zarib(version: str):
    pdf_path = f"data/{version}/zarib_analysis.pdf"
    c = canvas.Canvas(pdf_path, pagesize=letter)
    c.drawString(100, 750, f"تحلیل ضریب برد راند - {version}")
    c.save()

def analyze_similar_matches(version: str):
    pdf_path = f"data/{version}/similar_character_matches.pdf"
    c = canvas.Canvas(pdf_path, pagesize=letter)
    c.drawString(100, 750, f"تحلیل شباهت بازی‌ها - {version}")
    c.save()

def analyze_5_0_matches(version: str):
    pdf_path = f"data/{version}/5_0_matches.pdf"
    c = canvas.Canvas(pdf_path, pagesize=letter)
    c.drawString(100, 750, f"لیست بازی‌های ۵-۰ - {version}")
    c.save()

def analyze_daily_report(version: str):
    pdf_path = f"data/{version}/daily_report.pdf"
    c = canvas.Canvas(pdf_path, pagesize=letter)
    c.drawString(100, 750, f"گزارش روزانه - {version}")
    c.save()

def save_matches_to_csv(matches, filepath):
    if not matches:
        return
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=matches[0].keys())
        writer.writeheader()
        writer.writerows(matches)

# تابع اصلی برای اجرای همه تحلیل‌ها برای mk11 و mkx
async def run_analysis_all(bot):
    versions = ["mk11", "mkx"]
    all_data = {
        "mk11": get_mk11_data(),
        "mkx": get_mkx_data()
    }

    for version in versions:
        # ذخیره داده‌های بازی
        save_matches_to_csv(all_data[version], f"data/{version}/matches.csv")
        # تولید گزارش‌های PDF
        analyze_zarib(version)
        analyze_similar_matches(version)
        analyze_5_0_matches(version)
        analyze_daily_report(version)

# تابع ارسال گزارش‌ها به تلگرام
async def send_daily_reports(bot):
    try:
        versions = {
            "mk11": "data/mk11/daily_report.pdf",
            "mkx": "data/mkx/daily_report.pdf"
        }

        for version, path in versions.items():
            if os.path.exists(path):
                await bot.send_document(chat_id=639020566, document=open(path, "rb"), caption=f"گزارش روزانه {version}")
            else:
                await bot.send_message(chat_id=639020566, text=f"فایل گزارش {version} پیدا نشد.")
    except Exception as e:
        await bot.send_message(chat_id=639020566, text=f"خطا در ارسال گزارش: {e}")
