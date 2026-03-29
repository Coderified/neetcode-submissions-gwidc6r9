class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        for words in strs:
            c = [0]*26

            for alphabets in words:

                c[ord(alphabets)-ord("a")]+=1

            d[tuple(c)].append(words)
        return d.values()



        