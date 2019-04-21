"""771. Jewels and Stones
https://leetcode.com/problems/jewels-and-stones/description/


You're given strings J representing the types of stones that are jewels, and
S representing the stones you have.  Each character in S is a type of stone
you have.  You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are
letters. Letters are case sensitive, so "a" is considered a different type of
stone from "A".

Example 1:


Input: J = "aA", S = "aAAbbbb"
Output: 3


Example 2:


Input: J = "z", S = "ZZ"
Output: 0


Note:


S and J will consist of letters and have length at most 50.
The characters in J are distinct.
"""


class Solution:

    def num_jewels_in_stones(self, j: str, s: str) -> int:
        ans = 0
        for stone in s:
            if stone in j:
                ans += 1
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.num_jewels_in_stones("aA", "aAAbbbb"))
    print(solution.num_jewels_in_stones("z", "ZZ"))
