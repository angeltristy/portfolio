class Node(object):
    def __init__(self, data, next=None):
        self.__data = data
        self.__next = next
    def get_data(self):
        """
        Purpose:
            Retrieve the contents of the data field
        Return:
            the data value stored previously in the node
        """
        return self.__data
    def get_next(self):
        """
        Purpose:
            Retrieve the contents of the next field
        Return:
            the value sotred previously in the next field
        """
        return self.__next
    def set_data(self, val):
        """
        Purpose:
            Set the contents of the data field to val
        Pre-conditions:
            val: a data value to be stored
        Post-conditions:
            stores a new data value, replacing existing value
        Return:
            None
        """
        self.__data = val
    def set_next(self, val):
        """
        Purpose:
            Set the contents of the next field to val
        Pre-conditions:
            val: a data value to be stored
        Post-conditions:
            stores a new data value, replacing existing value
        Return:
            None
        """
        self.__next = val