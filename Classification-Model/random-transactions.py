import random
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

categories = {
    "necessities": {
        "Food": ["Korzinka", "Makro", "Carrefour", "Bi1", "Asia Market"],
        "Transport": ["Yandex Go", "MyTaxi", "UzAuto", "Gas Station UZ", "Petrol Market"],
        "Healthcare": ["Dori-Darmon", "Apteka Plus", "Shifo Med", "Oximed", "Pharmateka"],
        "Clothing": ["OZON UZ", "LC Waikiki", "Globus", "Colins", "ZARA UZ"],
        "Housing": ["Tashkent Utilities", "UzEltech", "Komunalka Pay", "HomeRent.uz"],
        "Education": ["EduMarket UZ", "Cambridge Center", "StudyLand", "IT Park Courses"]
    },
    "wants": {
        "Entertainment": ["Netflix", "Kinomax", "PlayStation Store", "Meloman UZ", "YouTube Premium"],
        "Travel": ["UzAirways", "MyTravel UZ", "Booking.com", "TripExpress"],
        "Hobbies": ["Hobby World", "Kniga.uz", "ArtStore UZ", "PhotoMarket"],
        "Gadgets": ["Texnomart", "MediaPark", "Idea.uz", "MI Store", "Sulpak"],
        "Luxury items": ["Royal Boutique", "Cartier Tashkent", "Gold Market", "Luxury Style"]
    },
    "savings_investments": {
        "Emergency fund": ["Emergency Transfer", "Cash Reserve"],
        "Investments": ["Humo Invest", "CryptoUZ", "TBC Invest", "Freedom Finance"],
        "Retirement funds": ["FuturePension UZ", "RetireNow"]
    },
    "unexpected": {
        "Repairs": ["AutoFix UZ", "HomeRepair Tashkent", "Fixit Center"],
        "Medical emergencies": ["Shoshilinch", "Emergency Clinic", "CityMed Help"],
        "Gifts": ["GiftMe UZ", "Toys.uz", "HappyBox", "Podarki Market"],
        "Fines": ["GIBDD Tashkent", "City Fines", "Penalty Pay"]
    },
    "debts": {
        "Loans": ["Agrobank Loan", "MicroCreditBank", "Alif Nasiya", "Kapitalbank Credit"],
        "Payday loans": ["FastLoan UZ", "EasyMoney", "QarzBer"],
        "Credit card interest": ["Credit Interest", "CardFee UZ"]
    }
}

transactions = []
months = ["2025-01", "2025-02", "2025-03", "2025-04", "2025-05", "2025-06", "2025-07", "2025-08", "2025-09", "2025-10", "2025-11", "2025-12"]	
transaction_id = 10000

for month in months:
    year, mon = map(int, month.split("-"))
    budget = random.randint(15_000_000, 25_000_000)
    spent = 0

    while spent < budget:
        category = random.choice(list(categories.keys()))
        subcategory = random.choice(list(categories[category].keys()))
        merchant = random.choice(categories[category][subcategory])
        amount = random.randint(10_000, 1_500_000)
        if spent + amount > budget:
            break

        date = datetime(year, mon, random.randint(1, 28))
        transactions.append({
            "id": f"txn_{transaction_id}",
            "amount": amount,
            "currency": "UZS",
            "status": "success" if random.random() > 0.05 else "failed",
            "description": f"Payment to {merchant}",
            "merchant": merchant,
            "subcategory": subcategory,
            "main_category": category,
            "created_at": date.isoformat(),
            "city": "Tashkent",
            "type": random.choice(["P2P_DEBIT", "P2P_CREDIT", "POS", "TRANSFER"]),
            "mcc": str(random.randint(5000, 5999)),
            "card_type": random.choice(["HUMO", "UZCARD", "VISA"]),
        })
        spent += amount
        transaction_id += 1

df = pd.DataFrame(transactions)
df.to_json("/mnt/data/uzbekistan_expenses_dataset.json", orient="records", indent=2, force_ascii=False)
df.head()
