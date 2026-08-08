class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # countDict = defaultdict(int)
        # for n in nums:
        #     countDict[n] += 1
        # countDict = dict(sorted(countDict.items(), key=lambda item: item[1], reverse=True))
        # result = list(countDict)[:k]
        # print(result)

        # return result 

        count = Counter(nums)

        return [
            num 
            for num, _ in sorted(
                count.items(), 
                key=lambda item:item[1], 
                reverse=True
                )[:k]
        ]           



        