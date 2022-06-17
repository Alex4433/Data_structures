class LinkedList:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.len = 1

    def append(self, data):
        if self.next:
            self.next.append(data)
        else:
            self.next = LinkedList(data)
        self.len += 1

    def show_all(self):
        print(self.data, end=' ')
        if self.next:
            self.next.show_all()


l = LinkedList(4)
l.append(6)
l.append(5)
l.append(3)
l.append(1)
l.show_all()
