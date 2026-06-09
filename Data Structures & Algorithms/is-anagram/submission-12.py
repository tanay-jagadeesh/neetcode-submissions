class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False

        org_s = sorted(s)
        org_t = sorted(t)

        if org_s == org_t: 
            return True
        return False 