import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')

MK11_DIR = os.path.join(DATA_DIR, 'mk11')
MKX_DIR = os.path.join(DATA_DIR, 'mkx')

# مسیر فایل‌های MK11
MK11_MATCHES_PDF = os.path.join(MK11_DIR, 'matches.pdf')
MK11_5_0_PDF = os.path.join(MK11_DIR, '5_0_matches.pdf')
MK11_SIMILAR_PDF = os.path.join(MK11_DIR, 'similar_character_matches.pdf')
MK11_DAILY_REPORT_PDF = os.path.join(MK11_DIR, 'daily_report.pdf')
MK11_ZARIB_ANALYSIS_PDF = os.path.join(MK11_DIR, 'zarib_analysis.pdf')

# مسیر فایل‌های MKX
MKX_MATCHES_PDF = os.path.join(MKX_DIR, 'matches.pdf')
MKX_5_0_PDF = os.path.join(MKX_DIR, '5_0_matches.pdf')
MKX_SIMILAR_PDF = os.path.join(MKX_DIR, 'similar_character_matches.pdf')
MKX_DAILY_REPORT_PDF = os.path.join(MKX_DIR, 'daily_report.pdf')
MKX_ZARIB_ANALYSIS_PDF = os.path.join(MKX_DIR, 'zarib_analysis.pdf')