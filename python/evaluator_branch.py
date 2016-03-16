import sys
import math
import numpy as np
from sklearn import metrics
import random
import operator

class BranchEvaluator:

  def __init__(self,submission,solution):
    self.submission = submission
    self.solution = solution
    random.seed(19890223)
    #the actual seed is not public)

  def run(self):
    sum_public = 0; num_public = 0
    sum = 0; num = 0
    for user in self.solution.data:
      if len(self.solution.data[user]) > 0:
        score = self.score(user)
        sum+=score; num+=1
        if random.random() < 0.3:
          sum_public+=score; num_public+=1
    return (sum_public/float(num_public), sum/float(num))

  def score(self,user):
    if user in self.submission.data:
      user_solution = self.solution.data[user]
      user_submission = self.submission.data[user] 
      if len(user_submission) > 0:
        cosine_5 = self.cosine(user_submission,user_solution,5)
        cosine_1 = self.cosine(user_submission,user_solution,1)
        return (cosine_5 + cosine_1) * 0.5
      else:
        return 0
    else:
      return 0


  def cosine(self,submission,solution,K):
    sum = 0
    submission_subset = self.create_subset(submission,K)
    norm = self.norm(submission_subset)
    if norm > 0:
      for branch in submission_subset:
        if branch in solution:
          sum += submission_subset[branch] * solution[branch]
      return sum / float(norm) / float(self.norm(solution))
    else:
      return 0

  def create_subset(self,submission,K):
    if len(submission) <= K:
      return submission
    else:
      sorted_submission = sorted(submission.items(), key=operator.itemgetter(1),reverse=True)
      submission_subset = {}
      for i in range(K):
        submission_subset[sorted_submission[i][0]] = sorted_submission[i][1]
      return submission_subset

  def norm(self,data):
    norm = 0
    for i in data:
      norm += data[i]*data[i]
    return math.pow(norm,0.5)

