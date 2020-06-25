# import only system from os 
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
        if(self.head==None):
            self.head=temp
        else:
            while(p.next!=None):
                p=p.next
            p.next=temp 
        
    def atBeg(self):
        number=int(input("Enter the value: "))
        temp=Node(number)
        if(len==0):
            self.head==temp
        else:
            temp.next=self.head
            self.head=temp


    def addpos(self):
        pos=int(input("Enter position"))
        num = int(input("Enter NUmber: "))
        temp = Node(num)
        len=self.length()
        p=self.head
        if(pos>len):
            print("Invalid position",pos)
        elif(pos==0):
            temp.next=self.head
            self.head=temp
        else:
            i=1
            while(i<pos):
                p=p.next
                i += 1
            temp.next=p.next
            p.next=temp

            
    def deletepos(self):
        len=self.length()
        pos=int(input("Enter the pos" ))
        p=self.head
        if(pos>=len):
            print("Not found")
        elif(len==0):
            print("List is empty")
        elif(pos==0):
            self.head=p.next
        else:
            i=1
            while(i<pos):
                p =p.next
                i +=1
            q=p.next
            p.next=q.next
    def deletebeg(self):
        p=self.head
        len=self.length()
        p=self.head
        if(len==0):
            print("List is empty")
        else:
            self.head=p.next

    def deletelast(self):
        p=self.head
        i=1
        len=self.length()
        for i in range(1,len-1):
            p=p.next
        q=p.next
        p.next=q.next
        print("Deleted: ",q.item)
        
        
llist = LL()

while(1):
    print("\n--------------------------")
    print("1-Append\n2-Print\n3-Length\n4-Add At begin\n5-Add at Pos\n6-Delete pos\n7-DElete beg\n8-delete last\n9-Exit")
    print("---------------------------\n")
    ch = int(input("Enter your choice: "))

    if ch==1:
        llist.append()
    elif ch==2:
        llist.lprint()
    elif ch==3:
        len=llist.length()
        if(len==0):
            print("List is empty\n")
        else:
            print("\nLength is: ",llist.length())
    elif ch==4:
        llist.atBeg()
    elif ch==5:
        llist.addpos()
    elif ch==6:
        llist.deletepos()
    elif ch==7:
        llist.deletebeg()
    elif ch==8:
        llist.deletelast()
    
    else:
        quit()




        
