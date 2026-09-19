class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        ans = []

        def dfs(i, path):
            if i == len(nums):
                ans.append(path.copy())
                return

            path.append(nums[i])
            dfs(i + 1, path)
            path.pop()

            dfs(i + 1, path)

        dfs(0, [])
        return ans