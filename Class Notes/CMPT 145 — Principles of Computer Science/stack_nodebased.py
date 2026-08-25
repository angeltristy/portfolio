"""
Angel Clarke rlv890 11345050
CMPT 145 02 L14
"""

class Stack(object):
    def __init__(self):
        """
        Purpose
            creates an empty stack
        """
        self.__size = 0
        self.__top = None

    def size(self):
        """
        Purpose:
            returns the number of data values in the stack
        Return:
            the number of data values in the stack
        """
        return self.__size

    def is_empty(self):
        """
        Purpose:
            checks if the stack has no data in it
        Return:
            true if the stack has no data, or false otherwise
        """
        return self.__size == 0

    def push(self, value):
        """
        Purpose
            adds the given data value to the stack
        Pre-conditions:
            value: data to be added
        Post-condition:
            the value is added to the stack
        Return:
            (none)
        """
        new_node = N.node(value, self.__top)
        self.__top = new_node
        self.__size += 1

    def pop(self):
        """
        Purpose:
            Removes and returns a data value from the stack
            Note: the stack cannot be empty!
        Post-condition:
            the first value is removed from the stack
        Return:
            The first value in the stack, or None
        """
        assert not self.is_empty(), 'popped an empty stack'
        prev_first_node = self.__top
        result = prev_first_node.get_data()
        self.__top = prev_first_node.get_next()
        self.__size -= 1
        return result

    def peek(self):
        """
        Purpose
            returns the value from the top of given stakc without removing it
            Note: the stack cannot be empty!
        Post-condition:
            None
        Return:
            the value at the top of the stack
        """
        assert self.is_empty(), 'peeked into an empty stack'
        first_node = self.__top
        result = first_node.get_data()
        return result