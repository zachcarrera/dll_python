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
        self.head: DLLNode | None = None
        self.tail: DLLNode | None = None

    def is_empty(self):
        """check if a list is empty"""

        return self.head is None

    def size(self):
        """return the size of the doubly linked list"""

        if self.is_empty():
            return 0

        runner = self.head
        count = 1

        while runner is not None:
            runner = runner.next
            count += 1

        return count

    def add_to_front(self, value):
        """add a node to the front of the list"""

        new_node = DLLNode(value)

        # insert into empty list
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            return self

        # insert into list with one or more nodes
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        return self

    def add_to_back(self, value):
        """add a node to the back of the list"""

        # empty list
        if self.is_empty():
            return self.add_to_front(value)

        # not empty list
        new_node = DLLNode(value)

        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node
        return self

    def remove_from_front(self):
        """remove a node from the front of the list"""

        if self.is_empty():
            return

        # if there only one node
        if self.head.next is None:
            removed_node = self.head
            self.tail = None
            self.head = None
            return removed_node.value

        removed_node = self.head
        self.head = self.head.next
        self.head.prev = None
        return removed_node.value

    def remove_from_back(self):
        """remove a node form the back of the list"""

        if self.is_empty():
            return

        # if there is only one node
        # self.head needs to be set to None
        if self.head.next is None:
            removed_node = self.tail
            self.tail = None
            self.head = None
            return removed_node.value

        removed_node = self.tail
        self.tail = self.tail.prev
        return removed_node.value

    def remove_value(self, value):
        """remove the first node that is found with the given value"""

        if self.is_empty():
            return

        runner = self.head

        while runner is not None and runner.value != value:
            runner = runner.next

        # either value found or at the end of the list
        if runner is None:
            return

        # remove from middle, front or back
        if runner is self.head:
            return self.remove_from_front()

        if runner is self.tail:
            return self.remove_from_back()

        runner.prev.next = runner.next
        runner.next.prev = runner.prev

        return runner.value

    def print_list(self):
        """print the doubly linked list"""

        if self.is_empty():
            print("Empty List")
            return self
        runner = self.head

        while runner is not None:
            runner = runner.next

        return self


dll_1 = DLList()
dll_1.print_list()
