letters = ''.join(c for c in ['a', 'b', '1'] if c.isalpha())
for c in letters:
    print(c, type(c))

letters[0] = 'a' # wrong, string is immutable