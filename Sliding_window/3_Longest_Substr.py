class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = res = 0
        freq = set()
        for right in range(len(s)):
            while s[right] in freq:
                freq.remove(s[left])
                left+=1
            freq.add(s[right])
            res = max(res, right - left + 1)
        return res