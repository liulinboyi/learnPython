# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        result = []

        def dfs(self, node, level):
            if not node:
                return
            visted = []
            if node in visted:
                return
            print(node.val)
            try:
                if not result[level]:
                    # result.append([node.val])
                    pass
                else:
                    result[level].append(node.val)
            except IndexError:
                result.insert(level, [node.val])
            dfs(self, node.left, level + 1)
            dfs(self, node.right, level + 1)

        dfs(self, root, 0)
        return result
