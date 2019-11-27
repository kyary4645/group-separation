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

kmeans = KMeans(n_clusters=3)
xl_df["class"] = kmeans.fit_predict(df)
s_df = xl_df.sort_values("class")
m_df = xl_df.groupby("class").mean()

m_df.plot.bar(figsize=(10,8))

c1_df = xl_df[xl_df["class"].isin([0])]
c2_df = xl_df[xl_df["class"].isin([1])]
c3_df = xl_df[xl_df["class"].isin([2])]


print(c1_df)
print(c2_df)
print(c3_df)

sns.set_style("darkgrid")

fig = plt.figure()
ax = Axes3D(fig)
ax.set_xlabel("HTML/CSS")
ax.set_ylabel("Rails")
ax.set_zlabel("JavaScript/jquery")

ax.plot(c1_df["HTML/CSS"],c1_df["Rails"],c1_df["JavaScript/jquery"],marker="o", linestyle="None", c="red")
ax.plot(c2_df["HTML/CSS"],c2_df["Rails"],c2_df["JavaScript/jquery"],marker="o", linestyle="None", c="blue")
ax.plot(c3_df["HTML/CSS"],c3_df["Rails"],c3_df["JavaScript/jquery"],marker="o", linestyle="None", c="green")
plt.show()