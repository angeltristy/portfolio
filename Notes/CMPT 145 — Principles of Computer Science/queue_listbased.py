def __init__(self):
    """
    Purpose: creates an empty queue
    """
    self.__data = list()

def is_empty(self):
    """
    Purpose:
        checks if the given queue has no data in it
    Return:
        true if the queue has no data, or false otherwise
    """
    return len(self.__data) == 0
def size(self):
    """
    Purpose:
        returns the number of data values in the given queue
    Return:
        The number of data values in the given queue
    """
    return len(self.__data)

def enqueue(self, value):
    """
    Purpose:
        Adds the given data value to the given queue
    Pre-conditions:
        value: data to be added
    Post-conditions:
        value is added to queue
    Returns:
        None
    """
    self.__data.append(value)

def dequeue(self):
    """
    Purpose:
        Removes and returns a data value from the given queue
    Post-condiitons:
        the first value is removed from the queue
    Returns:
        the first value in the queue
    """
    return self.__data.pop(0)

def peek(self):
    """
    Purpose:
        returns the value from the front of given queue without removing it
    Post-condition:
        none
    Return:
        the value at the front of the queue
    """
    return self.__data[0]