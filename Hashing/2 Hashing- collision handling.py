


class HashTable:
    def __init__(self):
        self.MAX=10
        self.arr=[[] for i in range(self.MAX)]
    
    def get_hash(self,key):
        h=0
        for i in key:
            h +=ord(i)
        return h % self.MAX

    def __setitem__(self,key,val):
        h=self.get_hash(key)
        found = False
        if((len(self.arr[h]))>1):
            for i,element in enumerate(self.arr[h]):
                if(element[0]==key):
                    found = True
                    self.arr[h][i]=[key,val]       
                    break
        if not found:
            self.arr[h].insert(0,[key,val])


    def __getitem__(self,key):
        h=self.get_hash(key) 
        for element in self.arr[h]:
            if(key==element[0]):
                return element[1]

    def printarr(self):
        for i in self.arr:
            print(i)

t=HashTable()
t['a']=12
t['ad']=23
t['a']=34
t.printarr()
print(t['ad'])




