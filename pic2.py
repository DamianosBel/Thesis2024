import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

connection = "mysql+mysqlconnector://damianos:poot@localhost/sp"

query = "select * from data where date between '2024-04-20' and '2024-06-16'"

data = pd.readsql(query, connection)

print(data['Date'].dtype)

data['Date'] = pd.to_datetime(data['Date'])

print(data['Date'].dtype)

features = data[['Open', 'Close']]

kmeans = KMeans(n_clusters=2)
kmeans.fit(features)

labels = kmeans.labels

centers = kmeans.clustercenters

plt.scatter(features.iloc[:, 0], features.iloc[:, 1], c=labels, cmap='viridis')
plt.scatter(centers[:, 0], centers[:, 1], marker='X', s=200, linewidths=3, color='r')
plt.title('Αποτελέσματα k-means')
plt.xlabel('Open')
plt.ylabel('Close')
plt.show()