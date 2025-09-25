from typing import List

# space complexity : o(n)
# time complexity : o(n)
#  
def twoSum(self, nums: List[int], target: int) -> List[int]:
    # Dictionary (hashmap) to store numbers we've seen
    # Key = number, Value = index of that number
    value_index = {}
    
    # Loop through the list once → O(n) time
    for index, num in enumerate(nums):
        
        # Calculate the complement (the number we need to reach target)
        complement = target - num
        
        # Check if we've already seen the complement
        if complement in value_index:
            # If yes, return current index and the stored index
            return [index, value_index[complement]]
        
        # Otherwise, store the current number with its index
        value_index[num] = index
    
    # If no solution found (problem statement guarantees one)
    return []


print( twoSum([ 1 , 2 , 2 , 6 , 9 ] , 4 ) ) # test case 