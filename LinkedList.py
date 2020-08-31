class Node:

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:

    def __init__(self):
        self.head = None

    def add(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)

    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

    def insert(self, target, data):
        node = self.head
        while node.next:
            node = node.next
            if node.data == target:
                temp = node.next
                node.next = Node(data)
                node.next.next = temp
            else:
                ("No node")

    def delete(self, data):
        if self.head == None:
            print('No node')
            return

        if self.head.data == data:
            if self.head.next:
                temp = self.head
                self.head = temp.next
                del temp
        else:
            node = self.head
            while node.next:
                if node.next.data == data:
                    temp = node.next
                    node.next = temp.next
                    del temp
                    return
                else:
                    node = node.next

            print("No such node")
