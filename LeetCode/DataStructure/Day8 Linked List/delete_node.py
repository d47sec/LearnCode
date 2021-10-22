class Node:
    def __init__(self, data) -> None:
        self.data = data 
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
    
    def insertTail(self, data):
        new_Node = Node(data)
        temp = self.head
        if temp == None:
            self.head = new_Node
            return
        while temp.next != None:
            temp = temp.next
        temp.next = new_Node
        new_Node.next = None
    
    # xoá node theo giá trị
    def deleteNode(self, value):
        temp = self.head
        if temp.data == value:
            self.head = temp.next
            temp = None
            return
        while temp.next != None:
            if temp.data == value:
                break
            prev = temp
            temp = temp.next
        # trường hợp này là value ko có ở trong linked list 
        if temp == None:
            return  
        prev.next = temp.next
        temp = None
    # xoá node theo index 
    def deleteNode2(self, index):
        temp = self.head
        if index == 0 and temp != None:
            self.head = temp.next
            temp = None
            return
        while index > 1 and temp.next != None:
            prev = temp
            temp = temp.next
            index -= 1
        prev.next = temp.next
        temp = None

if __name__ == '__main__':
    llist = LinkedList()
    llist.insertTail(1)
    llist.insertTail(2)
    llist.insertTail(3)
    llist.insertTail(4)
    llist.insertTail(5)
    llist.insertTail(6)
    llist.printList()
    print("="*20)
    # llist.deleteNode(4)
    llist.deleteNode2(4)
    llist.printList()

