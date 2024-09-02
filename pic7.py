import yfinance as yf

# Κατασκευάζουμε ένα αντικείμενο για την μετοχή APPL
apple = yf.Ticker("APPL")

# Ανάκτηση ιστορικών δεδομένων
historical_data = apple.history(period="5y")

print(historical_data)


