def double(x):
    return x * 2

nums = [4, -2, -6, 8, -9, 10]
nums2 = list(map(double, nums))
print(nums2)

nums3 = list(filter(lambda x : x>0, nums))
print(nums3)
