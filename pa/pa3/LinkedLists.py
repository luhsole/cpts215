# Hansol Lee
# PA 3: DLL
# Version: 1.0
# Date: October 10, 2021
#
# This program is an implementation of doubly linked list.


class Node:
    def __init__(self, value=0):
        self.data = value
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.data)

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def get_prev(self):
        return self.prev

    def set_data(self, newvalue):
        self.data = newvalue

    def set_next(self, newnext):
        self.next = newnext

    def set_prev(self, newprev):
        self.prev = newprev


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
        :return: the data to remove
        '''
        if (index is None):
            index = self.length - 1
        if (index < 0) or (index >= self.length) or (self.head is None):
            return None

        if (index == 0):
            curr = self.head
            if (curr.get_next() is not None):
                self.head = curr.get_next()
                self.head.set_prev(None)
                curr.set_next(None)
            else:
                self.head = None
                self.tail = None
        elif (index == self.length-1):
            curr = self.tail
            prev = self.tail.get_prev()
            if (prev is not None):
                prev.set_next(None)
                curr.set_prev(None)
                self.tail = prev
            else:
                self.tail = None
                self.head = None
        else:
            i = 0
            curr = self.head
            while (i < index):
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

    def get(self, index):
        '''
        Retrieves and returns item at the given position in the list.
        '''
        if (self.head is None) or (index < 0) or (index > self.length-1):
            return None
        else:
            i = 0
            curr = self.head
            while (i < index):
                curr = curr.get_next()
                i += 1
            if (curr is not None):
                return curr.get_data()
            else:
                return None

    def put(self, index, item):
        '''
        Updates/Replaces the item at a given index position of the doubly linked list.
        '''
        if (index < 0) or (index > self.length):
            return None

        if (self.head is None):
            self.add(item)
        elif (index == self.length):
            self.append(item)
        else:
            curr = self.head
            i = 0
            while (i < index) and (i < self.length-1):
                curr = curr.get_next()
                i += 1
            curr.set_data(item)

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

    def __str__(self):
        '''
        Creates String representation of the DLL
        :return: String representation of the DLL
        '''
        if self.head is None:
            return "[]"
        temp = self.head
        s = str(temp.get_data())
        while temp.next is not None:
            temp = temp.next
            s = s + ", " + str(temp.get_data())
        return "[" + s + "]"


def main():
    dll = DoublyLinkedList()
    print("dll.is_empty(): ", str(dll.is_empty()))
    # dll.insert(0, 0)
    dll.add(1)
    print("dll.add(1): ", dll)
    dll.append(3)
    dll.append(5)
    dll.append(7)
    print("dll.append(3, 5, 7): ", dll)
    print("dll.size(): ", str(dll.size()))
    dll.insert(0, 0)
    print("dll.insert(0, 0): ", dll)
    dll.insert(5, 9)
    print("dll.insert(5, 9): ", dll)
    dll.insert(2, 2)
    print("dll.insert(2, 2): ", dll)
    print("dll.size(): ", str(dll.size()))
    dll.pop(0)
    print("dll.pop(0): ", dll)
    dll.pop(3)
    print("dll.pop(3): ", dll)
    dll.pop(4)
    print("dll.pop(4): ", dll)
    dll.pop(None)
    print("dll.pop(None): ", dll)

    # temp_dll = dll
    # temp_dll.pop(1)
    # print(dll)
    # print(temp_dll)

    print("dll.size(): ", str(dll.size()))
    dll.remove(2)
    print("dll.remove(2): ", dll)
    dll.remove(4)
    print("dll.size(): ", str(dll.size()))
    print("dll.search(3): ", str(dll.search(3)))
    print("dll.search(4): ", str(dll.search(4)))
    print("dll.is_empty(): ", str(dll.is_empty()))

    print("-----------------------------------")

    # cdll = CircularDoublyLinkedList()
    # print("cdll.is_empty(): ", str(cdll.is_empty()))
    # # cdll.insert(0, 0)
    # cdll.add(1)
    # print("cdll.add(1): ", cdll)
    # cdll.append(3)
    # cdll.append(5)
    # cdll.append(7)
    # print("cdll.append(3, 5, 7): ", cdll)
    # print("cdll.size(): ", str(cdll.size()))
    # cdll.insert(0, 0)
    # print("cdll.insert(0, 0): ", cdll)
    # cdll.insert(5, 9)
    # print("cdll.insert(5, 9): ", cdll)
    # cdll.insert(2, 2)
    # print("cdll.insert(2, 2): ", cdll)
    # print("cdll.size(): ", str(cdll.size()))
    # cdll.pop(0)
    # print("cdll.pop(0): ", cdll)
    # cdll.pop(3)
    # print("cdll.pop(3): ", cdll)
    # cdll.pop(4)
    # print("cdll.pop(4): ", cdll)
    # cdll.pop(None)
    # print("cdll.pop(None): ", cdll)
    # print("cdll.size(): ", str(cdll.size()))
    # cdll.remove(3)
    # print("cdll.remove(3): ", cdll)
    # cdll.remove(4)
    # print("cdll.size(): ", str(cdll.size()))
    # print("cdll.search(2): ", str(cdll.search(2)))
    # print("cdll.search(4): ", str(cdll.search(4)))
    # print("cdll.is_empty(): ", str(cdll.is_empty()))


# main()