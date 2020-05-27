import sys

sys.path.append('../doubly_linked_list')

from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """

    def __init__(self, limit=10):
        self.max_nodes = limit
        self.current_nodes = 0

        self.dll = DoublyLinkedList()
        self.dict = {}
    

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """

    def get(self, key):
        # return None if key-value pair doesn't exist in cache
        if key not in self.dict:
            return None
        # if exists iterate over dll
        node = self.dll.head
        while node is not None:
            if key == node.value[0]:
                self.dll.move_to_front(node)
                break
            node = node.next

        # return Value
        return self.dict[key]

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.


    self.dll.head = (key, value) Tuple
    self.dll.head = {key: value} Dict
    self.dll.head = [key, value] List
    """

    def set(self, key, value):
        # if key is already stored, overwrite old value
        if key in self.dict:
            # overwrite in dictionary
            self.dict[key] = value
            # overwrite in DLL
            ## iterate accross and find node to be updated
            node = self.dll.head
            while node is not None:
                # check key equality
                if node.value[0] == key:
                    # and update the value
                    node.value[1] = value
                    # move to head of dll
                    self.dll.move_to_front(node)

                    break

                node = node.next

        else :

            # handle case where we are full
            if self.current_nodes == self.max_nodes:
                #delete something
                
                node = self.dll.tail
                old_key = node.value[0]
                self.dll.remove_from_tail()
                del self.dict[old_key]
                # self.dict.pop(old_key)  <-- This will work and will return the value 
                self.current_nodes -= 1


            # add to cashe
            self.dict[key] = value
            self.dll.add_to_head([key, value])
            self.current_nodes += 1



