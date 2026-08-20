from collections import deque
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        #build dupe
        dupe = [[triangle[0][0]]]

        print(dupe)
        for i in range(1, len(triangle)):
            tmp =[]
            for j in range(len(triangle[i])):
                print(i)
                print(j)
                print()
                if j == 0:
                    tmp.append(dupe[i-1][j])
                elif j == len(triangle[i]) - 1:
                    tmp.append(dupe[i-1][j-1])
                else:
                    mini = min(dupe[i-1][j], dupe[i-1][j-1])
                    tmp.append(mini)
                tmp[-1]+=triangle[i][j]
            dupe.append(tmp)

        return min(dupe[-1])


        