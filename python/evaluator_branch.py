import sys
import numpy as np
from sklearn import metrics
import random

class BranchEvaluator:

  def __init__(self,submission,solution):
    self.submission = submission
    self.solution = solution
    random.seed(19890223)


  def run(self):
    for user in self.solution.data:
      self.score(user)

  def score(self,user):
    user_solution = self.solution.data[user]
    user_submission = self.submission.data[user]

  def cosine_at_K(self,submission,solution)


