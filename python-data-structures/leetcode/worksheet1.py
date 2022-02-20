a = '0111'
b = '01'


max_len = max(len(a), len(b))
print(max_len)
a, b = a.zfill(max_len), b.zfill(max_len)
print(a, b)


