"""
Problem Statement
Given a root of the binary tree and an integer ‘S’, 
return true if the tree has a path from root-to-leaf 
such that the sum of all the node values of that path 
equals ‘S’. Otherwise, return false.
"""


class TreeNode(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class Solution:
    def hasPath(self, sum, root):
        if root is None:
            return False

        if sum == root.value and root.left is None and root.right is None:
            return True

        return self.hasPath(root.left, sum-root.val) or self.hasPath(root.right, sum-root.val)


class main():
    root = Treenode(5)
    root.left =
    root.right =
    root.left.left =
    root.left.right =
    root.right.left =
    root.right.right =
