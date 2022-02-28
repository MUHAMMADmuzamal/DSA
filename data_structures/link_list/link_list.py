"""
Linked List
    A Linked List is a linear collection of data elements, called nodes,
        each pointing to the next node by means of a pointer. It is a
        data structure consisting of a group of nodes which together
        represent a sequence.
    -Singly-linked list: linked list in which each node points to the
        next node and the last node points to null
    -Doubly-linked list: linked list in which each node has two pointers,
        p and n, such that p points to the previous node and n points to
        the next node; the last node's n pointer points to null
    -Circular-linked list: linked list in which each node points to the
        next node and the last node points back to the first node
    Time Complexity:
        -Access: O(n)
        -Search: O(n)
        -Insert: O(1)
        -Remove: O(1)
"""


class SinglyLinkedListNode:
    """Method that creates a node"""

    def __init__(self, data: any = None, next_node: object = None) -> None:
        self.data = data
        self.next = next_node


class SinglyLinkedList:
    """Methods that perform various operations on
        Linked List using Node class"""

    def __init__(self) -> None:
        self.head = None

    def is_empty(self) -> bool:
        """Check if the list is empty"""
        return self.head is None

    def add_first(self, data: any) -> None:
        """Add an item to the beginning of the list"""
        new_node = SinglyLinkedListNode(data, self.head)
        self.head = new_node

    def add_last(self, data: any) -> None:
        """Add an item to the end of the list"""
        new_node = SinglyLinkedListNode(data)
        if not self.is_empty():
            cur_node = self.head
            while cur_node.next:
                cur_node = cur_node.next
            cur_node.next = new_node
        else:
            self.head = new_node
    
    def add_in_between(self, data: any, prev_node: object, next_node: object) -> None:
        """Add an item to the middle of the list"""
        new_node = SinglyLinkedListNode(data, next_node)
        prev_node.next = new_node

    def remove_first(self) -> any:
        """Remove and return the first element of the list"""
        if self.is_empty():
            return None
        data = self.head.data
        self.head = self.head.next
        return data

    def remove_last(self) -> any:
        """Remove and return the last element of the list"""
        if self.is_empty():
            return None
        cur = self.head
        data = None
        while cur.next.next:
            cur = cur.next
        data = cur.next.data
        cur.next = None
        return data 
    
    def remove_in_between(self, prev_node: object, next_node: object) -> any:
        """Remove and return the middle element of the list"""
        if self.is_empty():
            return None
        prev_node.next = next_node
    
    def reverse(self) -> None:
        """Reverses the list"""
        if self.is_empty():
             return None
        cur  = self.head
        prev = None
        while cur:
            next = cur.next
            cur.next = prev
            prev, cur = cur, next
        self.head = prev
    
    def print_list(self) -> None:
        """Print the list"""
        if self.is_empty():
            print("None")
        else:
            cur = self.head
            while cur:
                print(cur.data,' -> ' if cur.next else ' -> None', end='')
                cur = cur.next
            print()


class SinglyCircularLinkList(SinglyLinkedList):
    """Methods that perform various operations on
        Circular Linked List using Node class"""

    def add_first(self, data: any) -> None:
        """Add an item to the beginning of the list"""
        if self.is_empty():
            new_node = SinglyLinkedListNode(data)
            self.head = new_node
            new_node.next = self.head
        else:
            new_node = SinglyLinkedListNode(self.head.data, self.head.next)
            self.head.data = data
            self.head.next = new_node

    def add_last(self, data: any) -> None:
        """Add an item to the end of the list"""
        new_node = SinglyLinkedListNode(data, self.head)
        if not self.is_empty():
            cur_node = self.head
            while True:
                if self.head == cur_node.next:
                    break
                cur_node = cur_node.next
            cur_node.next = new_node
        else:
            self.head = new_node
            new_node.next = self.head

    def remove_first(self) -> any:
        """Remove and return the first element of the list"""
        if self.is_empty():
            return None
        data = self.head.data
        self.head.data, self.head.next = self.head.next.data, self.head.next.next
        return data
    
    def remove_last(self) -> any:
        """Remove and return the last element of the list"""
        if self.is_empty():
            return None
        cur_node = self.head
        data  = None
        while True:
            if self.head == cur_node.next.next:
                break
            cur_node = cur_node.next
        data = cur_node.next.data
        cur_node.next = self.head
        return data
    
    def reverse(self) -> None:
        """Reverses the list"""
        if self.is_empty():
             return None
        cur  = self.head
        prev = None
        while True:
            if self.head == cur.next:
                break
            next = cur.next
            cur.next = prev
            prev, cur = cur, next
        next = cur.next
        cur.next = prev
        prev, cur = cur, next
        cur.next = prev
        self.head = prev

    def print_list(self) -> None:
        """Print the list"""
        if self.is_empty():
            print("None")
        else:
            cur = self.head
            while True:
                print(cur.data,' -> ' if cur.next != self.head else ' -> None', end='')
                cur = cur.next
                if self.head == cur: # if use this logic then While True
                    break
                
            print()


class DoublyLinkedListNode:
    """Method that creates a node"""

    def __init__(self, data: any = None, prev_node: object = None, next_node: object = None) -> None:
        self.data =  data
        self.prev = prev_node
        self.next = next_node


