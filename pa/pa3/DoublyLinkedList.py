# Doubly Linked List (DLL) class definition
from Node import Node


class DLL:
    def __init__(self):
        '''
        Creates a new doubly linked list that is empty.
        '''
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        '''
        Creates and returns a string representation of the doubly linked list.
        '''
        if self.head is None:
            return '[]'
        else:
            curr = self.head
            result = '['
            while curr is not self.tail:
                result += str(curr.get_data()) + ', '
                curr = curr.get_next()
            result = result + str(curr.get_data()) + ']'
            return result

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

    def pop(self, index = None):
        '''
        Removes and returns the item at position index.
        If index is not specified, removes and returns the last item in the list.
        If the index is out of range, it does not update the list.
        '''
        if index is None:
            index = self.length - 1
        if (index < 0) or (index >= self.length) or (self.head is None):
            return None

        if index == 0:
            curr = self.head
            if curr.get_next() is not None:
                self.head = curr.get_next()
                self.head.set_prev(None)
                curr.set_next(None)
            else:
                self.head = None
                self.tail = None
        elif index == self.length-1:
            curr = self.tail
            prev = self.tail.get_prev()
            if prev is not None:
                prev.set_next(None)
                curr.set_prev(None)
                self.tail = prev
            else:
                self.tail = None
                self.head = None
        else:
            i = 0
            curr = self.head
            while i < index:
                curr = curr.get_next()
                i += 1
            curr.get_prev().set_next(curr.get_next())
            curr.get_next().set_prev(curr.get_prev())
            curr.set_prev(None)
            curr.set_next(None)

        self.length -= 1
        return curr.get_data()

    def remove(self, item):
        '''
        Removes the item from the list.
        The method does not update the list if the item is not present in the list
        '''
        index = self.search(item)
        self.pop(index)

    def search(self, item):
        '''
        Searches for the item in the list. It needs the item and returns the index of the item (-1 if not found).
        '''
        if self.head is None:
            return -1
        else:
            index = 0
            curr = self.head
            while (curr is not None) and (curr.get_data() != item):
                curr = curr.get_next()
                index += 1
            if curr is not None:
                return index
            else:
                return -1

    def get(self, index):
        '''
        Retrieves and returns item at the given position in the list.
        '''
        if (self.head is None) or (index < 0) or (index > self.length - 1):
            return None
        else:
            i = 0
            curr = self.head
            while i < index:
                curr = curr.get_next()
                i += 1
            if curr is not None:
                return curr.get_data()
            else:
                return None

    def put(self, index, item):
        '''
        Updates/Replaces the item at a given index position of the doubly linked list.
        '''
        if (index < 0) or (index > self.length):
            return None

        if self.head is None:
            self.add(item)
        elif index == self.length:
            self.append(item)
        else:
            curr = self.head
            i = 0
            while (i < index) and (i < self.length - 1):
                curr = curr.get_next()
                i += 1
            curr.set_data(item)

    def __getitem__(self, index):
        '''
        Retrieves and returns the data element at a given position index of the doubly linked list using indexing.
        '''
        return self.get(index)

    def __setitem__(self, index, item):
        '''
        Adds a new item to the doubly linked list using assignment operation at the given position index.
        '''
        self.put(index, item)

    def __delitem__(self, index):
        '''
        Deletes data from the list at the given index position
        '''
        self.pop(index)

    def __iter__(self):
        '''
        Returns and iterator object created by the generator method
        '''
        return self.generator()

    def generator(self):
        '''
        Creates an iterator object. Execution pauses during each loop and returns the current node data
        '''
        curr = self.head
        while curr is not None:
            yield curr
            curr = curr.get_next()

    def is_empty(self):
        '''
        The method checks if the list is empty and return a boolean value.
        '''
        return self.length == 0

    def size(self):
        '''
        Returns the number of items in the list.
        '''
        return self.length
