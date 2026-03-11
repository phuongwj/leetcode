class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}

        for i in range(len(strs)):
            sort = "".join(sorted(strs[i]))

            if sort not in group.keys():
                group[sort] = [strs[i]]
            else:
                group[sort].append(strs[i])

        ret = []
        for key in group.keys():
            ret.append(group[key])

        return ret