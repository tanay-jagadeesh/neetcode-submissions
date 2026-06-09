class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)

        if n1 > n2:
            return False

        count1 = {}
        count2 = {}

        for i in range(n1):
            count1[s1[i]] = 1 + count1.get(s1[i], 0)
            count2[s2[i]] = 1 + count2.get(s2[i], 0)

        if count1 == count2:
            return True

        for i in range(n1, n2):
            count2[s2[i]] = 1 + count2.get(s2[i], 0)
            count2[s2[i - n1]] -= 1
            if count2[s2[i - n1]] == 0:
                del count2[s2[i - n1]]
            if count1 == count2:
                return True

        return False
            
        
