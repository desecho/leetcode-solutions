class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for x in t:
            if s.count(x) != t.count(x):
                return False
        for x in s:
            if s.count(x) != t.count(x):
                return False
        return True
