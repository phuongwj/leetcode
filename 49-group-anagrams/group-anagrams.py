class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        group = []

        for i in range(len(strs)):
            sorted_string = ''.join(sorted(strs[i]))
            if sorted_string not in anagrams.keys():
                array = []
                array.append(strs[i])
                anagrams[sorted_string] = anagrams.get(sorted_string, array)
            else:
                anagrams.get(sorted_string).append(strs[i])
        
        for i in anagrams.values():
            group.append(i)

        return group