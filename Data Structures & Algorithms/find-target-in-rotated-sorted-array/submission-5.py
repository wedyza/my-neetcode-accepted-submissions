class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l) // 2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        return l, l - 1

    def search(self, nums: List[int], target: int) -> int:
        smallest, biggest = self.findMin(nums)
        ltb = nums[:biggest+1]
        stb = nums[smallest:]
        print(smallest, biggest)
        print(ltb)
        print(stb)
        if len(ltb) > 0 and target >= ltb[0]:
            main = ltb
            c = 0
        else:
            main = stb
            c = len(ltb)
        print(main)
        l, r = 0, len(main) - 1
        while l <= r:
            middle = (l + r) // 2
            if main[middle] == target:
                return middle + c
            elif main[middle] < target:
                l = middle + 1
            else:
                r = middle - 1
        return -1