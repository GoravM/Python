def containsDuplicate(nums: list[int]) -> bool:
        hashset = set()
        for i in nums:
            # already nums[i]
            if i in hashset:
                return True
            hashset.add(i)
        return False

input = [1,2,3,4,5,2]
print(containsDuplicate(nums= input))