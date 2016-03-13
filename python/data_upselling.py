class UpsellingData:

  def __init__(self,file_name):
    self.data = {}
    f = open(file_name,'r')
    for line in f:
      line = line.strip("\n")
      records = line.split(",")
      self.data[records[0]] = float(records[1])




