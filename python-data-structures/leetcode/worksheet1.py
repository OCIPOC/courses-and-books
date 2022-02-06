def strStr(haystack: str, needle: str) -> int:
    if not needle:
        return 0
    elif not haystack:
        return -1
    else:
        for i in range(len(haystack)):
            if haystack[i: i + len(needle)] == needle:
                return i
        return -1

    