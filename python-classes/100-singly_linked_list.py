#!/usr/bin/python3
# class Node
"""
    define a class 'Node'
"""


class Node:
    """
        node in a singly-linked list
    """

    def __init__(self, data, next_node=None):
        """
            initialize new node
            Args:
                data (int): data of the new node
                next_node (Node): next node of the new node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
            get the data of the node
        """
        return (self.__data)

    @data.setter
    def data(self, value):
        """
            validates that data is an integer
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
            get the next_node of the Node
        """
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """
            validates next_node as either None or a node
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
        define a class 'SinglyLinkedList'
    """

    def __init__(self):
        """
            initalize a new SinglyLinkedList
        """
        self.__head = None

    def sorted_insert(self, value):
        """
            insert a new Node to the SinglyLinkedList
            Args:
                value (Node): new Node to insert
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """
            define the print() representation of a SinglyLinkedList
        """
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))
