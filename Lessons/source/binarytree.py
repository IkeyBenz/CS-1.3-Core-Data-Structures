#!python
from queue import Queue
from stack import Stack


class BinaryTreeNode(object):

    def __init__(self, data):
        """Initialize this binary tree node with the given data."""
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        """Return a string representation of this binary tree node."""
        return 'BinaryTreeNode({!r})'.format(self.data)

    def is_leaf(self):
        """Return True if this node is a leaf (has no children)."""

        return self.left == self.right == None

    def is_branch(self):
        """Return True if this node is a branch (has at least one child)."""

        return not self.is_leaf()

    def height(self):
        """Return the height of this node (the number of edges on the longest
        downward path from this node to a descendant leaf node).
        Wors case running time: O(n), children and grandchildren (and so on) are all on one side"""

        left, right = 0, 0

        if self.left is not None:
            left = 1 + self.left.height()

        if self.right is not None:
            right = 1 + self.right.height()

        return max(left, right)


class BinarySearchTree(object):

    def __init__(self, items=None):
        """Initialize this binary search tree and insert the given items."""
        self.root = None
        self.size = 0
        if items is not None:
            for item in items:
                self.insert(item)

    def __repr__(self):
        """Return a string representation of this binary search tree."""
        return 'BinarySearchTree({} nodes)'.format(self.size)

    def is_empty(self):
        """Return True if this binary search tree is empty (has no nodes)."""
        return self.root is None

    def height(self):
        """Return the height of this tree (the number of edges on the longest
        downward path from this tree's root node to a descendant leaf node).
        Worst case running time: O(n) Really unbalanced
        Best case running time: O(1) Item is root
        Average case running time: O(log(n))"""
        if self.root.is_branch():
            return self.root.height()

        return 0  # Root has no children

    def contains(self, item):
        """Return True if this binary search tree contains the given item.
        Worst case running time: O(n) Really unbalanced
        Best case running time: O(1) Item is root
        Average case running time: O(log(n))"""

        node = self._find_node_recursive(item, self.root)

        return node is not None

    def search(self, item):
        """Return an item in this binary search tree matching the given item,
        or None if the given item is not found.
        Worst case running time: O(n) Really unbalanced
        Best case running time: O(1) Item is root
        Average case running time: O(log(n))"""

        node = self._find_node_recursive(item, self.root)

        return node.data if node is not None else None

    def insert(self, item):
        """Insert the given item in order into this binary search tree.
        Worst case running time: O(n) Really unbalanced
        Best case running time: O(1) Tree is empty
        Average case running time: O(log(n))"""

        if self.is_empty():
            self.root = BinaryTreeNode(item)
            self.size = 1
            return

        parent = self._find_parent_node_recursive(item, self.root)

        if item < parent.data:
            parent.left = BinaryTreeNode(item)

        elif item > parent.data:
            parent.right = BinaryTreeNode(item)

        self.size += 1

    def _find_node_iterative(self, item):
        """Return the node containing the given item in this binary search tree,
        or None if the given item is not found. Search is performed iteratively
        starting from the root node.
        Worst case running time: O(n) Really unbalanced
        Best case running time: O(1) Item is root
        Average case running time: O(log(n))"""
        # Start with the root node
        node = self.root

        while node is not None:

            if item == node.data:
                return node

            elif item < node.data:
                node = node.left

            elif item > node.data:
                node = node.right

        return None

    def _find_node_recursive(self, item, node):
        """Return the node containing the given item in this binary search tree,
        or None if the given item is not found. Search is performed recursively
        starting from the given node (give the root node to start recursion).
        Worst case running time: O(n) Really unbalanced
        Best case running time: O(1) Item is root
        Average case running time: O(log(n))"""

        if node is None:
            return None

        if node.data == item:
            return node

        if item < node.data:
            return self._find_node_recursive(item, node.left)

        if item > node.data:
            return self._find_node_recursive(item, node.right)

    def _find_parent_node_iterative(self, item):
        """Return the parent node of the node containing the given item
        (or the parent node of where the given item would be if inserted)
        in this tree, or None if this tree is empty or has only a root node.
        Search is performed iteratively starting from the root node.
        Worst case running time: O(n) Really unbalanced
        Best case running time: O(1) Item is root
        Average case running time: O(log(n))"""

        node = self.root
        parent = None

        while node is not None:

            if item == node.data:
                return parent

            elif item < node.data:
                parent = node
                node = node.left

            elif item > node.data:
                parent = node
                node = node.right

        return parent

    def _find_parent_node_recursive(self, item, node, parent=None):
        """Return the parent node of the node containing the given item
        (or the parent node of where the given item would be if inserted)
        in this tree, or None if this tree is empty or has only a root node.
        Search is performed recursively starting from the given node
        (give the root node to start recursion)."""

        if node is None:
            return parent

        if item == node.data:
            return parent

        if item < node.data:
            return self._find_parent_node_recursive(item, node.left, node)

        if item > node.data:
            return self._find_parent_node_recursive(item, node.right, node)

    def delete(self, item):
        """Remove given item from this tree, if present, or raise ValueError.
        TODO: Best case running time: ??? under what conditions?
        TODO: Worst case running time: ??? under what conditions?"""
        # TODO: Use helper methods and break this algorithm down into 3 cases
        # based on how many children the node containing the given item has and
        # implement new helper methods for subtasks of the more complex cases

    def items_in_order(self):
        """Return an in-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree in-order from root, appending each node's item
            self._traverse_in_order_iterative(self.root, items.append)
        # Return in-order list of all items in tree
        return items

    def _traverse_in_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive in-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        Runtime: O(n), assuming visit() is O(1)"""

        if node.left is not None:
            self._traverse_in_order_recursive(node.left, visit)

        visit(node.data)

        if node.right is not None:
            self._traverse_in_order_recursive(node.right, visit)

    def _traverse_in_order_iterative(self, node, visit):
        """Traverse this binary tree with iterative in-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        Runtime: O(n), assuming visit() is O(1)"""
        
        stack = Stack()
        curr_node = node

        while len(stack) > 0 or curr_node:
            if curr_node:
                stack.push(curr_node)
                curr_node = curr_node.left
            else:
                curr_node = stack.pop()
                visit(curr_node.data)
                curr_node = curr_node.right

    def items_pre_order(self):
        """Return a pre-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
                # Traverse tree pre-order from root, appending each node's item
            # self._traverse_pre_order_recursive(self.root, items.append)
            self._traverse_pre_order_iterative(self.root, items.append)
        # Return pre-order list of all items in tree
        return items

    def _traverse_pre_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive pre-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        Runtime: O(n), assuming visit() is O(1)"""
        visit(node.data)
        if node.left is not None:
            self._traverse_pre_order_recursive(node.left, visit)
        if node.right is not None:
            self._traverse_pre_order_recursive(node.right, visit)

    def _traverse_pre_order_iterative(self, node, visit):
        """Traverse this binary tree with iterative pre-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        """
        #				4					stack = [6,]
        #		2				6			out = [4, 2, ]
        #	1		3		5		7

        stack = Stack()
        stack.push(node)

        while len(stack) > 0:
            node = stack.pop()
            visit(node.data)

            if node.right:  # Delay right visit's until after all lefts
                stack.push(node.right)

            if node.left:
                stack.push(node.left)

    def items_post_order(self):
        """Return a post-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree post-order from root, appending each node's item
            self._traverse_post_order_iterative(self.root, items.append)
        # Return post-order list of all items in tree
        return items

    def _traverse_post_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive post-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        Runtime: O(n), assuming visit() is O(1)"""
        if node.left is not None:
            self._traverse_post_order_recursive(node.left, visit)
        if node.right is not None:
            self._traverse_post_order_recursive(node.right, visit)
        visit(node.data)

    def _traverse_post_order_iterative(self, node, visit):
        """Traverse this binary tree with iterative post-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        Running time: O(n) Iterates over each node
        Memory usage: O(n) We are creating a stack"""

        #				4					stack = [6, 4, 3, 2]
        #		2				6			out = []
        #	1		3		5		7		post_order = [ 1, 3, 2, 5, 7, 6, 4 ]

        stack = Stack()
        curr_node = node

        while len(stack) > 0 or curr_node:
   
            while curr_node:
                if curr_node.right:
                    stack.push(curr_node.right)
                
                stack.push(curr_node)
                curr_node = curr_node.left
            
            curr_node = stack.pop()

            if curr_node.right and stack.peek() == curr_node.right:
                stack.pop()
                stack.push(curr_node)
                curr_node = curr_node.right  
                
            else:
                visit(curr_node.data)
                curr_node = None
            



    def items_level_order(self):
        """Return a level-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree level-order from root, appending each node's item
            self._traverse_level_order_iterative(self.root, items.append)
        # Return level-order list of all items in tree
        return items

    def _traverse_level_order_iterative(self, start_node, visit):
        """Traverse this binary tree with iterative level-order traversal (BFS).
        Start at the given node and visit each node with the given function.
        Running time: O(n) It visits each node in the tree."""

        queue = Queue()
        queue.enqueue(start_node)

        while len(queue) > 0:
            node = queue.dequeue()

            visit(node.data)
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)


def test_binary_search_tree():
    # Create a complete binary search tree of 3, 7, or 15 items in level-order
    # items = [2, 1, 3]
    items = [4, 2, 6, 1, 3, 5, 7]
    # items = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]
    print('items: {}'.format(items))

    tree = BinarySearchTree()
    print('tree: {}'.format(tree))
    print('root: {}'.format(tree.root))

    print('\nInserting items:')
    for item in items:
        tree.insert(item)
        print('insert({}), size: {}'.format(item, tree.size))
    print('root: {}'.format(tree.root))

    print('\nSearching for items:')
    for item in items:
        result = tree.search(item)
        print('search({}): {}'.format(item, result))
    item = 123
    result = tree.search(item)
    print('search({}): {}'.format(item, result))

    print('\nTraversing items:')
    print('items in-order:    {}'.format(tree.items_in_order()))
    print('items pre-order:   {}'.format(tree.items_pre_order()))
    print('items post-order:  {}'.format(tree.items_post_order()))
    print('items level-order: {}'.format(tree.items_level_order()))


if __name__ == '__main__':
    test_binary_search_tree()
