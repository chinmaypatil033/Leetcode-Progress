class Solution(object):
    def groupAnagrams(self, strs):
        anagrams={}
        
        for word in strs:
            count=[0]*26

            for ch in word:
                index=ord(ch)-ord('a')
                count[index]+=1

            key=tuple(count)

            if key not in anagrams:
                anagrams[key]=[]

            anagrams[key].append(word)

        return list(anagrams.values())   