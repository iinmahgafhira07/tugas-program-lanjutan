class induk1(object):
   def __init__(self, a):
      self.a = a
   def cetakA(self):
      print("nilai a = ",self.a)
   
class induk2(object):
   def __init__(self, b):
      self.b = b
   def cetakB(self):
     print("nilai b = ",self.b)
     
     
class anak(induk1, induk2):
    def __init__(self, a, b, c):
   
      induk1.__init__(self, a)
      
      induk2.__init__(self,b)
      self.c = c
    def cetakC(self):
      print("nilai c = ", self.c)
def main():

  obj = anak(111, 222, 333)
  
  obj.cetakA()
  
  obj.cetakB()
  
  obj.cetakC()
  
  
if __name__ == "__main__":
  main()
