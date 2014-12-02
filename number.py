from itertools import product

nums = [1, 3, 5, 7, 9, 11, 13, 15]
expected_num = 30
nums_to_add = 5

for combination in product(nums, repeat=nums_to_add):
    print combination, " = ", sum(combination)
