class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for idx, val in enumerate(nums):
            required = target - val
            if required not in seen:
                seen[val] = idx
            else:
                return [seen[required], idx]