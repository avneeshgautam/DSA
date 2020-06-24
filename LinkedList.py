class Node:
    def __init__(self,item):
        self.item = item
        self.next = None

class LL:
    def __init__(self):
        self.head = None

    def length(self):
        count=0
        temp = self.head
        while(temp!=None):
            count +=1
            temp = temp.next
        return count
    
    def lprint(self):
        temp = self.head
        if(len==0):
            print("List is empty")
        else:
            while(temp!=None):
                print(temp.item,end="->")
                temp=temp.next

    # append this list
    def append(self):
        number = int(input("Enter the value: "))
        temp = Node(number)
        p = self.head
        
        
        while(p!=None):
            p=p.next
        
        
    
llist = LL()
llist.append()

llist.lprint()
print("\nLength: ",llist.length())
