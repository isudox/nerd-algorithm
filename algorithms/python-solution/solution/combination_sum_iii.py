# -*- coding: utf-8 -*-
"""216. Combination Sum III
https://leetcode.com/problems/combination-sum-iii/

Find all possible combinations of k numbers that add up to a number n,
given that only numbers from 1 to 9 can be used and each combination
should be a unique set of numbers.

Note:

All numbers will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]
"""
from typing import List


class Solution:
    def combination_sum3(self, k: int, n: int) -> List[List[int]]:
        candidates = list(range(1, 10))
        ans = []

        def backtrack(target, start, store: List[int]):
            for i in range(start, 9):
                if target < candidates[i]:
                    break

                if len(store) == k - 1:
                    if target < 10:
                        store.append(target)
                        nonlocal ans
                        ans.append(store[:])
                        store.pop()
                    break

                store.append(candidates[i])
                backtrack(target - candidates[i], i + 1, store)
                store.pop()

        backtrack(n, 0, [])
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.combination_sum3(3, 3))
    print(solution.combination_sum3(1, 10))
    print(solution.combination_sum3(2, 6))
    print(solution.combination_sum3(3, 7))
    print(solution.combination_sum3(3, 9))