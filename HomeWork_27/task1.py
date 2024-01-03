class Node:
    def __init__(self, value):
        self.value = value
        self.left: Node | None = None
        self.right: Node | None = None

    def __str__(self):
        return f"Node({self.value}, left: {None if self.left is None else self.left.value}, right: {None if self.right is None else self.right.value}) "

    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.value
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.value
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.value
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.value
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


# sorted integer tree
class BinaryTree:
    def __init__(self):
        self.root: Node | None = None

    def insert(self, value: int) -> None:
        self.root = self.__insert_recursive(self.root, value)

    def __insert_recursive(self, root: Node | None, value: int):
        if root is None:
            return Node(value)
        else:
            if value < root.value:
                root.left = self.__insert_recursive(root.left, value)
            else:
                root.right = self.__insert_recursive(root.right, value)
        return root

    def insert_tree(self, other_tree):
        if other_tree.root:
            self.root = self.__insert_tree_recursive(self.root, other_tree.root)

    def __insert_tree_recursive(self, root, other_root):
        if other_root:
            root = self.__insert_recursive(root, other_root.value)
            root.left = self.__insert_tree_recursive(root.left, other_root.left)
            root.right = self.__insert_tree_recursive(root.right, other_root.right)
        return root

    def delete(self, delete_value):
        self.root = self.__delete_recursive(self.root, delete_value)

    def __delete_recursive(self, root, delete_value):
        if root is None:
            return root

        if delete_value < root.value:
            root.left = self.__delete_recursive(root.left, delete_value)
        elif delete_value > root.value:
            root.right = self.__delete_recursive(root.right, delete_value)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp

            elif root.right is None:
                temp = root.left
                root = None
                return temp

            temp = self.min_value_node(root.right)
            root.value = temp.value
            root.right = self.__delete_recursive(root.right, temp.value)
        return root

    def delete_subtree(self, delete_value):
        self.root = self.__delete_subtree_recursive(self.root, delete_value)

    def __delete_subtree_recursive(self, root, delete_value):
        if root is None:
            return root

        if delete_value < root.value:
            root.left = self.__delete_subtree_recursive(root.left, delete_value)
        elif delete_value > root.value:
            root.right = self.__delete_subtree_recursive(root.right, delete_value)
        else:
            root = None  # Deleting the current node and its subtree

        return root

    def min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def search(self, search_value):
        return self.__search_recursive(self.root, search_value)

    def __search_recursive(self, root, search_value):
        if root is None or root.value == search_value:
            return root
        if search_value < root.value:
            return self.__search_recursive(root.left, search_value)
        return self.__search_recursive(root.right, search_value)

    def display(self):
        self.root.display()


some_tree = BinaryTree()
some_tree.insert(3)
some_tree.insert(4)
some_tree.insert(2)
some_tree.insert(10)
some_tree.insert(1)
some_tree.insert(11)
some_tree.insert(9)
# some_tree.__insert_recursive()
some_tree.display()

print(some_tree.search(20))

some_tree.delete(20)

some_tree.display()

bst1 = BinaryTree()
bst1.insert(50)
bst1.insert(30)
bst1.insert(20)
bst1.insert(40)

bst2 = BinaryTree()
bst2.insert(70)
bst2.insert(60)
bst2.insert(80)

print("Before inserting tree")
bst1.display()

bst1.insert_tree(bst2)

print("Tree after inserting another tree:")
bst1.display()


bst1.delete_subtree(30)

print("Tree after deleting subtree:")
bst1.display()