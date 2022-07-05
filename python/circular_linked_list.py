class CircularLinkedList:
    __first_item = None
    __last_item = None

    def __init__(self, data, next=None, prev=None):

        CircularLinkedList.__last_item = self

        if not CircularLinkedList.__first_item:
            CircularLinkedList.__first_item = self

        self.data = data
        if next:
            self.next = next
        else:
            self.next = CircularLinkedList.__first_item
        if prev:
            self.prev = prev
        else:
            self.prev = CircularLinkedList.__last_item

    def append(self, data):
        if self.next != CircularLinkedList.__first_item:
            self.next.append(data)
        else:
            self.next = CircularLinkedList(data, None, self)


    def show_all(self):
        print(self.data, end=' ')
        if self.next != CircularLinkedList.__first_item:
            self.next.show_all()


s = CircularLinkedList(3)
s.append(6)
s.append(1)
s.append(9)
s.append(3)
s.show_all()