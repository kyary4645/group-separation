import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

# Excelデータを読み込み、Dataframeにする
xl_df = pd.read_excel('test_data.xlsx')
df = xl_df.iloc[:, 1:]
df.loc["平均"] = df.mean()

xl_df["score"] = float()

for i in range(0,54):
  xl_df.iloc[i,4] = ((df.iloc[i,0] - df.iloc[54,0])**2)+((df.iloc[i,1] - df.iloc[54,1])**2)+((df.iloc[i,2] - df.iloc[54,2])**2)

s_df = xl_df.sort_values("score")
drop_col = ['氏名', 'HTML/CSS', 'Rails', 'JavaScript/jquery', 'score']
d_df = s_df.drop(drop_col, axis=1)
d_df["class"] = float()
for num in range(0,11):
  d_df[num::11] = num + 1

df_concat = pd.concat([s_df, d_df], axis=1)
s_df_concat = df_concat.sort_values('class')
l_df = s_df_concat.reset_index(drop=True)
m_l_df = l_df.groupby('class').mean()
l_df.to_html('grouping3.html')
m_l_df.to_html('average3.html')

m_l_df.plot.bar(figsize=(10,8),subplots=True,legend=False)
plt.show()

