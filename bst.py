class Node:

    def __init__(self, key, val, N):
        self.key = key
        self.val = val
        self.N = N
        self.left = None
        self.right = None

class BST:

    def __init__(self):
        self.root = None

    def size(self):
        return self._size(self.root)

    def _size(self, x):
        if x is None:
            return 0

        return x.N

    def get(self, key):
        return self._get(self.root, key)

    def _get(self, x, key):
        if x is None:
            return

        if x.key > key:
            return self._get(x.left, key)
        elif x.key < key:
            return self._get(x.right, key)
        else:
            return x.val

    def put(self, key, val):
        self.root = self._put(self.root, key, val)

    def _put(self, x, key, val):
        if x is None:
            return Node(key, val, 1)
        if x.key > key:
            x.left = self._put(x.left, key, val)
        elif x.key < key:
            x.right = self._put(x.right, key, val)
        else:
            x.val = val
        x.N = self._size(x.left) + self._size(x.right) + 1
        return x

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, x, key):
        if x is None:
            return None

        if x.key > key:
            x.left = self._delete(x.left, key)
        elif x.key < key:
            x.right = self._delete(x.right, key)
        else:
            if x.right is None:
                return x.left
            if x.left is None:
                return x.right
            t = x
            x = self._min(t.right)
            x.right = self._deleteMin(t.right)
            x.left = t.left

        x.N = self._size(x.left) + self._size(x.right) + 1
        return x

    def delete_min(self):
        self.root = self._deleteMin(self.root)

    def _deleteMin(self, x):
        if x.left is None:
            return x.right
        x.left = self._deleteMin(x.left)
        x.N = self._size(x.left) + self._size(x.right) + 1
        return x

    def is_empty(self):
        return self.root is None

    def in_order(self):
        return self._inorder(self.root)

    def _inorder(self, root):
        if root is None:
            return []

        return self._inorder(root.left) + [root.key]+self._inorder(root.right)


if __name__ == '__main__':
    st = BST()

    for key in "ighmqlcaz".upper():
        st.put(key, ord(key) - ord('A'))

    print(st.in_order())
