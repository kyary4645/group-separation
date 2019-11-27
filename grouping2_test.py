import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns

# Excelデータを読み込み、Dataframeにする
xl_df = pd.read_excel('test_data.xlsx')
df = xl_df.iloc[:, 1:]

sns.set_style("darkgrid")

fig = plt.figure()
ax = Axes3D(fig)
ax.set_xlabel("HTML/CSS")
ax.set_ylabel("Rails")
ax.set_zlabel("JavaScript/jquery")

ax.plot(df["HTML/CSS"],df["Rails"],df["JavaScript/jquery"],marker="o", linestyle="None")

sse = np.zeros(10)
se = np.zeros(10)
inertia = np.zeros(10)

for i in range(10):
  cluster_num = i + 1
  kmeans = KMeans(n_clusters=cluster_num)
  # 各データがどのクラスタに所属するか
  pred = kmeans.fit_predict(df)
  inertia[i] = kmeans.inertia_

  # 各データが自身の所属するクラスタ中心からどれだけ離れているか調べる
  transforms = kmeans.transform(df)
  distances = np.zeros((df.shape[0]))
  for index in range(len(transforms)):
    distances[index] = transforms[index,pred[index]]

  se[i] = np.sum(distances)
  sse[i] = np.sum(distances**2)

kmeans_df = pd.DataFrame({'se':se, 'sse':sse, 'inertia':inertia})
kmeans_df.plot(figsize=(10,8))
plt.show()
