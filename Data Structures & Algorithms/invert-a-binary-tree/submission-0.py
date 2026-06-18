# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
#recursive approach
#uses DFS
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        curr = root
        #base case if tree has no nodes
        if curr == None:
            return curr
        temp = curr.left
        curr.left = curr.right
        curr.right = temp

        self.invertTree(curr.left)
        self.invertTree(curr.right)

        return curr