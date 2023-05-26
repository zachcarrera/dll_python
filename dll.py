"""A Doubly Linked List Implementation"""


class DLLNode:
    """A node for a doubly linked list"""

    def __init__(self, value) -> None:
        self.value = value
        self.prev: DLLNode | None = None
        self.next: DLLNode | None = None


class DLList:
    """A doubly linked list representation"""

    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def add_to_front(self, value):
        """add a node to the front of the list"""

        new_node = DLLNode(value)

        # insert into empty list
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return self

        # insert into list with one or more nodes
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        return self

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
