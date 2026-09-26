class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0 
        window_set = set()
        max_length = 0
        if len(s) <= 1:
            return len(s)
        while r < len(s):
            if s[r] not in window_set:
                window_set.add(s[r])
                if max_length < len(window_set):
                    max_length = len(window_set)
            else:
                while l < len(s) and s[l] != s[r]:
                    window_set.remove(s[l])
                    l += 1
                l += 1
                window_set.add(s[r])
                if max_length < len(window_set):
                    max_length = len(window_set)
            r += 1
        return max_length