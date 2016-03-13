import sys
import numpy as np
from sklearn import metrics
import random

class UpsellingEvaluator:

  def __init__(self,submission,solution):
    self.submission = submission
    self.solution = solution
    random.seed(19890223)

  def run(self):
    truth = []; pred = []
    truth_public = []; pred_public = []
    for user in self.solution.data:
      tr = int(self.solution.data[user])
      if user in self.submission.data:
        pr = self.solution.data[user]
      else:
        pr = 0
      truth.append(tr)
      pred,append(pr)
      if random.random() < 0.3:
        truth_public.append(tr)
        pred_public.append(pr)
    return ( roc_auc_score(np.array(truth_public),np.array(pred_public)) , roc_auc_score(np.array(truth),np.array(pred)) )

