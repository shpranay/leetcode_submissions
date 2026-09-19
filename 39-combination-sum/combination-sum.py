class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        ans = []

        def dfs(start, target, path):
            if target == 0:
                ans.append(path.copy())
                return

            for i in range(start, len(candidates)):
                if candidates[i] > target:
                    break

                path.append(candidates[i])
                dfs(i, target - candidates[i], path)
                path.pop()

        dfs(0, target, [])
        return ans