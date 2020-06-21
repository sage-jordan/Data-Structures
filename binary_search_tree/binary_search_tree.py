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
        if self.value == value:
            return True
        elif self.value < vlaue and self.right:
            self.value = self.value.right
            return self.insert(value)
        elif self.value > value and self.left:
            self.value = self.value.left
            return self.insert(value)
        return False

        # if not self.value:
        #     self.value = value
        # if value < self.value:
        #     if not self.left:
        #         self.left = value
        #         return 'value added'
        #     return self.insert(value)
        # if value > self.value:
        #     if not self.right:
        #         self.right = value
        #         return 'value added'
        #     return self.insert(value)
        # if value == self.value:
        #     return 'Cannot add, duplicate item'

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        # when we start searching, slef will be the root
        # compare the target against self
        if target == self.value:
            return True
        if target < self.value:
            if self.left == None:
                return False
            return self.left.contains(target)
        if target > self.value:
            if self.right == None:
                return False
            return self.right.contains(target)

    # Return the maximum value found in the tree

    def get_max(self):
        pass

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        pass

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


tree = BSTNode(9)
print("False: ", tree.contains(8))
# print("True: ", tree.contains(8))
# print("False: ", tree.contains(8))
# print("True: ", tree.contains(8))
# print("False: ", tree.contains(8))
# print("True: ", tree.contains(8))
# print("False: ", tree.contains(8))
# print("True: ", tree.contains(8))
