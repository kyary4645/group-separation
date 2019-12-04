from simanneal import Annealer
import random
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns

class GroupingProblem(Annealer):

  def __init__(self, init_state):
    super(GroupingProblem, self).__init__(init_state) # important!

  # 探索点の移動ルール
  def move(self):
    # ランダムに選択したメンバーm1をチームt1からチームt2へ移す
    m1 = random.choice(list(range(nmembers)))
    t1 = self.state[m1].index(1)
    t2 = random.choice(list(range(nteams)))
    self.state[m1][t1], self.state[m1][t2] = self.state[m1][t2], self.state[m1][t1]

  # 目的関数
  def energy(self):
    v = 0
    nu = sum(sum(b[i] * self.state[i][j] for i in range(nmembers)) for j in range(nteams)) / nteams
    for j in range(nteams):
      mu_j = sum(scores[i] * self.state[i][j] for i in range(nmembers))
      v += abs(sum(scores[i] * self.state[i][j] for i in range(nmembers)) - mu_j) + 1.5 * abs(sum(b[i] * self.state[i][j] for i in range(nmembers)) - nu)
    return v

if __name__ == '__main__':
  # データの呼び出し
  xl_df = pd.read_excel('test_data.xlsx')
  df = xl_df.iloc[:, 1:]
  kmeans = KMeans(n_clusters=5)
  xl_df["class"] = kmeans.fit_predict(df)

  teams = [1,2,3,4,5,6,7,8,9,10,11]
  members = xl_df.loc[:,"氏名"].values.tolist()
  skills = ['class']
  scores = xl_df.loc[:,"class"].values.tolist()

  nteams = len(teams)
  nmembers = len(members)
  nskills = len(skills)
  b = [ai for ai in scores]

  # 初期割り当て
  init_state = [[0 for j in range(nteams)] for i in range(nmembers)]
  for i in range(nmembers):
    init_state[i][0] = 1 # 最初は全員1チームに所属
  
  prob = GroupingProblem(init_state)
  prob.steps = 200000
  prob.copy_strategy = "deepcopy"
  prob.anneal() # 焼きなましの実行
  g_df = pd.DataFrame()

  for i,s in enumerate(prob.state):
    g_df.loc[i,0] = teams[s.index(1)]
  
  df_concat = pd.concat([xl_df, g_df], axis=1)
  df_concat_new = df_concat.rename(columns={0: 'team'})
  s_df = df_concat_new.sort_values('team')
  m_df = df_concat_new.groupby('team').mean()
  s_df.to_html('grouping5.html')
  m_df.to_html('average5.html')

  m_df.plot.bar(figsize=(10,8),subplots=True,legend=False)
  plt.savefig('grouping5.png') 
  

