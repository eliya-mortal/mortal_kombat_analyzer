
import requests
import pandas as pd
from datetime import datetime

MELBET_URLS = {
    "mk11": "https://melbet.com/feeds/line/event/ext/en/all/Mortal%20Kombat%2011",
    "mkx": "https://melbet.com/feeds/line/event/ext/en/all/Mortal%20Kombat%20X"
}

def get_mk11_data():
    return fetch_melbet_data(MELBET_URLS["mk11"])

def get_mkx_data():
    return fetch_melbet_data(MELBET_URLS["mkx"])

def fetch_melbet_data(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        parsed_data = []

        for event in data.get("Value", []):
            match_id = event.get("EId")
            start_time = datetime.utcfromtimestamp(event.get("S", 0)).strftime('%Y-%m-%d %H:%M:%S')
            player1 = event.get("O1")
            player2 = event.get("O2")
            odds = event.get("E", [])

            p1_odds = None
            p2_odds = None

            for odd in odds:
                if odd.get("T") == 1:
                    p1_odds = odd.get("C")
                elif odd.get("T") == 2:
                    p2_odds = odd.get("C")

            parsed_data.append({
                "match_id": match_id,
                "start_time": start_time,
                "player1": player1,
                "player2": player2,
                "player1_odds": p1_odds,
                "player2_odds": p2_odds
            })

        return pd.DataFrame(parsed_data)

    except Exception as e:
        print(f"Error fetching data from Melbet: {e}")
        return pd.DataFrame()
