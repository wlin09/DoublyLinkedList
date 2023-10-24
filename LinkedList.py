# This project implements a doubly-linked list and includes big-Oh analysis for each function.

class Linked_List:
    
    class __Node:
        
        def __init__(self, val):
            # The big-oh performance is O(1). The time complexity is constant due to
            # the method only involving simple operations and not being dependent
            # on the size of the list.
            self.val = val
            self.next = None
            self.prev = None

    def __init__(self):
        # The big-oh performance is O(1). The time complexity is constant due to
        # the method only involving simple operations and not being dependent
        # on the size of the list.
        self.__head = None
        self.__tail = None
        self.__size = 0

    def __len__(self):
        # The big-oh performance is O(1). The time complexity is constant due to
        # the method only having to return self.__size, which is already being
        # updated throughout the code.
        return self.__size

    def append_element(self, val):
        # The big-oh performance is O(1). The time complexity is constant due to
        # the method not being dependent on the list's size as seen by the lack
        # of loops.
        new_node = self.__Node(val)
        if self.__size == 0:
            self.__head = new_node
            self.__tail = new_node
        else:
            self.__tail.next = new_node
            self.__tail = new_node
        self.__size = self.__size + 1

    def insert_element_at(self, val, index):
        # The big-oh performance is O(n). The time complexity is linear due to
        # the method having to traverse the entire list in its worst-case,
        # which makes it dependent on the size of the list.
        if index < 0:
            raise IndexError
        if index >= self.__size:
            raise IndexError
        if self.__size == 0:
            raise IndexError
        new_node = self.__Node(val)
        if index == 0:
            new_node.next = self.__head
            self.__head = new_node
        else:
            current = self.__head
            for i in range(1, index):
                current = current.next
            new_node.next = current.next
            current.next = new_node
        self.__size = self.__size + 1

    def remove_element_at(self, index):
        # The big-oh performance is O(n). The time complexity is linear due to
        # the method having to traverse the entire list in its worst-case,
        # which makes it dependent on the size of the list.
        if index < 0:
            raise IndexError
        if index >= self.__size:
            raise IndexError
        if index == 0:
            removed_val = self.__head.val
            self.__head = self.__head.next
            if self.__size == 1:
                self.__tail = None
        else:
            current = self.__head
            for i in range(1, index):
                current = current.next
            removed_val = current.next.val
            current.next = current.next.next
            if index == self.__size - 1:
                self.__tail = current
        self.__size = self.__size - 1
        return removed_val

    def get_element_at(self, index):
        # The big-oh performance is O(n). The time complexity is linear due to
        # the method having to traverse the entire list in its worst-case,
        # which makes it dependent on the size of the list.
        if index < 0:
            raise IndexError
        if index >= self.__size:
            raise IndexError
        current = self.__head
        for i in range(index):
            current = current.next
        return current.val

    def rotate_left(self):
        # The big-oh performance is O(1). The time complexity is constant due to
        # the method only having to change the links of neighboring nodes,
        # which makes it not dependent on the size of the list.
        if self.__size >= 2:
            self.__tail.next = self.__head
            self.__head = self.__head.next
            self.__tail.next.next = None
        
    def __str__(self):
        # The big-oh performance is O(n). The time complexity is linear due to
        # the method having to traverse the entire list, which makes it
        # dependent on the size of the list.
        current = self.__head
        if current is None:
            return '[ ]'
        string = []
        while current is not None:
            string.append(str(current.val))
            current = current.next
        return "[ " + ", ".join(string) + " ]"

    def __iter__(self):
        # The big-oh performance is O(1). The time complexity is constant due to
        # the method only having simply assignments, which makes it not
        # dependent on the size of the list.
        self.current_iter = self.__head
        return self

    def __next__(self):
        # The big-oh performance is O(1). The time complexity is constant due to
        # the method only having to update the iterator and returning the
        # curent value, which makes it not dependent on the size of the list.
        if self.current_iter is None:
            raise StopIteration
        val = self.current_iter.val
        self.current_iter = self.current_iter.next
        return val

    def __reversed__(self):
        # The big-oh performance is O(n). The time complexity is linear due to
        # the method having to traverse the entire list, which makes it
        # dependent on the size of the list.
        reversed_list = Linked_List()
        current = self.__head
        if current is not None:
            reversed_list.append_element(current.val)
            current = current.next
            while current is not None:
                reversed_list.insert_element_at(current.val, 0)
                current = current.next
        return reversed_list

# Tests to make sure linked list is running correctly
if __name__ == '__main__':
    ll = Linked_List()
    ll.append_element('hi')
    ll.append_element('I')
    ll.append_element('like')
    ll.append_element('pizza')
    print(ll)
# Testing if insert_element_at inserts in the correct position
    ll.insert_element_at(0, 0)
    print(ll)
# Testing if index for insert_element_at out of bounds
    try: 
        ll.insert_element_at(-5, -5)
        print(ll)
    except IndexError:
        print("Index Error")
# Testing if insert_element_at inserts in the correct position
    try: 
        ll.insert_element_at(1, 1)
        print(ll)
    except IndexError:
        print("Index Error")
# Testing if remove_element_at functions correctly
    try: 
        ll.remove_element_at(4)
        print(ll)
    except IndexError:
        print("Index Error")
# Testing remove_element_at when index is out of bounds
    try: 
        ll.remove_element_at(-3)
        print(ll)
    except IndexError:
        print("Index Error")
# Testing get_element_at to retrieve correct value
    try: 
        print(ll.get_element_at(3))
    except IndexError:
        print("Index Error")
# Testing when rotate_left rotates the linked list
    try: 
        ll.rotate_left()
        print(ll)
    except IndexError:
        print("Index Error")
# Testing the reversing of the linked list with reversed
    try: 
        print(reversed(ll))
    except IndexError:
        print("Index Error")
# Testing if iterating works throughout the linked list
    print ("")
    for val in ll:
        print(str(val))
    print (" ")
# Testing if iterating works throughout the reversed linked list
    print("")
    for val in reversed(ll):
        print(str(val))
    print(" ")