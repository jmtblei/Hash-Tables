

# '''
# Basic hash table key/value pair
# '''
class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value


# '''
# Basic hash table
# Fill this in.  All storage values should be initialized to None
# '''
class BasicHashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None]*capacity
        self.count = 0


# '''
# Fill this in.
# Research and implement the djb2 hash function
# '''
def hash(string, max):
    hash = 5381
    for i in string:
        hash = ((hash << 5) + hash) + ord(i)
        return hash % max


# '''
# Fill this in.

# If you are overwriting a value with a different key, print a warning.
# '''
def hash_table_insert(hash_table, key, value):
    index = hash(key, hash_table.capacity)
    #check if exists
    if hash_table.storage[index] is not None:
        #check if match
        if hash_table.storage[index].key != key:
            print(f'Warning, {str(index)} does not match {hash_table.storage[index]} and will be overwritten')
    hash_table.storage[index]=Pair(key, value)

# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    index = hash(key, hash_table.capacity)
    if hash_table.storage[index] is None or hash_table.storage[index].key != key:
        print(f'Warning, unable to remove item with key: {key}. Not found')
    else:
        hash_table.storage[index] = None
        


# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    index = hash(key, hash_table.capacity)
    #check if exists
    if hash_table.storage[index] is not None:
        #if doesn't match, return none
        if hash_table.storage[index].key != key:
            return None
        #return if is
        else:
            return hash_table.storage[index].value
    print(f'Unable to find key: {key}')
    return None


def Testing():
    ht = BasicHashTable(16)

    hash_table_insert(ht, "line", "Here today...\n")

    hash_table_remove(ht, "line")

    if hash_table_retrieve(ht, "line") is None:
        print("...gone tomorrow (success!)")
    else:
        print("ERROR:  STILL HERE")


Testing()
