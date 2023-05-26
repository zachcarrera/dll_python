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
