import json
import os
from fpdf import FPDF
from datetime import datetime
from telegram import Bot

TOKEN = "توکن رباتتو اینجا بذار"
CHAT_ID = "آیدی چت یا گروهتو بذار"

DATA_PATH = "data/matches.json"
OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def load_matches():
    if not os.path.exists(DATA_PATH):
        return []
    with open(DATA_PATH, "r") as f:
        return json.load(f)

def save_pdf(title, rows, columns, filename):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=title, ln=True, align='C')
    pdf.ln(10)
    for col in columns:
        pdf.cell(40, 10, col, border=1)
    pdf.ln()

    for row in rows:
        for item in row:
            pdf.cell(40, 10, str(item), border=1)
        pdf.ln()

    pdf.output(filename)

# 1. بازی‌های ۵-۰
def generate_score_5_0_file(path):
    matches = load_matches()
    rows = []
    for match in matches:
        if match.get("score") == "5-0":
            rows.append([
                match["player1"], match["player2"],
                match["winner"], match["score"]
            ])
    save_pdf("Matches with 5-0 Result", rows, ["Player1", "Player2", "Winner", "Score"], path)

# 2. بازی‌های با کاراکتر و ضریب نزدیک
def generate_karakter_match_file(path):
    matches = load_matches()
    rows = []
    for match in matches:
        if abs(match["odds1"] - match["odds2"]) <= 0.05:
            rows.append([
                match["player1"], match["player2"],
                match["odds1"], match["odds2"], match["result"]
            ])
    save_pdf("Close Odds & Same Characters", rows, ["Player1", "Player2", "Odds1", "Odds2", "Result"], path)

# 3. ضریب راند اول
def generate_round1_odds_file(path):
    matches = load_matches()
    odds_data = {}
    for match in matches:
        odds = match["round1_odds"]
        if odds not in odds_data:
            odds_data[odds] = {"total": 0, "game_wins": 0, "round_wins": 0, "round_losses": 0}
        odds_data[odds]["total"] += 1
        if match["winner"] == match["player_with_round1_odds"]:
            odds_data[odds]["game_wins"] += 1
        odds_data[odds]["round_wins"] += match["rounds_won"]
        odds_data[odds]["round_losses"] += match["rounds_lost"]

    rows = []
    for odds, data in odds_data.items():
        total_rounds = data["round_wins"] + data["round_losses"]
        win_percent = (data["round_wins"] / total_rounds) * 100 if total_rounds else 0
        rows.append([
            odds, data["total"], data["game_wins"],
            data["round_wins"], data["round_losses"],
            f"{win_percent:.2f}%"
        ])
    save_pdf("Round 1 Odds Analysis", rows, ["Odd", "Repeat", "Game Wins", "Rounds Won", "Rounds Lost", "Win %"], path)

# 4. بازه‌های زمانی مشابه
def generate_similarity_periods_file(path):
    matches = load_matches()
    # نمونه‌سازی ساده برای ساخت PDF از لیست بازی‌ها در بازه‌های مشابه
    rows = []
    for match in matches:
        if abs(match["odds1"] - match["odds2"]) <= 0.05 and abs(match["rounds_player1"] - match["rounds_player2"]) <= 1:
            rows.append([
                match["timestamp"], match["player1"], match["player2"],
                match["odds1"], match["odds2"], f"{match['rounds_player1']}-{match['rounds_player2']}"
            ])
    save_pdf("Similarity Periods", rows, ["Time", "Player1", "Player2", "Odds1", "Odds2", "Score"], path)

# 5. ارسال شبانه PDFها
async def send_nightly_report():
    bot = Bot(token=TOKEN)
    filenames = [
        "score_5_0.pdf",
        "karakter_match_analysis.pdf",
        "round1_odds_analysis.pdf",
        "similarity_periods.pdf"
    ]
    for fname in filenames:
        path = os.path.join(OUTPUT_DIR, fname)
        if os.path.exists(path):
            with open(path, "rb") as f:
                await bot.send_document(chat_id=CHAT_ID, document=f, filename=fname)