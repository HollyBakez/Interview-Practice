class Node:
    def __init__(self, data=None):
        self.next = None
        self.data = data

class SLinkedList:
    def __init__(self):
        self.head = None
    '''
    creates a new node by inputting new data
    '''
    def push_newNode(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
'''
No Buffer method 
Time Complexity O(N^2)
O(N * N) where both N is the n-th length of the Linked-List

def remove_duplicate(start = Node()):
    temp = Node()
    temp2 = Node()
    duplicate = Node()
    temp = start

    while temp != None and temp.next != None:
        temp2 = temp
        
        while temp2.next != None:
            if temp.data is temp2.next.data:
                duplicate = temp2.next
                temp2.next = temp2.next.next
                
            else:
                temp2 = temp2.next

        temp = temp.next
'''
#  Utitlizing set built in python
'''
Time Complexity: O(N)

'''

def remove_duplicates(start = Node()):
    if start.next is None:
        return
    curr = Node()
    curr = start
    seen = set([curr.data])
    while curr.next:
        if curr.next.data in seen:
            curr.next = curr.next.next 
        else:
            seen.add(curr.next.data)
            curr = curr.next
    return
    

    

def print_list(node = Node()):

    while node is not None:
        print(node.data)
        node = node.next


node1 = Node(10)
node2 = Node(12)
node3 = Node(5)
node4 = Node(12)
node5 = Node(5)


node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print("Before removing duplicates")
print_list(node1)

print("After removing duplicates")
remove_duplicates(node1)
print_list(node1)


    
        
    