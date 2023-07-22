class Node:
    def __init__(self, value, next=None):
        self.next = next
        self.value = value


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        node = self.head
        lr = 'H'
        while node is not None:
            lr += '-->' + str(node.value)
            node = node.next
        return lr

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            node = self.head
            while node.next is not None:
                node = node.next
            node.next = new_node

    def insert(self, value, index):
        new_node = Node(value)
        node = self.head
        for i in range(index):
            if node.next is None:
                print('index does not exist')
                return
            node = node.next

        new_node.next = node.next
        node.next = new_node

    def delete(self, index):
        if self.head is None:
            print('Empty List')
        else:
            node = self.head
            for i in range(index):
                if node.next is None:
                    print('index does not exist')
                    return
                prev_node = node
                node = node.next
            prev_node.next = node.next

    def update(self, value, index):
        if self.head is None:
            print('Empty List')
        else:
            node = self.head
            for i in range(index):
                if node.next is None:
                    print('index does not exist')
                    return
                node = node.next
            node.value = value

    def __len__(self):
        if self.head is None:
            return 0
        else:
            count = 1
            node = self.head
            while node.next is not None:
                node = node.next
                count += 1
            return count

    def reverse(self):
        if self.head is None:
            return
        else:
            prev = None
            current = self.head
            while current is not None:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
            self.head = prev

    def recursive_reverse(self, current):
        if current.next is None:
            self.head = current
            return
        self.recursive_reverse(current.next)
        next_node = current.next
        next_node.next = current
        current.next = None





ll = LinkedList()

ll.append(1)
print(ll)
ll.append(2)
print(ll)
ll.append(3)
print(ll)
ll.insert(9, 2)
print(ll)
ll.append(11)
print(ll)
ll.append(13)
print(ll)
ll.append(14)
print(ll)
ll.update(100,3)
print(ll)

ll.append(1)
print(ll)
ll.append(2)
print(ll)
ll.delete(2)
print(ll)
print(len(ll))
ll.reverse()
print(ll)
ll.recursive_reverse(ll.head)
print(ll)