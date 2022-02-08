
'''
[2,3,1,5] -> [0,1,0,3]
[3,2,1] -> [0,0,0]
'''
def get_mins(lst: list) -> list:
    res = []
    for i in range(len(lst)):
        count = 0
        for j in range(i+1):
            if lst[i] > lst[j]:
                count += 1
        res.append(count)
    return res



assert get_mins([3, 2, 1]) == [0, 0, 0]
assert get_mins([2, 3, 1, 5]) == [0, 1, 0, 3]
