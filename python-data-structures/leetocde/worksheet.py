import sys
data = []
for k in range(16):
    data.append(k)
    print('{} {}'.format(len(data), sys.getsizeof(data)))