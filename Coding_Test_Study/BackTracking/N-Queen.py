##https://leetcode.com/problems/n-queens/submissions/?envType=study-plan-v2&envId=top-100-liked

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        def check(x):
            for i in range(x):
                if arr[x] == arr[i] or abs(arr[x] - arr[i]) == x-i:
                    return False
            return True

        def answer(arr):
            a = []
            for i in range(n):
                tmp = ''
                for j in range(n):
                    if arr[i] == j:
                        tmp = tmp + 'Q'
                    else:
                        tmp = tmp + '.'
                a.append(tmp)
            ans.append(a)

        def dfs(x):
            if x == n: 
                answer(arr)
                return 
            for i in range(n):
                if visited[i] == 1:
                    continue
                arr[x] = i
                if check(x):
                    visited[i] = True
                    dfs(x+1)
                    visited[i] = False
                    
        arr = [-1]*n
        visited = [-1]*n
        dfs(0)
        return ans