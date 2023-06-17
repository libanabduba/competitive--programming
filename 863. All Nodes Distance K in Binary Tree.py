# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:

        def buildGraph(node, parent, parentMapping):

            if node:
                parentMapping[node] = parent
                buildGraph(node.left, node, parentMapping)
                buildGraph(node.right, node, parentMapping)

        parentMapping = {}

        buildGraph(root, None, parentMapping)

        q = deque([(target, 0)])
        visited = set([target])

        ans = []

        while q:

            node, distance = q.popleft()

            if distance == k:
                ans.append(node.val)

            if distance < k:

                for neigh in [parentMapping[node], node.left, node.right]:
                    if neigh and neigh not in visited:
                        q.append((neigh, distance + 1))
                        visited.add(neigh)


        return ans



        





