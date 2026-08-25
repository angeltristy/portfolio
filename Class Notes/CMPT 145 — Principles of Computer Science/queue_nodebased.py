"""
Angel Clarke rlv890 11345050
CMPT 145 02 L14
"""
import node as N

class Queue(object):
    def __init__(self):
        """
        Purpose
            creates an empty queue
        """
        self.__size = 0
        self.__front = None
        self.__back = None

    def size(self):
        """
        Purpose
            returns the number of data values in the queue
        Pre-conditions:
            queue: a queue object
        Return:
            The number of data values in the queue
        """
        return self.__size

    def is_empty(self):
        """
        Purpose
            checks if the given queue has no data in it
        Return:
            True if the queeu has no data or false otherwise
        """
        return self.__size == 0

    def enqueue(self, value):
        """
        Purpose
            adds the given data value to the queue
        Pre-conditions:
            value: data to be added
        Post-conditions:
            the value is added to the queue
        Return:
            (none)
        """
        new_node = N.node(value, None)

        if self.is_empty():
            self.__front = new_node
            self.__front = new_node
        else:
            prev_last_node = self.__back
            prev_last_node.set_next(new_node)
            self.__back = new_node

        self.__size += 1

    def dequeue(self, value):
        """
        Purpose
            removes and returns a data value from the queue
            Note: the queue cannot be empty!
        Post-conditions:
            the first value is removed from the queue
        Return:
            the first value in the queue, or None
        """
        assert not self.is_empty(), 'dequeued an empty queue'

        prev_first_node = self.__front()
        result = prev_first_node.get_data()
        self.__front = prev_first_node.get_next()
        self.__size -= 1
        if self.__size == 0:
            self.__back = None
        return result

    def peek(self):
        """
        Purpose
            returns the value from the front of queue without removing it
            Note: the queue cannot be empty
        Post-conditions:
            None
        Return:
            the value at the front of the queue
        """
        assert not self.is_empty(), 'peeked into an empty queue'

        first_node = self.__front
        result = first_node.get_data()
        return result
