class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = new_node

    def search(self, value):
        current = self.head

        while current:
            if current.data == value:
                return True

            current = current.next

        return False

    def length(self):
        count = 0
        current = self.head

        while current:
            count += 1
            current = current.next

        return count


ll = LinkedList()

ll.insert_at_end(10)
ll.insert_at_end(20)
ll.insert_at_end(30)

print(ll.search(20))
print(ll.search(50))

print("Length:", ll.length())