class Solution(object):
    def strStr(self, haystack, needle):
        return 0 if len(needle) < 1 else haystack.find(needle)