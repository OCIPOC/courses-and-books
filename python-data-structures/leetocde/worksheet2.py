def longest_palindrome(s: str) -> str:
    result = s[0]
    
    def get_longest(s, start, end) -> str:
        res = s[0]
        while start >= 0 and end <= len(s) - 1:
            if s[start] == s[end]:
                res = s[start: end + 1]
                start, end = start - 1, end + 1
            else:
                break
        return res
    
    for start in range(0, len(s)):
        res1 = get_longest(s, start, start + 1)
        res2 = get_longest(s, start, start)
        
        if len(res1) > len(result):
            result = res1
        if len(res2) > len(result):
            result = res2

    return result


print(longest_palindrome('bb'))
