import yfinance as yf
import pandas as pd

# Διάβασε τα σύμβολα από το CSV αρχείο
file_path = r'c:\\Users\\Damianos\\Desktop\\Διπλωματική\\olesoimetoxes.csv'  # Αντικαταστήστε αυτό με το πραγματικό path
symbols_df = pd.read_csv(file_path)

# Ανακτήστε τα ιστορικά δεδομένα για κάθε σύμβολο
for symbol in symbols_df['Symbol']:
    # Ανακτήστε τα δεδομένα από το Yahoo Finance
    data = yf.download(symbol, period='5y', interval='1d')

    # Αποθηκεύστε τα δεδομένα σε ένα αρχείο CSV
    data.to_csv(f'{symbol}_historical5y_data.csv')

    print(f'Τα δεδομένα αποθηκεύτηκαν στο αρχείο {symbol}_historical5y_data.csv')
