from simanneal import Annealer
import random
import pandas as pd

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
      mu_j = sum(sum(scores[i][k] * self.state[i][j] for i in range(nmembers)) for k in range(nskills)) / nskills
      for k in range(nskills):
        v += abs(sum(scores[i][k] * self.state[i][j] for i in range(nmembers)) - mu_j)
      v += 1.5 * abs(sum(b[i] * self.state[i][j] for i in range(nmembers)) - nu)
    return v
  

if __name__ == '__main__':
  # データの呼び出し
  xl_df = pd.read_excel('test_data.xlsx')
  df = xl_df.iloc[:, 1:]
  xl_df['total'] = df.sum(axis=1)

  teams = ['A','B','C','D','E','F','G','H','I','J','K']
  members = xl_df.loc[:,"氏名"].values.tolist()
  skills = ['HTML/CSS', 'Rails', 'JavaScript/jquery']
  scores = df.values.tolist()

  nteams = len(teams)
  nmembers = len(members)
  nskills = len(skills)
  b = [sum(ai) for ai in scores]

  # 初期割り当て
  init_state = [[0 for j in range(nteams)] for i in range(nmembers)]
  for i in range(nmembers):
    init_state[i][0] = 1 # 最初は全員Aチームに所属
  
  prob = GroupingProblem(init_state)
  prob.steps = 100000
  prob.copy_strategy = "deepcopy"
  prob.anneal()

  for i,s in enumerate(prob.state):
    print(members[i], teams[s.index(1)])


