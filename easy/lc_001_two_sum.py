class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums_len = len(nums)

        # Time => O(n^2) Space => O(1)
        # for i in range(nums_len - 1):
        #     for j in range(i + 1, nums_len):
        #         if (nums[i] + nums[j]) == target:
        #             return [i, j]
        
        # Time => O(n) Space => O(n)
        diff_map = {num: index for index, num in enumerate(nums)} 
        
        for index, num in enumerate(nums):
            key = target - num

            target_index = diff_map.get(key)
            if target_index is not None and target_index is not index:
                return [index, target_index]
            
        return []
