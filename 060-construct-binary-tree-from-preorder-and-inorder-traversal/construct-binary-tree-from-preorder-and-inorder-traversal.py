# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if inorder:																	
            inorder_index = inorder.index(preorder.pop(0))				
            root = TreeNode(inorder[inorder_index])																
            root.left = self.buildTree(preorder, inorder[:inorder_index])
            root.right = self.buildTree(preorder, inorder[inorder_index + 1:])																		                                               
            return root