class DoublyLinkedList:
    """Methods that perform various operations on
        Doubly Linked List using Node class"""

    def __init__(self) -> None:
        self.head = None
    
    def is_empty(self) -> bool:
        """Check if the list is empty"""
        return self.head is None
    
    def add_first(self, data: any) -> None:
        """Add an item to the beginning of the list"""
        if self.is_empty():
            new_node = DoublyLinkedListNode(data, None, None)
            self.head = new_node
        else:
            new_node = DoublyLinkedListNode(data, None, self.head)
            self.head.prev = new_node
            self.head = new_node
    
    def add_last(self, data: any) -> None:
        """Add an item to the end of the list"""
        new_node = DoublyLinkedListNode(data, next_node=None)
        if not self.is_empty():
            cur_node = self.head
            while cur_node.next:
                cur_node = cur_node.next
            new_node.prev = cur_node
            cur_node.next = new_node
        else:
            new_node.prev = None
            self.head = new_node

    def add_in_between(self, data: any, prev_node: object, next_node: object) -> None:
        """Add an item to the middle of the list"""
        new_node = DoublyLinkedListNode(data, prev_node, next_node)
        prev_node.next = new_node
        next_node.prev = new_node
    
    def remove_first(self) -> any:
        """Remove and return the first element of the list"""
        if self.is_empty():
            return None
        data = self.head.data
        self.head = self.head.next
        self.head.prev = None
        return data
    
    def remove_last(self) -> any:
        """Remove and return the last element of the list"""
        if self.is_empty():
            return None
        cur = self.head
        data = None
        while cur.next.next:
            cur = cur.next
        data = cur.next.data
        cur.next = None
        return data 

    def remove_in_between(self, prev_node: object, next_node: object) -> any:
        """Remove and return the middle element of the list"""
        if self.is_empty():
            return None
        next_node.prev = prev_node
        prev_node.next = next_node

    def reverse(self) -> None:
        """Reverses the list"""
        if self.is_empty():
             return None
        cur  = self.head
        new_head = None
        while cur:
            next = cur.next
            new_head = cur.prev
            cur.next, cur.prev = cur.prev, cur.next
            cur = next
        if new_head is not None:
            self.head = new_head.prev

    def print_list(self) -> None:
        """Print the list"""
        if self.is_empty():
            print("None")
        else:
            cur = self.head
            prev = cur
            while cur:
                print(cur.data,' -> ' if cur.next else ' -> None', end='')
                cur = cur.next
                if cur is not None:
                    prev = cur
            print("\nReverse Order Print")
            cur = prev
            while cur:
                print(cur.data,' -> ' if cur.prev else ' -> None', end='')
                cur = cur.prev
            print()
        

class DoublyCircularLinkList(DoublyLinkedList):
    """Methods that perform various operations on
        Doubly Circular Linked List using Node class"""

    def add_first(self, data: any) -> None:
        """Add an item to the beginning of the list"""
        if self.is_empty():
            new_node = DoublyLinkedListNode(data)
            self.head = new_node
            self.head.next = self.head
            self.head.prev = self.head
        else:
            new_node = DoublyLinkedListNode(data, self.head.prev, self.head)
            self.head.prev.next = new_node
            self.head.prev = new_node            
            self.head = new_node

    def add_last(self, data: any) -> None:
        """Add an item to the end of the list"""
        new_node = DoublyLinkedListNode(data)
        if not self.is_empty():
            cur_node = self.head
            while True:
                if self.head == cur_node.next:
                    break
                cur_node = cur_node.next
            cur_node.next = new_node
            new_node.next = self.head
            new_node.prev = cur_node
            self.head.prev = new_node
        else:
            self.head = new_node
            new_node.next = self.head
            new_node.prev = self.head

    def remove_first(self) -> any:
        """Remove and return the first element of the list"""
        if self.is_empty():
            return None
        data = self.head.data
        last = self.head.prev
        self.head.prev.next = self.head.next
        self.head = self.head.next
        self.head.prev = last
        return data
    
    def remove_last(self) -> any:
        """Remove and return the last element of the list"""
        if self.is_empty():
            return None
        cur_node = self.head
        data  = None
        while True:
            if self.head == cur_node.next.next:
                break
            cur_node = cur_node.next
        data = cur_node.next.data
        cur_node.next = self.head
        self.head.prev = cur_node
        return data

    def reverse(self) -> None:
        """Reverses the list"""
        if self.is_empty():
             return None
        cur = self.head
        last = self.head
        while True:
            temp =  cur.next
            cur.next = cur.prev
            cur.prev = temp
            cur = temp
            if cur ==  last:
                break
        self.head = last.next
        

        

    def print_list(self) -> None:
        """Print the list"""
        if self.is_empty():
            print("None")
        else:
            cur = self.head
            while True:
                print(cur.data,' -> ' if cur.next != self.head else ' -> None', end='')
                cur = cur.next
                if self.head == cur: # if use this logic then While True
                    break
                
            print()

    def print_list_reverse(self) -> None:
        """Print the list"""
        if self.is_empty():
            print("None")
        else:
            cur = self.head
            while True:
                print(cur.data,' -> ' if cur.prev != self.head else ' -> None', end='')
                cur = cur.prev
                if self.head == cur: # if use this logic then While True
                    break
            print()
        
if __name__ == '__main__':
    # ll = SinglyLinkedList()
    # ll = SinglyCircularLinkList()
    # ll = DoublyLinkedList()
    ll = DoublyCircularLinkList()
    for i in range(10):
        ll.add_first(i)
    ll.print_list()
    for i in range(11,21):
        ll.add_last(i)
    ll.print_list()      
    ll.add_in_between(1000,ll.head,ll.head.next)
    ll.print_list()
    ll.remove_in_between(ll.head,ll.head.next.next)
    ll.print_list()
    print(ll.remove_first())
    ll.print_list()
    print(ll.remove_last())
    ll.print_list()
    ll.reverse()
    ll.print_list()
    if type(ll) is DoublyCircularLinkList:
        ll.print_list_reverse()