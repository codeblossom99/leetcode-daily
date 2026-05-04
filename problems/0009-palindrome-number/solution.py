#
# @lc app=leetcode id=9 lang=python
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x):
        return str(x) == str(x)[::-1]