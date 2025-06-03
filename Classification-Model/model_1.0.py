import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from pathlib import Path

train_file_path = Path.cwd() / 'train.json'
test_file_path = Path.cwd() / 'test.json'

if not train_file_path.exists():
    raise FileNotFoundError(f"Файл {train_file_path} не найден")
if not test_file_path.exists():
    raise FileNotFoundError(f"Файл {test_file_path} не найден")

train_df = pd.read_json(train_file_path)
test_df = pd.read_json(test_file_path)

required_columns = ['merchant', 'type']
for df, name in [(train_df, 'train'), (test_df, 'test')]:
    if not all(col in df.columns for col in required_columns):
        raise ValueError(f"В датасете {name} отсутствуют необходимые столбцы: {required_columns}")


hierarchy_json = {
    "necessities": ["Housing", "Food", "Transport", "Healthcare", "Clothing", "Education"],
    "wants": ["Entertainment", "Travel", "Hobbies", "Gadgets", "Luxury items"],
    "savings_investments": ["Emergency fund", "Investments", "Retirement funds"],
    "unexpected": ["Repairs", "Medical emergencies", "Gifts", "Fines"],
    "debts": ["Loans", "Payday loans", "Credit card interest"]
}

subcategory_to_main = {}
for main, subs in hierarchy_json.items():
    for sub in subs:
        subcategory_to_main[sub] = main

merchant_to_subcategory = {
    "Makro": "Food",
    "Korzinka": "Food",
    "PharmMarket": "Healthcare",
    "UzGas": "Transport",
    "Apteka Plus": "Healthcare",
    "UZRailways": "Transport",
    "Netflix": "Entertainment",
    "YouTube Premium": "Entertainment",
    "PlayStation Store": "Entertainment",
    "iTunes": "Entertainment",
    "Adidas": "Clothing",
    "Starbucks": "Luxury items",
    "Humo Invest": "Investments",
    "Alif Capital": "Investments",
    "TBC Invest": "Investments",
    "CryptoUz": "Investments",
    "ETF Market": "Investments",
    "Alpha Insurance": "Medical emergencies",
    "Emergency Clinic": "Medical emergencies",
    "CarRepair Tashkent": "Repairs",
    "Legal Help": "Fines",
    "Loan Repayment - Agrobank": "Loans",
    "CreditCard Uz": "Credit card interest",
    "Alif Loan": "Loans",
    "MicroCreditBank": "Loans"
}


train_df['subcategory'] = train_df['merchant'].map(merchant_to_subcategory)
train_df['main_category'] = train_df['subcategory'].map(subcategory_to_main)
test_df['subcategory'] = test_df['merchant'].map(merchant_to_subcategory)
test_df['main_category'] = test_df['subcategory'].map(subcategory_to_main)


train_df = train_df.dropna(subset=['subcategory', 'main_category'])
test_df = test_df.dropna(subset=['subcategory', 'main_category'])

if train_df.empty:
    raise ValueError("Тренировочный датасет пуст после удаления пропусков")
if test_df.empty:
    raise ValueError("Тестовый датасет пуст после удаления пропусков")

test_df = test_df.copy()  
train_df = train_df.copy()


train_df['text'] = train_df['merchant'] + ' ' + train_df['type']
test_df['text'] = test_df['merchant'] + ' ' + test_df['type']

X_train = train_df['text']
y_train = train_df['subcategory']
X_test = test_df['text']
y_test = test_df['subcategory']

vectorizer = TfidfVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

model = LogisticRegression(max_iter=1000)
model.fit(X_train_vec, y_train)

y_pred = model.predict(X_test_vec)
print("Classification Report:")
print(classification_report(y_test, y_pred))

def classify_transaction(merchant: str, txn_type: str):
    text_input = f"{merchant} {txn_type}"
    vector = vectorizer.transform([text_input])
    subcat = model.predict(vector)[0]
    main_cat = subcategory_to_main.get(subcat, "Unknown")  
    return {"subcategory": subcat, "main_category": main_cat}

example = classify_transaction("Apteka", "W")
print("Пример классификации:", example)