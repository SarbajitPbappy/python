class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, root, key):
        if root is None:
            return AVLNode(key)
        elif key < root.key:
            root.left = self._insert(root.left, key)
        else:
            root.right = self._insert(root.right, key)

        root.height = 1 + max(self._get_height(root.left), self._get_height(root.right))

        balance = self._get_balance(root)

        if balance > 1 and key < root.left.key:
            return self._rotate_right(root)

        if balance < -1 and key > root.right.key:
            return self._rotate_left(root)

        if balance > 1 and key > root.left.key:
            root.left = self._rotate_left(root.left)
            return self._rotate_right(root)

        if balance < -1 and key < root.right.key:
            root.right = self._rotate_right(root.right)
            return self._rotate_left(root)

        return root

    def _get_height(self, node):
        if node is None:
            return 0
        return node.height

    def _get_balance(self, node):
        if node is None:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def _rotate_left(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y

    def _rotate_right(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y

    def display(self):
        self._display(self.root)

    def _display(self, root):
        if root:
            self._display(root.left)
            print(root.key, end=" ")
            self._display(root.right)


# Creating an AVL tree and inserting the given elements
elements = [17, 11, 7, 53, 4, 12, 8, 60, 16, 20, 55]

avl_tree = AVLTree()
for element in elements:
    avl_tree.insert(element)

# Displaying the AVL tree
print("AVL Tree:")
avl_tree.display()
