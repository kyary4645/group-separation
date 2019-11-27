import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

# Excelデータを読み込み、Dataframeにする
xl_df = pd.read_excel('test_data.xlsx')
df = xl_df.iloc[:, 1:]

# それぞれの合計点をDataframeに追加
xl_df['total'] = df.sum(axis=1)
s_df = xl_df.sort_values('total', ascending=False) # totalの順番に並び替え

drop_col = ['HTML/CSS', 'Rails', 'JavaScript/jquery', 'total']
d_df = s_df.drop(drop_col, axis=1)
d_df['class'] = float()
pd.options.display.precision = 0
for i in range(0,11):
  d_df[i::11] = i + 1

df_concat = pd.concat([s_df,d_df.iloc[:,1:]], axis=1)
s_df_concat = df_concat.sort_values('class')
l_df = s_df_concat.reset_index(drop=True)
m_l_df = l_df.groupby('class').mean()
l_df.to_html('grouping1.html')
m_l_df.to_html('average1.html')

m_l_df.plot.bar(figsize=(10,8),subplots=True,legend=False)
plt.show()
