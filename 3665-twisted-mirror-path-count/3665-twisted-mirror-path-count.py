class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        dp = [[[0, 0] for _ in range(n)] for _ in range(m)]
        dp[0][0][0] = 1  # start counted once

        for i in range(m):
            for j in range(n):
                r, d = dp[i][j]      # arrived moving right / moving down
                if r == 0 and d == 0:
                    continue

                if grid[i][j] == 0:
                    total = (r + d) % MOD
                    if j + 1 < n:
                        dp[i][j + 1][0] = (dp[i][j + 1][0] + total) % MOD
                    if i + 1 < m:
                        dp[i + 1][j][1] = (dp[i + 1][j][1] + total) % MOD
                else:
                    # mirror: entered moving right -> goes down
                    if i + 1 < m:
                        dp[i + 1][j][1] = (dp[i + 1][j][1] + r) % MOD
                    # mirror: entered moving down -> goes right
                    if j + 1 < n:
                        dp[i][j + 1][0] = (dp[i][j + 1][0] + d) % MOD

        if grid[m - 1][n - 1] == 1:
            return 0
        return (dp[m - 1][n - 1][0] + dp[m - 1][n - 1][1]) % MOD