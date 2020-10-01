=#################### using Array##################33

arr=[]
with open(r"C:\Users\Jinu\Documents\Study\DSA_py\DSA_python\1.Hashing\Exercise\1 weather.csv","r") as f:
    for line in f:
        tokens = line.strip().split(',')
        # temperature = int(tokens[1])
        arr.append(int(tokens[1]))

print(arr)
print(sum(arr[0:7])/7)
print(max(arr))




