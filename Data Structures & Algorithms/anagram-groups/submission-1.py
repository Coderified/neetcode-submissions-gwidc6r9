class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        l1=[]
        i=0
        while i in range(len(strs)):
            words = strs[i]
            l=[]
            l.append(words)
            d1={}
            for letters in words:
                d1[letters] = d1.get(letters,0)+1
            
            nl=strs[i+1:]
            for otherwords in nl:
                if words == otherwords:
                    l.append(otherwords)
                    continue
                d=d1.copy()
                print("d fresh",d)
                print("otherwords",otherwords)
                if len(otherwords)!= len(words):
                    continue
                for letters in otherwords:
                    if letters not in d:
                        continue
                    else:
                        d[letters]-=1
                print("otherwords",otherwords)
                print("d final",d)
                print(d1)
                if set(d.values())=={0}:
                    l.append(otherwords)
                  
            for ws in l:
                strs.remove(ws)

            l1.append(l)
            
        return l1    


        