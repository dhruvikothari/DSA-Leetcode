class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]

        for i in range (numRows - 1):
            # in python you can modify the array like this and -1 index takes you to the last element.
            temp = [0] + result[-1] + [0]
            row = []
            for j in range (len(result)+ 1):
                row.append(temp[j] + temp[j+1])
            result.append(row)
        return result
