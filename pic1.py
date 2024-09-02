import pandas as pd
import matplotlib.pyplot as plt

query = "select open from data where date='2020-03-06' ORDER BY rand() limit 20"

query = "select close from data where date='2020-03-06' ORDER BY rand() limit 20"

df_open = pd.DataFrame(open_data)
df_close = pd.DataFrame(close_data)

df_open['Date'] = pd.to_datetime(df_open['Date'])
df_close['Date'] = pd.to_datetime(df_close['Date'])

#Plot the data
plt.figure(figsize=(14, 7))
plt.plot(df_open['Date'], df_open['Open'], marker='o', label='Open')
plt.plot(df_close['Date'], df_close['Close'], marker='x', label='Close')
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Open and Close Prices Over Time')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig('/mnt/data/open_close_prices.png')

import ace_tools as tools; tools.display_dataframe_to_user(name="Open and Close Prices Data", dataframe=df_open.join(df_close.set_index('Date'), on='Date'))

plt.show()