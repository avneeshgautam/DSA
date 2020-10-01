# class Hash:
#     def __init__(self):
#         self.MAX = 10
#         self.d=[0]*self.MAX
    
#     def inserting(self,key):
#         h = key % self.MAX
#         for i in range(h,h+10):
#             t = i % self.MAX
#             if(self.d[t] == 0):
#                 self.d[t] = key
#                 break
    
#     def priting(self):
#         for i in range(self.MAX):
#             print(i,self.d[i])


# t = Hash()
# t.inserting(12)
# t.inserting(10)
# t.inserting(15)
# t.inserting(29)
# t.inserting(22)
# t.inserting(25)
# t.inserting(32)
# t.inserting(2)
# t.inserting(42)
# t.inserting(52)
# t.inserting(2)
# t.priting()


class Hash:
    def __init__(self):
        self.MAX=10
        self.d={}
        for i in range(self.MAX):
            self.d[i] = 0
    
    def inserting(self,key):
        h = key % self.MAX
        for i in range(h,h+10):
            j = i%10
            if(self.d[j] == 0):
                self.d[j] = key
                break

    def printing(self):
        for i,j in self.d.items():
            print(i,j)

t = Hash()
t.inserting(12)
t.inserting(33)
t.inserting(22)
t.printing()

