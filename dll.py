"""A Doubly Linked List Implementation"""


class DLLNode:
    """A node for a doubly linked list"""

    def __init__(self, value) -> None:
        self.value = value
        self.prev = None
        self.next = None


class DLList:
    """A doubly linked list representation"""

    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def print_list(self):
        """print the doubly linked list"""

        if self.head is None:
            print("Empty List")
            return self
        runner = self.head

        while runner is not None:
            runner = runner.next

        return self


dll_1 = DLList()
dll_1.print_list()
