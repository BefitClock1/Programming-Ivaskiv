class Node:
    def __init__(self, value, priority, color="red"):
        self.value = value
        self.priority = priority
        self.color = color  
        self.left = None
        self.right = None
        self.parent = None


class que:
    def __init__(self):
        self.root = None

    def insert(self, value, priority):
        n_node = Node(value, priority)
        if self.root is None:
            self.root = n_node
            self.root.color = "black"
            return

        parent = None
        curent = self.root
        while curent is not None:
            parent = curent
            if priority < curent.priority:
                curent = curent.right
            else:
                curent = curent.left

        n_node.parent = parent
        if priority > parent.priority:
            parent.left = n_node
        else:
            parent.right = n_node

        while n_node != self.root and n_node.parent.color == "red":
            parent = n_node.parent
            grandparent = parent.parent
            if parent == grandparent.left:
                uncle = grandparent.right
                if uncle and uncle.color == "red":
                    parent.color = "black"
                    uncle.color = "black"
                    grandparent.color = "red"
                    n_node = grandparent
                else:
                    if n_node == parent.right:
                        n_node = parent
                        self.rotate_left(n_node)
                    parent.color = "black"
                    grandparent.color = "red"
                    self.rotate_right(grandparent)
            else:
                uncle = grandparent.left
                if uncle and uncle.color == "red":
                    parent.color = "black"
                    uncle.color = "black"
                    grandparent.color = "red"
                    n_node = grandparent
                else:
                    if n_node == parent.left:
                        n_node = parent
                        self.rotate_right(n_node)
                    parent.color = "black"
                    grandparent.color = "red"
                    self.rotate_left(grandparent)
        self.root.color = "black"

    def rotate_left(self, node):
        new_parent = node.right
        node.right = new_parent.left
        if new_parent.left:
            new_parent.left.parent = node
        new_parent.parent = node.parent
        if node.parent is None:
            self.root = new_parent
        elif node == node.parent.left:
            node.parent.left = new_parent
        else:
            node.parent.right = new_parent
        new_parent.left = node
        node.parent = new_parent

    def rotate_right(self, node):
        new_parent = node.left
        node.left = new_parent.right
        if new_parent.right:
            new_parent.right.parent = node
        new_parent.parent = node.parent
        if node.parent is None:
            self.root = new_parent
        elif node == node.parent.right:
            node.parent.right = new_parent
        else:
            node.parent.left = new_parent
        new_parent.right = node
        node.parent = new_parent

    def get_max_priority(self):
        if self.root is None:
            return None
        curent = self.root
        while curent.left is not None:
            curent = curent.left
        return curent.priority

    def del_max_priority(self):
        if self.root is None:
            return None
        curent = self.root
        while curent.left is not None:
            curent = curent.left
        value = curent.value
        self.delete_node(curent)
        return value

    def delete_node(self, node):
        if node.left is None and node.right is None:
            if node == self.root:
                self.root = None
            elif node == node.parent.left:
                node.parent.left = None
            else:
                node.parent.right = None
        elif node.left is None:
            if node == self.root:
                self.root = node.right
            elif node == node.parent.left:
                node.parent.left = node.right
            else:
                node.parent.right = node.right
            node.right.parent = node.parent
        elif node.right is None:
            if node == self.root:
                self.root = node.left
            elif node == node.parent.left:
                node.parent.left = node.left
            else:
                node.parent.right = node.left
            node.left.parent = node.parent
        else:
            successor = node.right
            while successor.left is not None:
                successor = successor.left
            node.value = successor.value
            node.priority = successor.priority
            self.delete_node(successor)

    def show_queue(self):
        def inorder(node):
            if node is not None:
                inorder(node.left)
                print(f"Value: {node.value}, Priority: {node.priority}, Color: {node.color}")
                inorder(node.right)
        inorder(self.root)
