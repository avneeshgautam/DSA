# # # stock_price=[]
# # # with open(r"C:\Users\Jinu\Documents\Study\DSA_py\DSA_python\data.csv","r") as f:
# # #     for line in f:
# # #         tokens = line.split(',')
# # #         day = tokens[0]
# # #         price = float(tokens[1])
# # #         stock_price.append([day,price])

# # # print(stock_price)


# # # for i in stock_price:
# # #     if(i[0]=='Mar-09'):
# # #         print("")
# # #         print(i[1])

# stock_dict={}
# with open(r"C:\Users\Jinu\Documents\Study\DSA_py\DSA_python\stock.csv","r") as f:
#     for line in f:
#         tokens = line.split(',')
#         day = tokens[0]
#         price = float(tokens[1])
#         stock_dict[day]=price

# # print(stock_dict)

# # print("")
# # print(stock_dict['Mar-09'])


# def get_hash(key):
#     h=0
#     for char in key:
#         h +=ord(char)
#     return h % 100


# for i in stock_dict.keys():
#     print(get_hash(i))

################################################

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


