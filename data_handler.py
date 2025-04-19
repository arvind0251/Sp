# data_handler.py

import json, os
from constants import DATA_FILE

# In-Memory Data
USER_DATA = {}
SERVICE_PRICING = {}
COUNTRIES = {}
PROMO_CODES = {}

def save_data():
    data = {
        "USER_DATA": USER_DATA,
        "SERVICE_PRICING": SERVICE_PRICING,
        "COUNTRIES": COUNTRIES,
        "PROMO_CODES": PROMO_CODES
    }
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

def load_data():
    global USER_DATA, SERVICE_PRICING, COUNTRIES, PROMO_CODES
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
            USER_DATA = data.get("USER_DATA", {})
            SERVICE_PRICING = data.get("SERVICE_PRICING", {})
            COUNTRIES = data.get("COUNTRIES", {})
            PROMO_CODES = data.get("PROMO_CODES", {})
