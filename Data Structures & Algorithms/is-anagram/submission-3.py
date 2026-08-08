class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ##################solution1##################
        # return sorted(s) == sorted(t)

        ##################solution2##################
        if len(s) != len(t):
            return False
        
        # count = {}
        # for char in s:
        #     count[char] = count.get(char,0) + 1
        count = defaultdict(int)
        for char in s:
            count[char] += 1
        
        for char in t:
            if char not in count:
                return False
            
            count[char] -= 1
            if count[char] < 0:
                return False

        return True

        ##################solution3##################
        # return Counter(s) == Counter(t)


        