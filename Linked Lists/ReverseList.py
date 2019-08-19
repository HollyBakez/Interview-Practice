class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None

    def push_back(self, data):
        data = Node(data)
        cur = self.head
        '''
        if list is currently empty set new val as head
        '''
        if self.head is None:
            self.head = data
        else:
            while cur.next is not None:
                cur = cur.next
            cur.next = data
    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next

    def reverse(self):
        prev = None
        cur = self.head
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        self.head = prev


test_list = SLinkedList()
test_list.push_back(1)
test_list.push_back(2)
test_list.push_back(3)
test_list.push_back(4)
print("Before reverse... ")
test_list.print_list()

print("After reverse... ")
test_list.reverse()
test_list.print_list()
