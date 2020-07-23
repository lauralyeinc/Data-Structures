"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
from linked_list import LinkedList


class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()
        #self.storage = [] #array 
    
    def __len__(self):
        return self.size
        #return len(self.storage)

    def enqueue(self, value):  # add an item of data awaiting processing to a queue of such items 
        self.storage.add_to_tail(value)
        self.size += 1
        #self.storage.append()

    def dequeue(self): # remove an item of data awaiting processing from a quence of such items 
        if self.size != 0:
            self.size -= 1 
            return self.storage.remove_head()
        else:
            return None 

        # head = self.head 
        # if not head:
        #     return None
        # else:
            # self.size -= 1
            # self.head = head.next_node
            # return head.value 

        # if len(self.storage) != 0:
        #     return self.storage.pop()
        # else:
        #     return None 

