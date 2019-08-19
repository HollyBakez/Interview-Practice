class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None
    
    def push_back(self, new_data=None):
        new_data = Node(new_data)
        if self.head is None:
            self.head = new_data 
            return
        trav = self.head
        while trav.next:
            trav = trav.next
        trav.next = new_data
        return 
    
    def print_list(self):
        temp = self.head 
        while temp: 
            print(temp.data)
            temp = temp.next

class Solution:
  def addTwoNumbers(self, l1, l2, c = 0):
    temp1 = l1
    temp2 = l2
    new_list = SLinkedList() 
    
    while temp1: 
        temp_value = temp1.data + temp2.data + c 
        if temp_value > 9:
            rem = temp_value - 10 
            c = 1 
            new_list.push_back(rem)
        else:
            c = 0 
            new_list.push_back(temp_value)
        temp1 = temp1.next 
        temp2 = temp2.next
        if temp1 is None and c is not 0:
            new_list.push_back(c)

    return new_list.print_list()

l1 = Node(2)
l1.next = Node(4)
l1.next.next = Node(6)
    
l2 = Node(5)
l2.next = Node(6)
l2.next.next = Node(4)

Solution().addTwoNumbers(l1, l2)


            
