class OrderedStream:

    def __init__(self, n: int):
        self.size=n
        self.arr=[None]*(n+1)
        self.ptr=1

    def insert(self, idKey: int, value: str) -> List[str]:
        ans=[]
        self.arr[idKey]=value
        while self.ptr <=self.size and self.arr[self.ptr] !=None:
            ans.append(self.arr[self.ptr])
            self.ptr +=1
        
        return ans
    
            
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)