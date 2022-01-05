
# PA5: HashMap
# Version 1.0
# November 28, 2021
# An implementation of HashMap with two lists: key and value.

class HashMap:
    def __init__(self, size=1):
        '''
        Constructor initializing global variables
        :param size: size of lists
        '''
        self.size = size
        self.keylist = [[None] for _ in range(self.size)]
        self.valuelist = [[None] for _ in range(self.size)]

    def __str__(self):
        '''
        Return a string representation of key-value pairs stored in the map
        :return:
        '''
        s = "["
        for slot, key in enumerate(self.keylist):
            value = self.valuelist[slot]
            s += str(key) + ":" + str(value) + ", "
        return s + "]"

    def __len__(self):
        '''
        Return the number of key-value pairs present in the map
        :return: number of pairs
        '''
        count = 0
        for item in self.keylist:
            if item is not None:
                count += 1
        return count

    def __contains__(self, key):
        '''
        Checks if a key is present in the map
        :param key: key to search
        :return: True if present, False if not
        '''
        return self.get(key) != -1

    def __getitem__(self, key):
        '''
        Searches for the key in the map and returns the corresponding value
        :param key: key to search
        :return: value of the key, -1 if key does not exist
        '''
        return self.get(key)

    def __setitem__(self, key, value):
        '''
        Adds a key-value pair to the map
        :param key: key to add
        :param value: value to add
        :return:
        '''
        self.put(key, value)

    def __delitem__(self, key):
        '''
        Removes item
        :param key: key to remove
        :return:
        '''
        self.remove(key)

    def hashfunction(self, item):
        '''
        Applies a hash function on the key and returns its slot position
        :param item: item to perform function on
        :return:
        '''
        key = 0
        for x in item:
            key += ord(x)
        return key % self.size

    def rehash(self, oldhash):
        return (oldhash + 1) % self.size

    def put(self, key, value):
        '''
        Adds a key-value pair to the map
        :param key: key to add
        :param value: value to add
        :return: the slot position
        '''
        hashvalue = self.hashfunction(key)
        slot_placed = -1
        # check if key exists in map
        if self.keylist[hashvalue] == [None] or self.keylist[hashvalue][0] == key:
            # if slot is empty or key exists at hashvalue, store key in slot
            self.keylist[hashvalue][0] = key
            slot_placed = hashvalue
        else:
            # if key does not exist at hashvalue, rehash
            nextslot = self.rehash(hashvalue)
            while self.keylist[nextslot] != [None] and self.keylist[nextslot][0] != key:
                # if a key at slot exists but not the same key, rehash
                nextslot = self.rehash(nextslot)
                if nextslot == hashvalue:
                    # if no slots are available return -1
                    return slot_placed
            # store key in slot
            self.keylist[nextslot][0] = key
            slot_placed = nextslot
        # check if value already exists in map
        if self.valuelist[slot_placed] == [None]:
            # if there is no value, store value in slot
            self.valuelist[slot_placed][0] = value
        else:
            # if there already is a value, insert the new value in the slot
            self.valuelist[slot_placed].insert(0, value)
        return slot_placed

    def get(self, key):
        '''
        Searches for the key in the map and returns the corresponding value
        :param key: key to search
        :return: value of the key, -1 if key does not exist
        '''
        startslot = self.hashfunction(key)
        stop = False
        found = False
        position = startslot
        while not found and not stop:
            if self.keylist[position][0] == key:
                found = True
            else:
                position = self.rehash(position)
                if position == startslot:
                    stop = True
        if found:
            # return self.valuelist[position]
            return self.valuelist[position][0]
        else:
            return -1

    def remove(self, key):
        '''
        Removes item
        :param key: key to remove
        :return:
        '''
        startslot = self.hashfunction(key)
        stop = False
        found = False
        position = startslot
        while not found and not stop:
            if self.keylist[position][0] == key:
                found = True
                self.keylist[position] = [None]
            else:
                position = self.rehash(position)
                if position == startslot:
                    stop = True
        if found:
            self.valuelist[position] = [None]
            return position
        else:
            return -1


