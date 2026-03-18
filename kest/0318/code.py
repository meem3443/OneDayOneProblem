class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def push_front(self, x):
        new_node = Node(x)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.count += 1

    def push_back(self, x):
        new_node = Node(x)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.count += 1

    def pop_front(self):
        if self.head is None:
            return

        value = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self.count -= 1
        print(value)

    def pop_back(self):
        if self.head is None:
            return

        if self.head == self.tail:
            value = self.head.data
            self.head = None
            self.tail = None
            self.count -= 1
            print(value)
            return

        cur = self.head
        while cur.next != self.tail:
            cur = cur.next

        value = self.tail.data
        cur.next = None
        self.tail = cur
        self.count -= 1
        print(value)

    def size(self):
        print(self.count)

    def empty(self):
        if self.count == 0:
            print(1)
        else:
            print(0)

    def front(self):
        if self.head is not None:
            print(self.head.data)

    def back(self):
        if self.tail is not None:
            print(self.tail.data)


N = int(input())
linked_list = LinkedList()

for _ in range(N):
    command = input().split()

    if command[0] == "push_front":
        linked_list.push_front(int(command[1]))

    elif command[0] == "push_back":
        linked_list.push_back(int(command[1]))

    elif command[0] == "pop_front":
        linked_list.pop_front()

    elif command[0] == "pop_back":
        linked_list.pop_back()

    elif command[0] == "size":
        linked_list.size()

    elif command[0] == "empty":
        linked_list.empty()

    elif command[0] == "front":
        linked_list.front()

    elif command[0] == "back":
        linked_list.back()