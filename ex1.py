nums = [2,7,11,15]
target = 9

def find(s, n):
# write your implementation here
    for i in range(len(nums)):
        for j in range (i+1, len(nums)):
            if ((nums[i]+nums[j]) == target):
                return [i,j]
    return None

# to test method
result = find(nums, target)
print("Test: {} | Target: {}".format(nums,target))
print("Result: {}".format(result))
