class HashTable:
    def __init__(self):
        self.MAX=100
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self,key):
        h=0
        for char in key:
            h +=ord(char)

        return h % self.MAX

    def __setitem__(self,key,val):
        h = self.get_hash(key)
        self.arr[h] = val

    def print_arr(self):
        for i in self.arr:
            print(i,end="\n")

    def __getitem__(self,key):
        h = self.get_hash(key)
        return self.arr[h]

t = HashTable()
# print(t.get_hash('march 6'))
# t.add('march 6',130)
# t.add('march 22',330)
# # t.print_arr()

# t.get('march 22')
t['march 6'] = 11
t['apr 6'] = 12
t['may 6'] = 15
t['jun 6'] = 17
# print(t['may 6'])
print(t['march 6'])
# t.print_arr()


