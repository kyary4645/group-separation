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

kmeans = KMeans(n_clusters=2)
xl_df["class"] = kmeans.fit_predict(df)

s_df = xl_df.sort_values("class")
m_df = xl_df.groupby("class").mean()
c_mean = xl_df["class"].mean()
# print(c_mean)



# r_df1 = xl_df.sample(n=5)
# g_mean1 = r_df1["class"].mean()
# index1 = r_df1.index.values
# d_df1 = xl_df.drop(index1)

# r_df2 = d_df1.sample(n=5)
# g_mean2 = r_df2["class"].mean()
# index2 = r_df2.index.values
# d_df2 = d_df1.drop(index2)

# r_df3 = d_df2.sample(n=5)
# g_mean3 = r_df3["class"].mean()
# index3 = r_df3.index.values
# d_df3 = d_df2.drop(index3)

# r_df4 = d_df3.sample(n=5)
# g_mean4 = r_df4["class"].mean()
# index4 = r_df4.index.values
# d_df4 = d_df3.drop(index4)

# r_df5 = d_df4.sample(n=5)
# g_mean5 = r_df5["class"].mean()
# index5 = r_df5.index.values
# d_df5 = d_df4.drop(index5)

# r_df6 = d_df5.sample(n=5)
# g_mean6 = r_df6["class"].mean()
# index6 = r_df6.index.values
# d_df6 = d_df5.drop(index6)

# r_df7 = d_df6.sample(n=5)
# g_mean7 = r_df7["class"].mean()
# index7 = r_df7.index.values
# d_df7 = d_df6.drop(index7)

# r_df8 = d_df7.sample(n=5)
# g_mean8 = r_df8["class"].mean()
# index8 = r_df8.index.values
# d_df8 = d_df7.drop(index8)

# r_df9 = d_df8.sample(n=5)
# g_mean9 = r_df9["class"].mean()
# index9 = r_df9.index.values
# d_df9 = d_df8.drop(index9)

# r_df10 = d_df9.sample(n=5)
# g_mean10 = r_df10["class"].mean()
# index10 = r_df10.index.values
# d_df10 = d_df9.drop(index10)

# r_df11 = d_df10.sample(n=4)
# g_mean11 = r_df11["class"].mean()
# index11 = r_df11.index.values
# d_df11 = d_df10.drop(index11)

# print(r_df1)
# print(d_df1)
# print(r_df2)
# print(d_df2)
# print(r_df3)
# print(d_df3)
# print(r_df4)
# print(d_df4)
# print(r_df5)
# print(d_df5)
# print(r_df6)
# print(d_df6)
# print(r_df7)
# print(d_df7)
# print(r_df8)
# print(d_df8)
# print(r_df9)
# print(d_df9)
# print(r_df10)
# print(d_df10)
# print(r_df11)
# print(d_df11)

# # if ((int(c_mean) - 0.12) <= int(g_mean) <= (int(c_mean) + 0.1)):
# #   print(xl_df)


m_df.plot.bar(figsize=(10,8))

c1_df = xl_df[xl_df["class"].isin([0])]
c2_df = xl_df[xl_df["class"].isin([1])]

sns.set_style("darkgrid")

fig = plt.figure()
ax = Axes3D(fig)
ax.set_xlabel("HTML/CSS")
ax.set_ylabel("Rails")
ax.set_zlabel("JavaScript/jquery")

ax.plot(c1_df["HTML/CSS"],c1_df["Rails"],c1_df["JavaScript/jquery"],marker="o", linestyle="None", c="red")
ax.plot(c2_df["HTML/CSS"],c2_df["Rails"],c2_df["JavaScript/jquery"],marker="o", linestyle="None", c="blue")
plt.show()