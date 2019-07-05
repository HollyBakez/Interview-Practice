class Node:
    def __init__(self, data = None):
        self.next = None 
        self.data = data

class SLinkedList: 
    def __init__(self):
        self.head = None 
    
    def push(self, new_node = None):
        new_node = Node(new_node)
        new_node.next = self.head 
        self.head = new_node
        return new_node

    def append(self, new_node = None):
        new_node = Node(new_node)
        if self.head is None:
            self.head = new_node
            return 
        last = self.head
        while last.next:
            last = last.next

        last.next = new_node
        return new_node
    def print_list(self):
        curr = self.head 
        while curr:
            print(curr.data)
            curr = curr.next
    
    
def delete_middle(mid_node = Node()):
    if mid_node.next is not None:
        mid_node.data = mid_node.next.data
        mid_node.next = mid_node.next.next
    else:
        print("This is the last node")

        
        


link_list = SLinkedList()
link_list.push(1)
link_list.push(2)
link_list.push(3)
link_list.push(12)
middle_node = link_list.push(111)
link_list.push(14)
link_list.push(20)
print("printing list: ")
link_list.print_list()


print("After deletion: ")
delete_middle(middle_node)
link_list.print_list()