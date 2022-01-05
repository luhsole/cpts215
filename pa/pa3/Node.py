# Node class definition
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