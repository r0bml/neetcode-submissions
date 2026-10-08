class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for index, value in enumerate(nums):
            required = target - value
            if required not in seen:
                seen[value] = index
            else:
                return [seen[required], index]
            