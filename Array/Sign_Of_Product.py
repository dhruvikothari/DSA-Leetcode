class Solution:
    def arraySign(self, nums: List[int]) -> int:
        negtv = 0

        for i in nums:
            if(i==0):
                return 0
            if(i<1):
                negtv += 1
            else:
                negtv += 0
        if(negtv % 2 == 0):
            return 1
        else:
            return -1
