import random

class Node:

    def __init__(self, data, root=True):
        self.root = root
        self.data = data
        self.left = None
        self.right = None

    def append(self, data):
        if self.__sort_condition(data):
            if self.right:
                self.right.append(data)
            else:
                self.right = Node(data, root=False)
        else:
            if self.left:
                self.left.append(data)
            else:
                self.left = Node(data, root=False)

    def __sort_condition(self, data):
        return data > self.data

    def print_all(self):
        print(self.data, end=' ')
        if self.left:
            self.left.print_all()

        if self.right:
            self.right.print_all()

    def check_having_element(self, el):
        if self.data != el:
            if self.__sort_condition(el):
                if self.right:
                    return self.right.check_having_element(el)
                else:
                    return False
            else:
                if self.left:
                    return self.left.check_having_element(el)
                else:
                    return False
        else:
            return True


d = Node(random.randrange(100, 1000))
list_of_number = []


for _ in range(5_000):
    a = random.randrange(-500, 1000)
    d.append(a)
    list_of_number.append(a)


a = d.check_having_element(list_of_number[9])
print(a)
