import yfinance as yf

apple = yf.Ticker("APPL")

historical_data = apple.history(period="5y")

print(historical_data)
