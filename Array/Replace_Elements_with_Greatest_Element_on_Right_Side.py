class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
            rightmxm = -1
            for i in range(len(arr)-1, -1,-1):
                newmxm = max(rightmxm, arr[i])
                arr[i]= rightmxm
                rightmxm = newmxm
            return arr
