

# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# '''
# Fill this in

# Resizing hash table
# '''
class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None]*capacity


# '''
# Research and implement the djb2 hash function
# '''
def hash(string, max):
    hash = 5381
    for i in string:
        hash = ((hash << 5) + hash) + ord(i)
        return hash % max


# '''
# Fill this in.

# Hint: Used the LL to handle collisions
# '''
def hash_table_insert(hash_table, key, value):
    index = hash(key, hash_table.capacity)
    pair = hash_table.storage[index]
    new_pair = LinkedPair(key, value)
    prev_pair = None

    #check if exists/not empty and match
    while pair is not None and pair.key != key:
        prev_pair = pair
        pair = prev_pair.next

    if pair is not None and pair.key == key:
        pair.value = value  # update value of key

    elif pair is None:
        new_pair.next = hash_table.storage[index]
        hash_table.storage[index] = new_pair


# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    index = hash(key, hash_table.capacity)
    pair = hash_table.storage[index]
    #check if exists/not empty and match
    if pair is not None:
        while pair is not None and pair.key != key:
            pair = pair.next
        if pair.key == key:
            #remove reference to key
            hash_table.storage[index] = pair.next
    else:
        print(f'Warning: Unable to find key: {key}')


# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    index = hash(key, hash_table.capacity)
    pair = hash_table.storage[index]
    #check if exists/not empty and match
    while pair is not None:
        if pair.key == key:
            return pair.value
        #set to .next pair if no match
        pair = pair.next


# '''
# Fill this in
# '''
def hash_table_resize(hash_table):
    #double size of given array
    new_capacity = HashTable(2 * hash_table.capacity)
    #insert from old hash table into new
    for index in range(len(hash_table.storage)):
        pair = hash_table.storage[index]
        while pair != None:
            hash_table_insert(new_capacity, pair.key, pair.value)
            print([i.key for i in new_capacity.storage if i is not None])
            #go to next pair
            pair = pair.next
    return new_capacity


def Testing():
    ht = HashTable(2)

    hash_table_insert(ht, "line_1", "Tiny hash table")
    hash_table_insert(ht, "line_2", "Filled beyond capacity")
    hash_table_insert(ht, "line_3", "Linked list saves the day!")

    print(hash_table_retrieve(ht, "line_1"))
    print(hash_table_retrieve(ht, "line_2"))
    print(hash_table_retrieve(ht, "line_3"))

    old_capacity = len(ht.storage)
    ht = hash_table_resize(ht)
    new_capacity = len(ht.storage)

    print("Resized hash table from " + str(old_capacity)
          + " to " + str(new_capacity) + ".")


Testing()
