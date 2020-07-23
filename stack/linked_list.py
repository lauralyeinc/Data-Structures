class Node:
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0 

    def add_to_head(self, value):
        #empty linkedlist
        # if self.length == 0:  # if self.head is None and self.tail is None 
        #     new_node = Node(value, self.head)
        #     self.head = new_node
        #     self.tail = new_node
        #     self.length += 1 
        # else: 
        # not empty linkedlist 
        #     new_node = Node(value, self.head)
        #     self.head = new_node
        #     self.length += 1 
        # following dry rule 
        new_node = Node(value, self.head)
        self.head = new_node
        if self.length == 0: 
            self.tail = new_node
        self.length += 1

    def add_to_tail(self, value):
        new_node = Node(value)
        # empty linkedlist
        # if self.length == 0: 
        #     self.head = new_node
        #     self.tail = new_node
        #     self.length += 1 
        # else:
        #     self.tail.set_next(new_node)
        #     self.tail = new_node
        if self.head is None and self.tail is None:
            self.head = new_node
        else:
            self.tail.set_next(new_node)
        self.tail = new_node
        self.length += 1 
    
    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current is not None:
            if current.get_value() == value:
                return True
            
            current = current.get_next()
        
        return False

    def remove_head(self):
        #empty linked list
        if self.head is None:
            return None

        # list with 1 node
        if self.head is self.tail:
            value = self.head.get_value()
            self.head = None
            self.tail = None
            self.length -= 1 
            return value
        # list with two or more nodes
        else:  
            value = self.head.get_value()
            self.head = self.head.get_next()
            self.length -= 1 
            return value 

    def remove_tail(self):
        #empty linked list
        if self.tail is None:
            return None
        
        #list with 1 Node
        elif self.head == self.tail:
            value = self.head.get_value()
            self.tail = None
            self.head = None
            self.length -=1 
            return value 

        current = self.head
        # list with 2 or more nodes. 
        while current.get_next() is not self.tail: 
            current = current.get_next()
        
        value = self.tail.get_value()
        self.tail = current.set_next(None)
        return value 

    def get_max(self):
        if self.head is None:
            return None
        cur_node = self.head
        cur_max = self.head.get_value()
        while cur_node is not None:
            if cur_node.get_value() > cur_max:
                cur_max = cur_node.get_value()
            cur_node = cur_node.get_next()
        
        return cur_max