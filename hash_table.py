
class Contact:
    '''
    Contact class to represent a contact with a name and number.
    '''

    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __str__(self):
        return f"{self.name}: {self.number}"


class Node:
    '''
    Node class to represent a single entry in the hash table.
    '''

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None



class HashTable:
    '''
    HashTable class to store and search contacts.
    Uses separate chaining to handle collisions.
    '''

    def __init__(self, size):
        self.size = size
        self.data = [None] * size

    def hash_function(self, key):
        total = 0
        for char in key:
            total += ord(char)
        return total % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        new_contact = Contact(key, value)

        current = self.data[index]

        while current is not None:
            if current.key == key:
                current.value = new_contact
                return
            current = current.next

        new_node = Node(key, new_contact)
        new_node.next = self.data[index]
        self.data[index] = new_node

    def search(self, key):
        index = self.hash_function(key)
        current = self.data[index]

        while current is not None:
            if current.key == key:
                return current.value
            current = current.next

        return None

    def print_table(self):
        for i in range(self.size):
            current = self.data[i]
            print(f"Index {i}:", end=" ")

            if current is None:
                print("Empty")
            else:
                while current is not None:
                    print(f"- {current.value}", end=" ")
                    current = current.next
                print()


# Test your hash table implementation here.  

# Test the contact management system
if __name__ == "__main__":
    table = HashTable(10)

    print("Empty Hash Table:")
    table.print_table()

    # Add contacts
    print("\nAdding Contacts:")
    table.insert("John", "909-876-1234")
    table.insert("Rebecca", "111-555-0002")
    table.print_table()

    # Search for a contact
    print("\nSearching for John:")
    print(table.search("John"))

    # Test collisions
    print("\nTesting Collisions:")
    table.insert("Amy", "111-222-3333")
    table.insert("May", "222-333-1111")
    table.print_table()

    # Test duplicate names
    print("\nUpdating Rebecca:")
    table.insert("Rebecca", "999-444-9999")
    table.print_table()

    # Search for a missing contact
    print("\nSearching for Chris:")
    print(table.search("Chris"))
