class MinStack:

    def __init__(self):
        self.l=[]
        self.minst=[]
    
               

    def push(self, val: int) -> None:
        self.l.append(val)
        val=min(val,self.minst[-1] if self.minst else val)
        self.minst.append(val)


    def pop(self) -> None:
        self.l.pop()
        self.minst.pop()

    def top(self) -> int:
        return self.l[-1]
        

    def getMin(self) -> int:
        return self.minst[-1]
