class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        countStr = defaultdict(list) # xu ly missing value
        for s in strs:
            countW = [0] * 26
            for i in s:
                countW[ord(i) - ord('a')] += 1
            key = tuple(countW)
            countStr[key].append(s)

        return list(countStr.values())