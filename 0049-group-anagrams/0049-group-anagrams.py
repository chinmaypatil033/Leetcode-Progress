class Solution(object):
    def groupAnagrams(self, strs):
        anagrams={}

        for word in strs:
            letters=list(word)

            for i in range(len(letters)-1):

                for j in range(len(letters)-i-1):
                    if letters[j]>letters[j+1]:
                        letters[j],letters[j+1]=letters[j+1],letters[j]

            key=""
            for letter in letters:
                key+=letter

            if key not in anagrams:
                anagrams[key]=[]
            anagrams[key].append(word)

        return list(anagrams.values())                         

        