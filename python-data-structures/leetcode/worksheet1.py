def eff_sum_array(nums: list, k) -> int:
    dictionary = {0:1}
    prefix_sum = 0
    output = 0
    
    for num in nums:
        print(dictionary, prefix_sum, output, num, nums)
        prefix_sum += num
        output += dictionary.get(prefix_sum - k,0)
        
        if prefix_sum not in dictionary:
            dictionary[prefix_sum] = 1
        else:
            dictionary[prefix_sum] += 1
    return output

assert eff_sum_array([1,-1,0], 0) == 3
        