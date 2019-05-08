"""47. Permutations II
https://leetcode.com/problems/permutations-ii/

Given a collection of numbers that might contain duplicates,
return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]


[]: []
[1]: [1]
[1,2]: [1, 2], [2, 1]
[1,2,1]: [1,1,2], [1,2,1], [2,1,1]
1,1,2,1,1
"""
import copy
from typing import List


class Solution:

    def permute_unique(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        if length == 0:
            return [[]]
        ans = []
        pre_nums = nums[:-1]
        pre_ans = self.permute_unique(pre_nums)
        is_dup = nums[-1] in pre_nums
        for permutation in pre_ans:
            for i in range(length):
                temp = copy.deepcopy(permutation)
                temp.insert(i, nums[-1])
                if is_dup and ans:
                    if temp in ans:
                        continue
                ans.append(temp)
        return ans
