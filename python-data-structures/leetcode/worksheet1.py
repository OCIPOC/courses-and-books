def isAlienSorted(self, words: list, order: str) -> bool:         
    order_map = dict([(v,i) for (i,v) in enumerate(words)])        
    
    def compare(x, y) -> int:
        for i in range(len(x)):
            if i > len(y) - 1:
                break
            elif order_map[x[i]] > order_map[y[i]]:
                return 1
            elif order_map[x[i]] < order_map[y[i]]:
                return -1
        
        if len(x) > len(y):
            return 1
        elif len(x) < len(y):
            return -1
        else:
            return 0
        

    sorted_w = sorted(words, cmp=compare)
    
    for i in range(len(words)):
        if words[i] != sorted_w[i]:
            return False
    
    return True