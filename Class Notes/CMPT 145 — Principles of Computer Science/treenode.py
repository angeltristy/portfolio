class treenode(object):
    def __init__(self, data, left=None, right=None):
        """
        Creates a new treenode for the given data
        Pre-conditions:
            data:   Any data value to be stored in the treenode
            left:   Another treenode (or None, by default)
            right:  Another treenode (or None, by default)
        """
        self.data = data
        self.left = left
        self.right = right

def pre_order(tnode):
    """
    Display the nodes of a tree in pre-order.
    :param tnode: a primitive tree
    :return: None
    """
    if tnode is None:
        return
    else:
        print(tnode.data, end=" ")
        pre_order(tnode.left)
        pre_order(tnode.right)

def in_order(tnode):
    """
    Display the nodes of a tree in in-order.
    :param tnode: a primitive tree
    :return: Nothing
    """
    if tnode is None:
        return
    else:
        in_order(tnode.left)
        print(tnode.data, end=" ")
        in_order(tnode.right)

def post_order(tnode):
    """
    Display the nodes of a tree in post-order
    :param tnode: a primitive tree
    :return: Nothing
    """
    if tnode is None:
        return
    else:
        post_order(tnode.left)
        post_order(tnode.right)
        print(tnode.data, end=" ")

import Queue as Q
def breadth_order(tnode):
    """
    Display the nodes of a tree in breadth-order.
    :param tnode: a primitive tree
    :return: Nothing
    """
    explore = Q.SimpleQueue()
    explore.enqueue(tnode)

    while explore.size() > 0:
        current = explore.dequeue()
        print(current.data, end=" ")
        if current.left is not None:
            explore.enqueue(current.left)
        if current.right is not None:
            explore.enqueue(current.right)

def height(tnode) -> int:
    """
    Purpose:
        Determine the height of a tree
        The height is defined as the length of the longest path from the root to any leaf
    Pre-conditions:
        :param tnode: a treenode
    Post-conditions:
        none
    Return:
        :return: the ehight of the tree as an integer
    """
    if tnode is None:
        return 0
    else:
        lh = height(tnode.left)
        rh = height(tnode.right)
        return 1 + max(lh, rh)

def count(tnode) -> int:
    """
    Purpose:
        Determine the number of nodes in the tree.
    Pre-conditions:
        :param tnode: a treenode
    Post-conditions:
        none
    Return:
        :return: the number of nodes as an integer
    """
    if tnode is None:
        return 0
    else:
        1 + count(tnode.left) + count(tnode.right)

def member(tnode, val) -> int:
    """
    Purpose:
        Determine if val is stored as data in a tree.
    Pre-conditions:
        :param tnode: a treenode
        :param val: value to look for in treenode
    Post-conditions:
        noen
    Return:
        :return: the height of the tree as an integer
    """
    if tnode is None:
        return False
    elif tnode.data == val:
        return True
    else:
        return member(tnode.left, val) or member(tnode.right, val)