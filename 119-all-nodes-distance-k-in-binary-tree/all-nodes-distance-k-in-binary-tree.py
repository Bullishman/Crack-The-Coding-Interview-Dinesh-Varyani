# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:

        def getParent(node, parent):
            if node is None:
                return

            parentMap[node] = parent
            getParent(node.left, node)
            getParent(node.right, node)

        def getNodes(node, cnt):
            if not node or node in seen or cnt > k:
                return

            seen.add(node)
            if cnt == k:
                res.append(node.val)

            getNodes(node.left, cnt + 1)
            getNodes(node.right, cnt + 1)
            getNodes(parentMap[node], cnt + 1)

        parentMap = {}
        seen = set()
        res = []
        getParent(root, None)
        getNodes(target, 0)

        return res