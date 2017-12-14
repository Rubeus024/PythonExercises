import re
class V:
  counter=0
  
  def __init__(self,x):
    self.x=x
  #niejawnie odwołujemy się do klasy
  @classmethod
  def add(cls):
    cls.counter+=1


obj1=V(3)
for i in range(1,5):
  obj1.add() 
  print(V.counter)
  
  # Przykładowy regular Expression
  x1='676-435-3577'
  pattern = re.compile(r'^(\d{3})-(\d{3})-(\d{4})$')
  print(pattern.search(x1).groups())
