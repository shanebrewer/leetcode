from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numDict = {}
        for i, x in enumerate(nums):
            if numDict.get(x) == None:
                numDict[x] = [i]
            else:
                numDict[x].append(i)
                
        for i, x in enumerate(nums):
            if numDict.get(target - x) != None:
                for j in numDict.get(target - x):
                    if j != i:
                        return list((i, j))
        return

if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([2,7,11,15], 9))
    print(s.twoSum([3, 2, 4], 6))
    print(s.twoSum([3, 3], 6))
    