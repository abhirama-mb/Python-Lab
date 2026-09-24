class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        current = self.head

        while current:
            print(current.data, end=" -> ")
            current = current.next

        print("None")

    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = new_node

    def delete_from_beginning(self):
        if self.head is None:
            return

        self.head = self.head.next

    def delete_from_end(self):
        if self.head is None:
            return

        if self.head.next is None:
            self.head = None
            return

        current = self.head

        while current.next.next:
            current = current.next

        current.next = None

    def delete_by_value(self, value):
        if self.head is None:
            return

        if self.head.data == value:
            self.head = self.head.next
            return

        current = self.head

        while current.next:
            if current.next.data == value:
                current.next = current.next.next
                return

            current = current.next

    def delete_at_position(self, position):
        if self.head is None:
            return

        if position == 0:
            self.head = self.head.next
            return

        current = self.head

        for _ in range(position - 1):
            if current.next is None:
                return
            current = current.next

        if current.next is None:
            return

        current.next = current.next.next


ll = LinkedList()

ll.insert_at_end(10)
ll.insert_at_end(20)
ll.insert_at_end(30)
ll.insert_at_end(40)

ll.display()

ll.delete_from_beginning()
ll.display()

ll.delete_from_end()
ll.display()

ll.delete_by_value(20)
ll.display()

ll.delete_at_position(0)
ll.display()