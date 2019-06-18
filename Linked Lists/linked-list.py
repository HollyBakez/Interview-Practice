class Node:
    def __init__(self, data=None):
        self.next = None
        self.data = data 

class SlinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def delete_node(self, key):

        temp = self.head

        if temp is not None:
            if temp.data == key:
                self.head == temp.next 
                temp = None 
                return 
        
        while temp is not None:
            if temp.data == key:
                break
            prev = temp 
            temp = temp.next
        
        if temp == None:
            return 
        
        prev.next = temp.next

        temp = None 

    def printlist(self):
        printval = self.head
        while printval:
            print(printval.data)
            printval = printval.next
            
list1 = SlinkedList()
list1.push("Holland")
list1.push("Jasmine")
list1.push(1)
list1.push(2)
print("Before deletion: ")
list1.printlist()

list1.delete_node(1)
list1.delete_node(2)
print("\nAfter deletion: ")
list1.printlist()