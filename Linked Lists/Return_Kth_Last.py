'''
Return Kth to Last:
Implement an algorithm to find the kth to last element of a singly linked list

Ex) 
Input: linked_list, k = 3
A -> B -> C -> D -> None
Output: B

'''

class Node:
    def __init__(self, data=None):
        self.next = None
        self.data = data



class SLinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_node):
        new_node = Node(new_node)
        new_node.next = self.head
        self.head = new_node

    '''
    key = 3 
    4 -> 3 -> 2 -> 1 
    curr.data = 4
    4 != 3
    curr.next.data = 3 
    curr.data == key 
    '''
    def remove(self, key):
        # set current point to the head of the ll
        curr = self.head
        # Check if the head has our key, then remove the node and point 
        # head to the next node making it the new head
        if curr is not None:
            if curr.data == key:
                self.head = curr.next 
                curr = None
                return 

        # traverse through the list and stops when the current pointer 
        # hits the key 
        while curr is not None:
            if curr.data == key:
                break
            prev = curr
            curr = curr.next 

        # List is empty 
        if curr == None:
            return 

        prev.next = curr.next 
        curr = None

    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next 
    
    def print_head(self):
        curr = self.head
        print(curr.data)
    
    def get_count(self):
        curr = self.head
        count = 0
        while curr:
            curr = curr.next 
            count += 1
        return count

# 4 -> 3 -> 2 -> 1 -> NULL
# if n_element = 2
# output = 2
def find_k_last(some_node = SLinkedList, n_element = int):
    curr = some_node.head
    amt_to_trav = some_node.get_count() - n_element
    count = 0 
    while count is not amt_to_trav:
        curr = curr.next 
        count +=1
    print(curr.data)

some_list = SLinkedList()
some_list.push('A')
some_list.push('B')
some_list.push('C')
some_list.push('D')
some_list.push('E')
some_list.push('F')
# F -> E -> D -> C -> B -> A -> NULL
# output = D
find_k_last(some_list, 4)

# F -> E -> D -> C -> B -> A -> NULL
# output = B
find_k_last(some_list, 1)

