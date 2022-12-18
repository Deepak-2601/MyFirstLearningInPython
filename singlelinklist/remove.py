class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, param):
        pass

    def remove(self):
        pass

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return None
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    def prepend(self, value):
        pass

    def get(self, param):
        pass

    def reverse(self):
        pass

    # def remove(self, index):
    #  if index < 0 or index >= self.length:
    #  return None
    # if index == 0:
    # return self.pop_first
    # if index == self.length - 1:
    #  return self.pop()
    # pre = self.get(index - 1)
    # temp = pre.next
    # pre.next = temp.next
    # temp.next = None
    # self.length -= 1
    # return temp
    def reverse(self):
        temp = self.head
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
            

my_linked_list = LinkedList(11)
my_linked_list.append(3)
my_linked_list.append(23)
my_linked_list.append(7)
my_linked_list.reverse()
print(my_linked_list)
