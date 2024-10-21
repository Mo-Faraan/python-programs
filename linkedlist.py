class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def addatbeg(self,data):
        newnode = Node(data)
        if self.head==None:
            self.head = newnode
            return
        else:
            newnode.next = self.head
            self.head = newnode
    
    def addatend(self,data):
        newnode  = Node(data)
        if self.head == None:
            self.head = newnode
            return
        else:
            prev = self.head
            while prev.next != None:
                prev = prev.next
            prev.next = newnode

    def printlist(self):
        curr = self.head
        while curr!=None:
            print(curr.data," -> ",end="")
            curr = curr.next
        print("None")

    def deletenode(self,data):
        curr = self.head
        if curr.data == data and curr == self.head :
            self.head = curr.next
            curr = None
            return 
        prev = None
        while curr.data != data and curr != None:
            prev = curr
            curr = curr.next
        if curr == None:
            print("no node found")
            return
        prev.next = curr.next
        curr = None
    
    def searchnode(self,data):
        curr = self.head
        while curr != None:
            if curr.data == data:
                return True
            curr = curr.next
        return False
    
    def insertatindex(self,index,data):
        if index == 0:
            self.addatbeg(data)
        else:
            position = 0
            curr = self.head
            while curr != None and position+1 != index :
                position+=1
                curr = curr.next
            if curr!=None:
                newnode = Node(data)
                prev = curr
                curr = curr.next
                prev.next = newnode
                newnode.next = curr
            else:
                print("no index")

    def updateNode(self, val, index):
        curr = self.head
        position = 0
        if position == index:
            curr.data = val
        else:
            while(curr != None and position != index):
                position = position+1
                curr = curr.next
            if curr != None:
                curr.data = val
            else:
                print("Index not present")
        
    def remfirstnode(self):
        curr=self.head
        if curr == None:
            curr = None
        else:
            self.head = curr.next
            curr = None
        
    def remlastnode(self):
        curr = self.head
        if curr is None:
            return
        if curr.next is None: 
            self.head = None
            return
        while curr.next is not None:
            prev = curr
            curr = curr.next
        prev.next = None
                
    def rematindex(self,index):
        if self.head == None:
            return
        curr = self.head
        position = 0
        while curr!=None and position+1 != index:
            position+=1
            curr = curr.next
        if curr!=None:
            curr.next = curr.next.next
        else:
            print("index not found")

    def remnode(self,data):
        curr = self.head
        if curr.data == data:
            self.remfirstnode()
        else:
            while(curr.next != None and curr.next.data != data):
                curr = curr.next
            if curr.next!=None :
                curr.next = curr.next.next
            else:
                return
        
    def sizeOfLL(self):
        size = 0
        if(self.head):
            current_node = self.head
            while(current_node):
                size = size+1
                current_node = current_node.next
            return size
        else:
            return 0

llist = LinkedList()

llist.addatend('a')
llist.addatend('b')
llist.addatbeg('c')
llist.addatend('d')
llist.insertatindex(2,'g')

print("node data")
llist.printlist()

print("rem 1st node")
llist.remfirstnode()
print("rem last node")
llist.remlastnode()
print("rem node at index 1")
llist.rematindex(1)

llist.printlist()

print("update node value")
llist.updateNode('z',0)
llist.printlist()

print("size")
print(llist.sizeOfLL())








