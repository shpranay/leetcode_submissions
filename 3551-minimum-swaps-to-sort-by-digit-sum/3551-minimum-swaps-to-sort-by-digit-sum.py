class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def digit_sum(n):
            return sum(int(d) for d in str(n))

        sorted_nums = sorted(nums, key=lambda x: (digit_sum(x), x))
        pos = {num: i for i, num in enumerate(sorted_nums)}

        visited = set()
        swaps = 0

        for i in range(len(nums)):
            if i in visited or pos[nums[i]] == i:
                continue

            cycle_size = 0
            j = i

            while j not in visited:
                visited.add(j)
                j = pos[nums[j]]
                cycle_size += 1

            swaps += cycle_size - 1

        return swaps