"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            # left is less
            if self.left is None:
                self.left = BSTNode(value)  # or is it value replacing it?
            else:
                self.left.insert(value)

        if value >= self.value:
            if self.right is None: 
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

        # understand/plan  
        #start at root and loop until cur_node is None
            #if value == cur_node
                #if cur_node.left is None
                    #insert our value 
                #else
                    #go left (update cur_node to be cur_node.left)
                # elif value > cur_node
                    # if cur_node.right is None
                        # insert value
                    # else
                        # go right (update cur_node to be cur_node.right)
        #pass


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # if found on first try
        if self.value == target:
            return True 
        # if not go left until it's found or not there 
        if target < self.value:
            if self.left is None:
                return False
            else:
                found = self.left.contains(target)
                return found 
        # then go right to find it it or return false if not there.
        if target > self.value:
            if self.right is None:
                return False
            else:
                found = self.right.contains(target)
                return found 

        #understand/plan
        # compare target_value to cur_value
            # 1 == return True
            # 2 < we go left
            # 3 > go right
            # 4 if can't go left/right (not found, return False)
        #pass


    # Return the maximum value found in the tree
    def get_max(self):
        # if tree has no right side 
        if self.right is None:
            # return "parent"
            return self.value
        # else keep going to the right to get the max.
        return self.right.get_max()

        #understand/plan 
        # go right until you can't go right anymore
        #pass


    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value) # need the "info" or value of the function to call it on each node.

        if self.left:
            self.left.for_each(fn)
        
        if self.right:
            self.right.for_each(fn)

        # understand/plan 
            # call fn using value for each node
            # in a tree it will have left and right sides, assuming it's not empty, check "each" side (left/right) for each item using the fn function. Would like to see this function as it's self and not just calling it. 
        #pass

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    # def in_order_print(self):
    #     pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    # def bft_print(self):
    #     pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    # def dft_print(self):
    #     pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    # def pre_order_dft(self):
    #     pass

    # # Print Post-order recursive DFT
    # def post_order_dft(self):
    #     pass

# """
# This code is necessary for testing the `print` methods
# """
# bst = BSTNode(1)

# bst.insert(8)
# bst.insert(5)
# bst.insert(7)
# bst.insert(6)
# bst.insert(3)
# bst.insert(4)
# bst.insert(2)

# bst.bft_print()
# bst.dft_print()

# print("elegant methods")
# print("pre order")
# bst.pre_order_dft()
# print("in order")
# bst.in_order_dft()
# print("post order")
# bst.post_order_dft()  
