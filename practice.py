
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: TreeNode, result: list = []) -> list[int]:
        if root:
            result.append(root.val)
            self.preorderTraversal(root.left, result)
            self.preorderTraversal(root.right, result)
        return result
    

    def level_order(self, root):
        if not root:
            return []      
        queue = deque([root])
        result = []      
        while queue:
            node = queue.popleft()
            result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)      
        return result

# Helper function to build a tree from a list (for testing)
def build_tree(nodes: list) -> TreeNode:
    """Builds tree from level-order list (LeetCode style input)"""
    if not nodes:
        return None    
    root = TreeNode(nodes[0])
    queue = [root]
    i = 1    
    while queue and i < len(nodes):
        current = queue.pop(0)       
        if nodes[i] is not None:
            current.left = TreeNode(nodes[i])
            queue.append(current.left)
        i += 1      
        if i < len(nodes) and nodes[i] is not None:
            current.right = TreeNode(nodes[i])
            queue.append(current.right)
        i += 1  
    return root


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: [1,null,2,3] (LeetCode example)
    #     1
    #      \
    #       2
    #      /
    #     3
    tree1 = build_tree([1, None, 2, 3])
    print("Recursive:", solution.preorderTraversal(tree1))  # Output: [1, 2, 3]
    
    # Test case 2: Empty tree
    tree2 = build_tree([])
    print("Empty tree:", solution.preorderTraversal(tree2))  # Output: []
    
    # Test case 3: Complete binary tree
    #       1
    #      / \
    #     2   3
    #    / \ / \
    #   4  5 6 7
    tree3 = build_tree([1, 2, 3, 4, 5, 6, 7])
    print("Complete tree:", solution.preorderTraversal(tree3))  # Output: [1, 2, 4, 5, 3, 6, 7]
    print("Level order of 3rd tree:", solution.level_order(tree3)) # [1, 2, 3, 4, 5, 6, 7]
    
    # Test case 4: General Tree
    #     1
    #    / \
    #   2   3
    #    \ /
    #    5 6
    tree4 = build_tree([1, 2, 3, None, 5, 6])
    print("General Tree:", solution.preorderTraversal(tree4))  # Output: [1, 2, 5, 3, 6]
    print("Level order of 4th tree:", solution.level_order(tree4)) # [1, 2, 3, 5, 6]

     # Test accumulation bug
    print("\nTesting accumulation bug:")
    bug_solution = Solution()
    print("First traversal:", bug_solution.preorderTraversal(tree1))  # [1, 2, 3]
    print("Second traversal:", bug_solution.preorderTraversal(tree4))  # Should be [1, 2, 5, 3, 6]