# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not postorder:
            return None


        root_value = postorder.pop()
        root_node = TreeNode(root_value)


        if not postorder:
            return root_node


        left_subtree_root = preorder[1]
        left_subtree_end_index = postorder.index(left_subtree_root)
        
        root_node.left = self.constructFromPrePost(preorder[1:left_subtree_end_index + 2], postorder[:left_subtree_end_index + 1])
        root_node.right = self.constructFromPrePost(preorder[left_subtree_end_index + 2:], postorder[left_subtree_end_index + 1:])
        
        
        return root_node