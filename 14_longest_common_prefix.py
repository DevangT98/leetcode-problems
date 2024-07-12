'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 
Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
'''

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        prefix = strs[0]

        for s in strs:
            if len(s) < len(prefix):
                prefix = s
        print(prefix)

        for s in strs:
            indx_p = 0
            indx_s = 0
            while indx_p < len(prefix) and indx_s < len(s):
                if prefix[indx_p]== s[indx_s]:
                    indx_p+=1
                    indx_s+=1
                else:
                    prefix = prefix[:indx_p]
                    break
        return prefix

sol = Solution()

strs = ["flower","flow","flight"]

print(sol.longestCommonPrefix(strs))