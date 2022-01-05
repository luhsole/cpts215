class BSTNode:
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.value = val
        self.left = left
        self.right = right
        self.parent = parent
        self.bf = 0

    def __iter__(self):
        if self:
            if self.has_left():
                for elem in self.left:
                    yield elem
            yield self.key
            if self.has_right():
                for elem in self.right:
                    yield elem

    def has_left(self):
        return self.left

    def has_right(self):
        return self.right

    def is_left(self):
        return self.parent and self.parent.left == self

    def is_right(self):
        return self.parent and self.parent.right == self

    def is_root(self):
        return not self.parent

    def is_leaf(self):
        return not (self.right or self.left)

    def has_any(self):
        return self.right or self.left

    def has_both(self):
        return self.right and self.left

    def replace_node_data(self, key, value, lc, rc):
        self.key = key
        self.value = value
        self.left = lc
        self.right = rc
        if self.has_left():
            self.left.parent = self
        if self.has_right():
            self.right.parent = self

    def splice_out(self):
        if self.is_leaf():
            if self.is_left():
                self.parent.left = None
            else:
                self.parent.right = None
        elif self.has_any():
            if self.has_left():
                if self.is_lef():
                    self.parent.left = self.left
                else:
                    self.parent.right = self.left
            else:
                if self.is_left:
                    self.parent.left = self.right
                else:
                    self.parent.right = self.right
                self.right.parent = self.parent

    def find_successor(self):
        succ = None
        if self.has_right():
            succ = self.right.find_min()
        else:
            if self.parent:
                if self.is_left():
                    succ = self.parent
                else:
                    self.parent.right = None
                    succ = self.parent.find_successor()
                    self.parent.right = self
        return succ

    def find_min(self):
        current = self
        while current.has_left():
            current = current.left
        return current


