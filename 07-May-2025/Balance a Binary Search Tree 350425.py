# Problem: Balance a Binary Search Tree - https://leetcode.com/problems/balance-a-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        sortedTree= []

        def inorder(node):
            if node:
                inorder(node.left)
                sortedTree.append(node.val)
                inorder(node.right)
        inorder(root)
        # print(sortedTree)
        def BST(vals):
            if not vals:
                return None
            mid = len(vals)//2
            node = TreeNode(vals[mid])
            node.left = BST(vals[:mid])
            node.right = BST(vals[mid+1:])

            return node
        return BST(sortedTree)
            

