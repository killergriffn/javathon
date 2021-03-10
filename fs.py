class fs:
  def readFile(path):
    try:
      f = open(path,"r")
      class callback:
        data = f.read()
      return callback.data
    except:
      class callback:
        err = "file or character index does not exist"
      raise Exception(callback.err) 
  def writeFile(path,data):
    try:
      f = open(path,"w")
      class callback:
        err = "data didnt parse.\ndata needs to be a string or integer"
      try:
        f.write(data)
      except:
        raise Exception(callback.err)
    except:
      raise Exception("file ("+path+") doesnt exist")
  def appendFile(path,data):
    try:
      f = open(path,"a")
      class callback:
        err = "data didnt parse.\ndata needs to be a string or integer"
      try:
        f.write(data)
      except:
        raise Exception(callback.err)
    except:
      raise Exception("file ("+path+") doesnt exist")