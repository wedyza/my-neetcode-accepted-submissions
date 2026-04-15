class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = 1
        zeros_ids = []
        for c, i in enumerate(nums):
            if i == 0:
                zeros_ids.append(c)
                continue
            n *= i
        
        answer = []
        for i in range(len(nums)):
            if i in zeros_ids:
                if len(zeros_ids) > 1:
                    answer.append(0)
                else:
                    answer.append(n)
            else:
                if len(zeros_ids) > 0:
                    answer.append(0)
                else:
                    answer.append(n // nums[i])
        return answer
        
