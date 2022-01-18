def len_distinct(s: str) -> int:
    chars = {}
    max_len, start, current = 0, 0, 0
    while current < len(s):
        chars[s[current]] = current
        if len(chars) > 2:
            min_item = min([x for x in chars.items()], key=lambda x: x[1])
            del chars[min_item[0]]
            start = min_item[1] + 1
        if max_len < (current - start) + 1:
            max_len = (current-start) + 1
        current +=1
    return max_len

print(len_distinct("eceba"))
# print(len_distinct("ccaabbb"))
