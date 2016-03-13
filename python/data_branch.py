class BranchData:

  def __init__(self,file_name):
    self.data = {}
    f = open(file_name,'r')
    for line in f:
      line = line.strip("\n")
      records = line.split(",")
      user = records[0]
      bank = records[1]
      score = records[2]
      if user not in self.data:
        self.data[user] = {}
      self.data[user][bank] = float(score)
