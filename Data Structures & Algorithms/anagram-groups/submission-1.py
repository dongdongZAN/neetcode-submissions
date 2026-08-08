from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupDict = defaultdict(list)

        for s in strs:
            key = "".join(sorted(s))
            groupDict[key].append(s)
        
        return list(groupDict.values())
            