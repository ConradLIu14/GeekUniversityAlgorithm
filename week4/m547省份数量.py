from typing import List
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def find(index: int) -> int:
            if parent[index] != index:
                parent[index] = find(parent[index])
            return parent[index]

        def union(index1: int, index2: int):
            parent[find(index2)] = find(index1)

        provinces = len(isConnected)
        parent = list(range(provinces))

        for i in range(1,provinces):
            for j in range(i):
                if isConnected[i][j] == 1:
                    # print(i,j,parent)
                    union(i, j)
                    # print('...',parent)

        circles = sum(parent[i] == i for i in range(provinces))
        return circles
