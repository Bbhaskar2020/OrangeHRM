# utils/helpers.py
import os
from datetime import datetime

def ensure_reports_dirs():
    os.makedirs("reports/html", exist_ok=True)
    os.makedirs("reports/screenshots", exist_ok=True)

def timestamp():
    return datetime.now().strftime("%Y%m%d_%H%M%S")
