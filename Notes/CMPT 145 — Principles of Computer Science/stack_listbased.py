class Stack(object):
    def __init__(self):
        """
        Purpose: Initializes list for the stack
        """
        self.__data = list()

    def is_empty(self):
        """
        Purpose:
            Returns true if stack has no data in it
        Returns:
            True if queue has no data, false otherwise
        """
        return len(self.__data) == 0

    def size(self):
        """
        Purpose:
            Returns length of the stack
        Returns:
            The number of data values in the stack
        """
        return len(self.__data)

    def push(self, value):
        """
        Purpose:
            Adds the given data value to the stack
        Pre-conditions:
            value: data to be added
        Post-conditions:
            the value is added to the stack
        Return:
            none
        """
        self.__data.append(value)

    def pop(self):
        """
        Purpose:
            Removes and returns a data value from the stack
        Post-conditions:
            the top value is removed from the stack
        Returns:
            returns the value at the top of the stack
        """
        return self.__data.pop()

    def peek(self):
        """
        Purpose:
            returns the value from the front of stack without removing it
        Post-conditions:
            None
        Return:
            the value at the front of the stack
        """
        return self.__data[-1]