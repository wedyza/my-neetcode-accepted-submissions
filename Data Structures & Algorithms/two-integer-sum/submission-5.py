class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_copy = nums.copy()
        nums_copy = list(map(lambda x: target - x, nums_copy))
        first_index = -1
        second_index = -1
        for c, i in enumerate(nums_copy):
            if i in nums:
                index = nums.index(i)
                if index == c:
                    if nums.count(i) == 1:
                        continue
                    index = nums.index(i, c+1)
                first_index = min(index, c)
                second_index = max(index, c)
                break
        return [first_index, second_index]