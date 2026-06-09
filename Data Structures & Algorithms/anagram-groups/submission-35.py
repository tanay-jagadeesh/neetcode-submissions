class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for s in strs:
            sort_s = tuple(sorted(s))
            result[sort_s].append(s)
        return list(result.values())
        