class BST:
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, key):
        return self.get(key)

    def __delitem__(self, key):
        self.delete(key)

    def __contains__(self, key):
        if self._get(key, self.root):
            return True
        else:
            return False

    def put(self, key, value):
        if self.root:
            self._put(key, value, self.root)
        else:
            self.root = BSTNode(key, value)
        self.size += 1

    def _put(self, key, value, current_node):
        if key == current_node.key:
            current_node.value = value
        elif key < current_node.key:
            if current_node.has_left():
                self._put(key, value, current_node.left)
            else:
                current_node.left = BSTNode(key, value, parent=current_node)
        else:
            if current_node.has_right():
                self._put(key, value, current_node.right)
            else:
                current_node.right = BSTNode(key, value, parent=current_node)

    def get(self, key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.value
            else:
                return None
        else:
            return None

    def _get(self, key, current_node):
        if not current_node:
            return None
        elif current_node.key == key:
            return current_node
        elif key < current_node.key:
            return self._get(key, current_node.left)
        else:
            return self._get(key, current_node.right)

    def delete(self, key, current_node):
        if self.size > 1:
            node_to_remove = self._get(key)
            if node_to_remove:
                self.remove(node_to_remove)
                self.size -= 1
            else:
                raise KeyError('Error, key not in tree')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size -= 1
        else:
            raise KeyError('Error, key not in tree')

    def remove(self, current_node):
        if current_node.is_leaf():
            if current_node == current_node.parent.left:
                current_node.parent.left = None
            else:
                current_node.parent.right = None
        elif current_node.has.both():
            succ = current_node.find_successor()
            succ.splice_out()
            current_node.key = succ.key
            current_node.value = succ.value
        else:
            if current_node.has_left():
                if current_node.is_left():
                    current_node.left.parent = current_node.parent
                    current_node.parent.left = current_node.left
                elif current_node.is_right():
                    current_node.left.parent = current_node.parent
                    current_node.parent.right = current_node.left
                else:
                    current_node.replace_node_data(current_node.left.key, current_node.left.value, current_node.left.left, current_node.left.right)
            else:
                if current_node.is_left():
                    current_node.right.parent = current_node.parent
                    current_node.parent.left = current_node.right
                elif current_node.is_right():
                    current_node.right.parent = current_node.parent
                    current_node.parent.right = current_node.right
                else:
                    current_node.replace_node_data(current_node.right.key, current_node.right.value, current_node.right.left, current_node.right.right)

    def in_order_traversal(self):
        if self.size > 0:
            self.in_order_helper(self.root)
            print()
        else:
            print("Empty tree")

    def in_order_helper(self, current_node):
        if current_node is not None:
            self.in_order_helper(current_node.left)
            print(str(current_node.key) + ":" + str(current_node.value), end=" ")
            self.in_order_helper(current_node.right)


class AVLTree(BST):
    def __init__(self):
        super(AVLTree, self).__init__()

    def _put(self, key, value, current_node):
        if key == current_node.key:
            current_node.value = value
        elif key < current_node.key:
            if current_node.has_left():
                self._put(key, value, current_node.left)
            else:
                current_node.left = BSTNode(key, value, parent=current_node)
                self.update_balance(current_node.left)
        else:
            if current_node.has_right():
                self._put(key, value, current_node.right)
            else:
                current_node.right = BSTNode(key, value, parent=current_node)
                self.update_balance(current_node.right)

    def update_balance(self, node):
        if node.bf > 1 or node.bf < -1:
            self.rebalance(node)
            return

        if node.parent is not None:
            if node.is_left():
                node.parent.bf += 1
            elif node.is_right():
                node.parent.bf -= 1

            if node.parent.bf != 0:
                self.update_balance(node.parent)

    def rebalance(self, node):
        if node.bf < 0:
            if node.right.bf > 0:
                self.rotate_right(node.right)
                self.rotate_left(node)
            else:
                self.rotate_left(node)
        elif node.bf > 0:
            if node.left.bf < 0:
                self.rotate_left(node.left)
                self.rotate_right(node)
            else:
                self.rotate_right(node)

    def rotate_left(self, rot_root):
        new_root = rot_root.right
        rot_root.right = new_root.left
        if new_root.left is not None:
            new_root.left.parent = rot_root
        new_root.parent = rot_root.parent
        if rot_root.is_root():
            self.root = new_root
        else:
            if rot_root.is_left():
                rot_root.parent.left = new_root
            else:
                rot_root.parent.right = new_root
        new_root.left = rot_root
        rot_root.parent = new_root
        rot_root.bf = rot_root.bf + 1 - min(new_root.bf, 0)
        new_root.bf = rot_root.bf + 1 + max(rot_root.bf, 0)

    def rotate_right(self, rot_root):
        new_root = rot_root.left
        rot_root.left = new_root.right
        if new_root.right is not None:
            new_root.right.parent = rot_root
        new_root.parent = rot_root.parent
        if rot_root.is_root():
            self.root = new_root
        else:
            if rot_root.is_right():
                rot_root.parent.right = new_root
            else:
                rot_root.parent.left = new_root
        new_root.right = rot_root
        rot_root.parent = new_root
        rot_root.bf = rot_root.bf - 1 - max(new_root.bf, 0)
        new_root.bf = new_root.bf - 1 + min(rot_root.bf, 0)

    def delete(self, key):
        # if key is in tree
        if key in self:
            # find node with the key
            if self.size > 1:
                node_to_remove = self._get(key, self.root)
            # remove the node
                if node_to_remove:
                    self.remove(node_to_remove)
                    self.size -= 1
                    return True
                else:
                    raise KeyError('Error, key not in tree')
            elif self.size == 1 and self.root.key == key:
                self.root = None
                self.size -= 1
                return True
            else:
                raise KeyError('Error, key not in tree')
        return False

    def remove(self, node):
        if node.is_leaf(): # node has no child
            if node == node.parent.left:
                node.parent.left = None
            else:
                node.parent.right = None
            # self.update_balance_delete(node)
        elif node.has_both(): # node has 2 children
            succ = node.find_successor()
            succ.splice_out()
            node.key = succ.key
            node.value = succ.value
            # self.update_balance_delete(node)
        else: # node has 1 child
            if node.has_left():
                if node.is_left():
                    node.left.parent = node.parent
                    node.parent.left = node.left
                    # node.parent.left = node.right
                elif node.is_right():
                    node.left.parent = node.parent
                    node.parent.right = node.left
                    # node.parent.right = node.right
                else:
                    node.replace_node_data(node.left.key, node.left.value, node.left.left, node.left.right)
                # self.update_balance_delete(node)
            else: # node.has_right()
                if node.is_left():
                    node.right.parent = node.parent
                    node.parent.left = node.right
                    # node.parent.left = node.left
                elif node.is_right():
                    node.right.parent = node.parent
                    node.parent.right = node.right
                    # node.parent.right = node.left
                else:
                    node.replace_node_data(node.right.key, node.right.value, node.right.left, node.right.right)
                # self.update_balance_delete(node)
        self.update_balance_delete(node)

    def update_balance_delete(self, node):
        if node.bf > 1 or node.bf < -1:
            self.rebalance(node)
            return

        if node.parent is not None:
            if node.is_left():
                node.parent.bf += 1
            elif node.is_right():
                node.parent.bf -= 1

            if node.parent.bf > 1 or node.parent.bf < -1:
                self.rebalance(node)
                self.update_balance_delete(node.parent.parent)
            elif node.parent.bf != 0:
                return
            else:
                self.update_balance_delete(node.parent)


    def in_order_helper(self, current_node):
        if current_node is not None:
            self.in_order_helper(current_node.left)
            print(str(current_node.key) + ":" + str(current_node.value) + "(%d)" % current_node.bf, self.in_order_helper(current_node.right))

    def level_order_traversal(self):
        if self.size > 0:
            queue = [str(self.root.key) + ":" + str(self.root.value) + "(%d)" % self.root.bf, "\n"]
            self.level_order_helper(self.root, queue)
            for data in queue:
                print(data, end="")
            print()
        else:
            print("Empty tree")

    def level_order_helper(self, node, queue):
        if node is not None:
            if node.left is not None:
                temp = node.left
                queue.append(str(temp.key) + ":" + str(temp.value) + "(%d)" % temp.bf)
            if node.right is not None:
                temp = node.right
                queue.append(str(temp.key) + ":" + str(temp.value) + "(%d)" % temp.bf)
            queue.append("\n")
            self.level_order_helper(node.left, queue)
            self.level_order_helper(node.right, queue)


def main():
    mytree = AVLTree()
    mytree[9]="CptS_450"
    mytree[8]="CptS_415"
    mytree[7]="CptS_315"
    mytree[6]="CptS_215"
    mytree[5]="CptS_132"
    mytree[4]="CptS_131"
    mytree[3]="CptS_122"
    mytree[2]="CptS_121"
    mytree[1]="CptS_115"
    mytree.level_order_traversal()

    mytree.delete(5)
    mytree.delete(6)
    mytree.level_order_traversal()


main()
