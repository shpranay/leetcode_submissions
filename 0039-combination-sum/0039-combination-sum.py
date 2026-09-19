class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        ans = []

        def dfs(start, target, path):
            if target == 0:
                ans.append(path.copy())
                return

            if target < 0:
                return

            for i in range(start, len(candidates)):
                path.append(candidates[i])
                dfs(i, target - candidates[i], path)
                path.pop()

        dfs(0, target, [])
        return ans