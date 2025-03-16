class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if s == None or len(s) == 0:
            return 0

        Max = 0
        slow = 0
        map = dict()

        for i in range(len(s)):
            c = s[i]

            if c in map and map[c] >= slow:
                slow = map[c] + 1
            map[c] = i
            Max = max(Max, i - slow +1)

        return Max    

        