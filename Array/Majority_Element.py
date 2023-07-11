class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = {}
        result, maxcnt = 0,0

        for n in nums:
            cnt[n] = 1 + cnt.get(n, 0)
            if cnt[n]>maxcnt:
                result = n
            else:
                result
            maxcnt = max(cnt[n], maxcnt)
        return result
