class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        freq = {}

        for i in nums:
            if i in freq:
                count += freq[i]
                freq[i] += 1
            else:
                freq[i] = 1
        return count