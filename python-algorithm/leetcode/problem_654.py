"""654. Maximum Binary Tree
https://leetcode.com/problems/maximum-binary-tree/


Given an integer array with no duplicates. A maximum tree building on this
array is defined as follow:

The root is the maximum number in the array.
The left subtree is the maximum tree constructed from left part subarray
divided by the maximum number.
The right subtree is the maximum tree constructed from right part subarray
divided by the maximum number.




Construct the maximum tree by the given array and output the root node of
this tree.


Example 1:

Input: [3,2,1,6,0,5]
Output: return the tree root node representing the following tree:

⁠     6
⁠   /   \
⁠  3     5
⁠   \    /
⁠    2  0
⁠     \
⁠      1



Note:

The size of the given array will be in the range [1,1000].
"""
from typing import List

from common.tree_node import TreeNode


class Solution:

    def construct_maximum_binary_tree(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        max_num = max(nums)
        max_index = nums.index(max_num)
        root = TreeNode(max(nums))
        root.left = self.construct_maximum_binary_tree(nums[:max_index])
        root.right = self.construct_maximum_binary_tree(nums[max_index + 1:])

        return root
