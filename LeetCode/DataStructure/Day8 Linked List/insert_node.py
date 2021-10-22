class Node:
    def __init__(self, data) -> None:
        self.data = data 
        self.next = None
    
    
class LinkedList:
    def __init__(self) -> None:
        self.head = None
        
    def printLinkedList(self):
        temp = self.head 
        while temp != None:
            print(temp.data)
            temp = temp.next
                
    def insertHead(self, data):
        new_Node = Node(data)
        new_Node.next = self.head
        self.head = new_Node
    
    def insertIndex(self, data, index):
        k = 1
        new_Node = Node(data)
        prev = self.head
        while k < index and prev.next:
            prev = prev.next
            k +=1
        new_Node.next = prev.next
        prev.next = new_Node
        
    def insertTail(self, data):
        
        new_Node = Node(data)
        if self.head == None:
            self.head = new_Node
            return 
        
        last = self.head
        while last.next:
            last = last.next        
        last.next = new_Node
        new_Node.next = None
        
            

if __name__ == "__main__":
    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    llist.head.next = second 
    second.next = third
    llist.printLinkedList()
    print("=========================")
    llist.insertHead(4)
    llist.printLinkedList()
    print("=========================")
    llist.insertTail(10)
    llist.printLinkedList()
    print("=========================")
    llist.insertIndex(100,2)
    llist.printLinkedList()