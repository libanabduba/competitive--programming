class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:


        q = deque([([0,0,0,0], 0)])

        visited = set([(0,0,0,0)])

        deadends = set(deadends)

        if target in deadends or "0000" in deadends:
            return -1


        while q:

            node, path_count = q.popleft()

            # print(tuple(node))

            temp = "".join(list(map(str, node)))
            # print(temp)

            if temp == target:
                return path_count

            for i in range(4):
                node_copy = node[::]
                node_copy_2 = node[::]
                node_copy[i] += 1
                node_copy_2[i] -= 1
                if node_copy[i] > 9: node_copy[i] = 0

                if node_copy_2[i] < 0: node_copy_2[i] = 9

                if "".join(list(map(str, node_copy))) not in deadends and tuple(node_copy) not in visited:
                    q.append((node_copy, path_count + 1))
                    visited.add(tuple(node_copy))

                if "".join(list(map(str, node_copy_2))) not in deadends and tuple(node_copy_2) not in visited:
                    q.append((node_copy_2, path_count + 1))
                    visited.add(tuple(node_copy_2))

                

        return -1

