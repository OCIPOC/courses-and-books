from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    length = 0
    min_len = min([(len(x)) for x in strs])
    for i in range(min_len):
        current = None
        for s in strs:
            if not current:
                current = s[i]
            elif current != s[i]:
                return strs[0][0:length]
                
        length += 1
    
    return strs[0][0:length]


print(longestCommonPrefix(["flower","flow","flight"]))