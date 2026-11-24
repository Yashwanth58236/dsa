"""
# Definition for a Node.
class Node(object):
	def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def postorder(self, root):
        res=[]
        def postorder(root):
            if root is None:
                return []

            for child in root.children:
                postorder(child)

            res.append(root.val)

        postorder(root)
        return res