class Nodes:
    def __init__(self,values):
        self.values = values
        self.next = None

class Stacks:
   def __init__(self,values):
        newnodes = Nodes(values)
        self.front = newnodes
        self.height = 1

   def push(self,values):
       newnodes = Nodes(values)
       if self.height == 0:
           self.front = newnodes
       else:
           newnodes.next = self.front
           self.front = newnodes
       self.height +=1

   def pop(self):
       if self.height == 0:
           return None
       tempo = self.front
       self.front = self.front.next
       tempo.next = None
       self.height =-1
       return tempo

   def printlist(self):
      tempo = self.front
      while tempo is not  None:
            print(tempo.values)
            tempo = tempo.next


printstack = Stacks(10)
printstack.push(20)
printstack.push(30)
printstack.push(40)
printstack.push(50)
printstack.pop()
printstack.printlist()