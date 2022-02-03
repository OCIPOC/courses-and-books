'''
    Example1: [a, b, c, a], [b, c]
    - string: a state: {}
    - string ab, state: {b:1}
    - string abc, state: {b:1, c:1}
    - string bc, state: {b:1, c:1}
    - string bca, state: {b:1, c:1}
'''

def create_dict(t: str) -> dict:
    res = {}
    for c in t:
        res[c] = res.get(c, (0,0))
        res[c] = (res[c][0] + 1, 0)
    return res


def is_complete(d: dict) -> bool:
    for x in d.values():
        if x[0] > x[1]:
            return False
    return True


def move_left(s: str, left: int, pattern: dict) -> int:
    while left < len(s):
        if not s[left] in pattern:
            left += 1
        else:
            state = pattern[s[left]]
            if state[1] > state[0]:
                pattern[s[left]] = (state[0], state[1] - 1)
                left += 1
            else:
                break
    return left


def min_window(s: str, t: str) -> str:
    pattern = create_dict(t)
    left, right, res = 0, 0, ''

    while right < len(s):
        if s[right] in pattern:
            pattern[s[right]] = pattern[s[right]][0], pattern[s[right]][1] + 1 

        right += 1
        left = move_left(s, left, pattern)

        if is_complete(pattern):
            if not res or len(res) > right - left:
                res = s[left:right]
    return res


assert min_window('a', 'b') == ''
assert min_window('a', 'a') == 'a'
assert min_window('a', 'aa') == ''
assert min_window('ADOBECODEBANC', 'ABC') == 'BANC'
