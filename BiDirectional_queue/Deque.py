class Node:
    def __init__(self, value = None, next = None, previous = None):
        self.value = value
        self.next = next
        self.previous = previous

    # def has_next(self):
    #     return self.next is not None
    #
    # def has_previous(self):
    #     return self.previous is not None

class Deque:
    def __init__(self):
        self.head = None
        self.tail = None
        self.previous_node = None
        self.next_node = None
        self.length = 0

    def __initialize_queue(self, value):
        if self.head == None:
            self.head = Node(value, None, None)
            self.tail = self.head
            return True

    def pushleft(self, value):
        self.length += 1
        if self.__initialize_queue(value): return
        self.head.previous = Node(value, self.head, None)
        self.head = self.head.previous

    def pushright(self, value):
        self.length += 1
        if self.__initialize_queue(value): return
        self.tail.next = Node(value, None, self.tail)
        self.tail = self.tail.next

    def popleft(self):
        self.length -= 1
        self.head = self.head.next
        self.head.previous = None

    def popright(self):
        self.length -= 1
        self.tail = self.tail.previous
        self.tail.next = None

    def get_length(self):
        return self.length

    # def get_right(self):
    #     return self.tail.value
    #
    # def get_left(self):
    #     return self.head.value
    #
    # def iterate(self):
    #     current_obj = self.head
    #     while current_obj is not None:
    #         print(current_obj.value)
    #         current_obj = current_obj.next
    #
    # def reverse_iterate(self):
    #     current_obj = self.tail
    #     while current_obj is not None:
    #         print(current_obj.value)
    #         current_obj = current_obj.previous

D = Deque()

D.pushright(2)
D.pushleft(3)
D.pushright(4)
D.pushleft(6)
D.popright()
D.pushleft()

#
# print(D.get_length())
# print(D.get_left())
# print(D.get_right())
#
# D.iterate()
# D.reverse_iterate()