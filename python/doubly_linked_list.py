class DoublyLinkedList:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def append(self, data):
        if self.next:
            self.next.append(data)
        else:
            self.next = DoublyLinkedList(data, prev=self)

    def show_all(self):
        print(self.data, end=' ')
        if self.next:
            self.next.show_all()

    def get_of_index(self, index):  # start - 0 index
        if index:
            return self.next.get_of_index(index - 1)
        else:
            return self.data

    def delete_of_index(self, index):
        if index - 1:
            self.next.delete_of_index(index-1)
        else:
            self.next.next.prev = self
            self.next = self.next.next

    def pop(self, index):
        res = self.get_of_index(index)
        self.delete_of_index(index)
        return res


l = DoublyLinkedList(7)
l.append(4)
l.append(7)
l.append(4)
l.append(2)
l.show_all()
l.delete_of_index(2)
print('')
l.show_all()
l.pop(2)
print('')
l.show_all()
