"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]

Output: true

Explanation:

The element 1 occurs at the indices 0 and 3.

Example 2:

Input: nums = [1,2,3,4]

Output: false

Explanation:

All elements are distinct.

Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]

Output: true

 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109

leetcode link : https://leetcode.com/problems/contains-duplicate/description/

"""

from typing import List 

def contains_duplicate1( nums: List[int]) -> bool:
        
        # time complexity : O(n)
        # space comlexity : o(n)
        
        # create an empty set that will contain elemnts of nums but without duplicates 
        nums_without_duplicates = set()       
        
        # iterate over nums and for each element we check if it exist in our set  
        # if yes this means this element occure more than one time in our array then we return true 
        # if no this means this the first occurence that we found of this element in the list 
        # we goona add it to the set so if there's another occurence of it we gonna find it 
        # if we reach the end of the list and we didn't return the true which means all elemnts are uniq 
        # we return false 

        for num in nums : 
            if num in nums_without_duplicates : 
                return True 
            
            nums_without_duplicates.add( num )

        
        return False 

def conatains_duplicate2( nums: List[int] ) -> bool : 
     
     # time complexity : O(n)
    # space comlexity : o(n)
        
     # assign the list elements to a new set
     # the set will contain just one occurence of our list elements 
     # so if the size of the list equal to the size of the set 
     # that means there's no an element in the list that occur at least twice they are all uniq
     # we return the negation of that 
    
    nums_without_duplicates = set( nums )

    return not (len( nums ) == len( nums_without_duplicates ) )


print ( conatains_duplicate2( [ ]) ) 


