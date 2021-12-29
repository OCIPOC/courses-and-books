def get_hash_code(s: str) -> str:
    cf = 37
    hash_code, mask = 0, (1 << 32) -1
    for i, v in enumerate(s):
        hash_code = (hash_code + pow(cf, i) * ord(v)) & mask
    return hash_code



