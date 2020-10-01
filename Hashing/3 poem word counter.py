d={}
with open(r"C:\Users\Jinu\Documents\Study\DSA_py\DSA_python\1.Hashing\Exercise\poem.txt","r") as f:
    for i in f:
        for j in i.split():
            if(j not in d):
                d[j] = 1
            else:
                d[j] +=1

for i,j in d.items():
    print(i,"\t ",j)
# with open(r"C:\Users\Jinu\Documents\Study\DSA_py\DSA_python\1.Hashing\Exercise\poemmmm.csv","a") as f2:
#     for i in f2:
#         print(i)