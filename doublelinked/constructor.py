class Nodes:
    def __init__(self, values):
        self.values = values
        self.forwards = None
        self.back = None


class DoubleLinkedList:
    def __init__(self, values):
        new_nodes = Nodes(values)
        self.heads = new_nodes
        self.tails = new_nodes
        self.lengths = 1

    def append(self, values):
        new_nodes = Nodes(values)
        if self.heads is None:
            self.heads = new_nodes
            self.tails = new_nodes
        else:
            self.tails.forwards = new_nodes
            new_nodes.back = self.tails
            self.tails = new_nodes
        self.lengths = +1
        return True

    def pop(self):
        if self.lengths == 0:
            return None
        tempo = self.tails
        if self.lengths == 1:
            self.heads = None
            self.tails = None
        else:
            self.tails = self.tails.back
            self.tails.forwards = None
            tempo.back = None
        self.lengths -= 1
        return tempo

    def print_List(self):
        tempo = self.heads
        while tempo is not None:
            print(tempo.values)
            tempo = tempo.forwards


Linked_list = DoubleLinkedList(5)
Linked_list.append(3)

print(Linked_list.print_List())
