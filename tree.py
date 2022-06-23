
#       root (1000)     depth 1 1000
# 100     200     300         2 100 - 200 - 300
# 110 120                     3 110 - 220 - 330
# (111 115) 121               4 112 - 224 - 336


class Node:
    def __init__(self, data):
        self.data = data
        self.children_nodes = []

    def append(self, data, depth_call=2):
        depth_zero = 0
        data_temp = data
        while data_temp % 10 == 0:
            data_temp = data_temp / 10
            depth_zero += 1

        if depth_call == depth_zero:
            if self.children_nodes:
                for node in self.children_nodes:
                    if node.data <= data <= node.data + 9.99 ** depth_call:
                        return 0
                self.children_nodes.append(Node(data))
            else:
                self.children_nodes.append(Node(data))
        else:
            if self.children_nodes:
                for node in self.children_nodes:
                    if node.data <= data <= node.data + 9.99 ** depth_call:
                        node.append(data, depth_call=depth_call-1)
                    else:
                        self.children_nodes.append(Node(data))
            else:
                self.children_nodes.append(Node(data))

    def show_tree(self):
        print(self.data)
        if self.children_nodes:
            for node in self.children_nodes:
                node.show_tree()

N = Node(1000)

N.append(120)
N.append(140)
N.append(240)
N.append(340)
N.append(440)
N.append(450)

N.show_tree()

