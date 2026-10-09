class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for index, value in enumerate(nums):
            required = target - value
            if required not in seen:
                seen[value] = index
            else:
                return [seen[required], index]
                
        
        