
def twoSum(nums: list[int], target: int) -> list[int]:
    
      prev_values = {}

      for i,n in enumerate(nums):
            diff = target - n

            if diff in prev_values:
                return [prev_values[diff], i]
            prev_values[n] = i
      return

input = [2,7,11,15]
target = 9
print(twoSum(input, target))