class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        char_index_map = {}
        max_length = 0

        for r in range(len(s)):
            if s[r] in char_index_map and char_index_map[s[r]] >= l:
                l = char_index_map[s[r]] + 1
            char_index_map[s[r]] = r
            max_length = max(max_length, r-l+1)
        return max_length