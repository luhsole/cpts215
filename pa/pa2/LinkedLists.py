# PA 2: DLL and CDLL
# Version: 1.0
# Date: October 10, 2021
#
# This program is an implementation of doubly linked list and circular doubly linked list.


class Node:
    '''
    Creates a Node object
    '''

    def __init__(self, data):
        '''
        Initializes values to use in a Node
        :param data: the data to store in the Node
        '''
        self.data = data
        self.next = None
        self.prev = None

    def get_data(self):
        '''
        Finds the data value of a Node
        :return: the data value of the Node
        '''
        return self.data

    def set_data(self, newdata):
        '''
        Sets the data of a Node
        :param newdata: the data to store
        :return:
        '''
        self.data = newdata


class DoublyLinkedList:
    '''
    Creates a Doubly Linked List object
    '''

    def __init__(self):
        '''
        Initializes the values of the DLL
        '''
        self.head = None
        self.tail = None
        self.length = 0

    def add(self, item):
        '''
        Adds a Node with the item value at the beginning of the DLL
        :param item: the data value to add
        :return:
        '''
        self.insert(0, item)

    def append(self, item):
        '''
        Adds a Node with the item value at the end of the DLL
        :param item: the data value to add
        :return:
        '''
        self.insert(self.length, item)

    def insert(self, index, item):
        '''
        Adds a node with the item value at the given index of the DLL
        :param index: the index to insert item
        :param item: the data value to add
        :return:
        '''
        newnode = Node(item)
        if index > self.length or index < 0:
            print("Index %s is invalid." % index)

        if index == 0:
            newnode.next = self.head
            if self.tail is None:
                self.tail = newnode
            else:
                self.head.prev = newnode
            self.head = newnode
        elif index == self.length:
            newnode.prev = self.tail
            if self.head is None:
                self.head = newnode
            else:
                self.tail.next = newnode
            self.tail = newnode
        else:
            temp = self.head
            count = 0
            while temp.next is not None and count < index:
                temp = temp.next
                count += 1
            newnode.next = temp
            newnode.prev = temp.prev
            temp.prev.next = newnode
            temp.prev = newnode
        self.length += 1

    def pop(self, index):
        '''
        Removes the Node at the given index
        :param index: the index of the Node to remove
        :return:
        '''
        if index is None:
            index = self.length - 1
        elif index > self.length or index < 0:
            print("Index %s is invalid." % index)
        if 0 <= index < self.length:
            if index == 0:
                self.head = self.head.next
            elif index == self.length - 1:
                temp = self.head
                while temp.next.next is not None:
                    temp = temp.next
                temp.next = None
            else:
                temp = self.head
                count = 0
                while temp.next.next is not None and count < index:
                    temp = temp.next
                    count += 1
                temp.prev.next = temp.next
                temp.next.prev = temp.prev
        self.length -= 1

    def remove(self, item):
        '''
        Removes the Node with item value
        :param item: the data value of the Node to remove
        :return:
        '''
        count = 0
        node_to_match = self.head
        exist = False
        while count < self.length:
            if node_to_match.get_data() == item:
                self.pop(count)
                exist = True
                count = self.length
            node_to_match = node_to_match.next
            count += 1
        if exist is False:
            print("%s does not exist in the list." % item)

    def search(self, item):
        '''
        Searches for the item in the DLL
        :param item: the data value to search
        :return: True if item exists, False if not
        '''
        temp = self.head
        while temp is not None:
            if temp.get_data() == item:
                return True
            temp = temp.next
        return False

    def is_empty(self):
        '''
        Checks if the DLL is empty
        :return: True if empty, False if not
        '''
        return self.head is None

    def size(self):
        '''
        Returns the size of the DLL
        :return: the size of the DLL
        '''
        return self.length

    def __str__(self):
        '''
        Creates String representation of the DLL
        :return: String representation of the DLL
        '''
        if self.head is None:
            return ""
        temp = self.head
        s = str(temp.get_data())
        while temp.next is not None:
            temp = temp.next
            s = s + ", " + str(temp.get_data())
        return s


class CircularDoublyLinkedList:
    def __init__(self):
        '''
        Initializes the values of CDLL
        '''
        self.head = None
        self.length = 0

    def add(self, item):
        '''
        Adds a Node with the item value at the beginning of the CDLL
        :param item: the item value
        :return:
        '''
        self.insert(0, item)

    def append(self, item):
        '''
        Adds a Node with the item value at the end of the CDLL
        :param item: the item value
        :return:
        '''
        self.insert(self.length, item)

    def insert(self, index, item):
        '''
        Adds a Node with the item value at the given index of the CDLL
        :param index: the index to insert the node
        :param item: the data value to insert
        :return:
        '''
        newnode = Node(item)
        if index > self.length or index < 0:
            print("Index %s is invalid." % index)
        if self.head is None:
            self.head = newnode
            newnode.prev = self.head
            newnode.next = self.head

        temp = self.head
        if index == 0:
            temp = temp.prev
        else:
            count = 0
            while temp.next is not self.head and count < index - 1:
                temp = temp.next
                count += 1
        temp.next.prev = newnode
        newnode.next = temp.next
        newnode.prev = temp
        temp.next = temp.next.prev
        if index == 0:
            self.head = self.head.prev
        self.length += 1

    def pop(self, index):
        '''
        Removes the Node at the given index
        :param index: the index of the node to remove
        :return:
        '''
        if index is None:
            index = self.length - 1
        elif index >= self.length or index < 0:
            print("Index %s is invalid." % index)
        if 0 <= index < self.length:
            if index == 0:
                temp = self.head
                if self.head.next is self.head:
                    self.head = None
                else:
                    while temp.next is not self.head:
                        temp = temp.next
                    self.head = self.head.next
                    temp.next = self.head
                    self.head.prev = temp
            elif index == self.length - 1:
                temp = self.head
                while temp.next.next is not self.head:
                    temp = temp.next
                temp.next = self.head
                self.head.prev = temp
            else:
                temp = self.head
                count = 0
                while count < index - 1:
                    temp = temp.next
                    count += 1
                temp.next = temp.next.next
                temp.next.prev = temp
            self.length -= 1

    def remove(self, item):
        '''
        Removes the Node with the item value
        :param item: the data value of the Node to remove
        :return:
        '''
        count = 0
        node_to_match = self.head
        exist = False
        while count < self.length:
            if node_to_match.get_data() == item:
                self.pop(count)
                exist = True
                count = self.length
            node_to_match = node_to_match.next
            count += 1
        if exist is False:
            print("%s does not exist in the list." % item)

    def search(self, item):
        '''
        Searches for the item in the CDLL
        :param item: the data value to search
        :return: True if item exists, False if not
        '''
        temp = self.head
        while temp is not None:
            if temp.get_data() == item:
                return True
            temp = temp.next
            if temp is self.head:
                return False
        return False

    def is_empty(self):
        '''
        Checks if the CDLL is empty
        :return: True if empty, False if not
        '''
        return self.head is None

    def size(self):
        '''
        Returns the size of the CDLL
        :return: the size of the CDLL
        '''
        return self.length

    def __str__(self):
        '''
        Creates String representation of the CDLL
        :return: String representation of the CDLL
        :return:
        '''
        if self.head is None:
            return ""
        temp = self.head
        s = str(temp.get_data())
        while temp.next is not self.head:
            temp = temp.next
            s = s + ", " + str(temp.get_data())
        return s
