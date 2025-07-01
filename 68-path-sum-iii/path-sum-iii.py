# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix_sum_counts = defaultdict(int)
        prefix_sum_counts[0] = 1

        def dfs(root, current_path_sum):
            count = 0
            if root:
                current_path_sum += root.val
                count = prefix_sum_counts[current_path_sum-targetSum]

                prefix_sum_counts[current_path_sum] += 1
                count += dfs(root.left, current_path_sum) + dfs(root.right, current_path_sum)
                prefix_sum_counts[current_path_sum] -= 1

            return count

        return dfs(root, 0)