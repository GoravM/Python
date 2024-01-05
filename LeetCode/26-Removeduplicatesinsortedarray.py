
def removeDuplicates(nums):
    new_ar = []
    count = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            new_ar.append(int(nums[i - 1]))
            count  += 1
        # if nums[i] == nums[-1] and nums[-1] != nums[-2]:
        #     new_ar.append(int(nums[-1]))

    return count

input = [0,0,1,1,1,2,2,3,3,4]
# output = [0,1,2,3,4]

print(removeDuplicates(nums= input))