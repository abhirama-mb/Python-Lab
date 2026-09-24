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

    def nth_node_from_end(self, n):
        slow = self.head
        fast = self.head

        for _ in range(n):
            if fast is None:
                return None

            fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next

        return slow.data


ll = LinkedList()

ll.insert_at_end(10)
ll.insert_at_end(20)
ll.insert_at_end(30)
ll.insert_at_end(40)
ll.insert_at_end(50)

print(ll.nth_node_from_end(2))