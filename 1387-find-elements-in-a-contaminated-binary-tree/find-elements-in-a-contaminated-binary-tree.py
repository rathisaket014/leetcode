# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.treeSet = set()
        if root:
            self.bfs(root)
        
    def bfs(self, root: TreeNode):
        queue = deque([root])
        root.val = 0

        while queue:
            node = queue.popleft()
            x = node.val
            self.treeSet.add(x)

            if node.left:
                node.left.val = 2 * x + 1
                queue.append(node.left)
            if node.right:
                node.right.val = 2 * x + 2
                queue.append(node.right)

    def find(self, target: int) -> bool:
        return target in self.treeSet


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)