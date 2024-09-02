import pandas as pd
from sklearn.cluster import AgglomerativeClustering
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage

connection = "mysql+mysqlconnector://damianos:poot@localhost/sp"

query = "select * from data where date between '2024-05-01' and '2024-06-16'"

query = "select * from data where date between '2020-03-06' and '2020-03-15'"

data = pd.read_sql(query, connection)

print(data['Date'].dtype)

data['Date'] = pd.to_datetime(data['Date'])

print(data['Date'].dtype)

target_date = '2024-01-15'

target_date = pd.to_datetime(target_date)

features = data[['Open', 'Close']]

agg_clustering = AgglomerativeClustering(n_clusters=3, linkage='ward')
labels = agg_clustering.fit_predict(features)

plt.scatter(features.iloc[:, 0], features.iloc[:, 1], c=labels, cmap='viridis')
plt.title('Αποτελέσματα Hierarchical Clustering')
plt.xlabel('Open')
plt.ylabel('Close')

linkage_matrix = linkage(features, 'ward')
dendrogram(linkage_matrix, labels=labels)
plt.show()