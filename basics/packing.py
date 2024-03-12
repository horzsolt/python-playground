def sumOf(*nums):
    print(type(nums)) #tuple
    print('Our numbers are:', nums)
    return sum(nums)

#print('Adding them up, we get:', sumOf(10, 20, 30))

nums_unpack = [range(2)]
print(type(nums_unpack))
print(nums_unpack)

nums_unpack = [*range(2)]
print(type(nums_unpack))
print(nums_unpack)


