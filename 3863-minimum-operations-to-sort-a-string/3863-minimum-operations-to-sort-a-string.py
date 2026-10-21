class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)

        # Case 1: Already sorted
        if s == ''.join(sorted(s)):
            return 0

        # Case 2: Length 2 and not sorted
        if n == 2:
            return -1

        mn = min(s)
        mx = max(s)

        # Case 3: Minimum is at the start or maximum is at the end
        if s[0] == mn or s[-1] == mx:
            return 1

        # Case 4: Minimum or maximum occurs in the middle
        if mn in s[1:-1] or mx in s[1:-1]:
            return 2

        # Case 5: Neither extreme occurs in the middle
        return 3