class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next = new_node
            self.tail = new_node

    def search(self, target):
        current = self.head

        while current is not None:
            if current.data == target:
                return True

            current = current.next
    def delete(self, target):
        current = self.head
        previous = None

        while current is not None:
            if current.data == target:

                if previous is None:
                    self.head = current.next

                else:
                    previous.next = current.next

                if current == self.tail:
                    self.tail = previous

                return True

            previous = current
            current = current.next

        return False