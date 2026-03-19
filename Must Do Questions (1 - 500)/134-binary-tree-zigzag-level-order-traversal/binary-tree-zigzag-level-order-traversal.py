# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        dic = defaultdict(list)

        def dfs(node: Optional[TreeNode], lvl: int) -> None:
            if not node:
                return None

            dic[lvl].append(node.val)
            if node.left:
                dfs(node.left, lvl+1)
            if node.right:
                dfs(node.right, lvl+1)
        
        dfs(root, 0)

        return [values[::-1] if idx % 2 != 0 else values for idx, values in dic.items()]