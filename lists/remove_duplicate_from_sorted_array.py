from typing import List
def removeDuplicates( nums: List[int]) -> int:
        
        k = len( nums )
        if k == 1 : 
            return 1 
        
        index1 = 0 
        index2 = 1 

        while index2 < k : 
            if nums[index1] == nums[index2] : 
                nums[index2] = "_"
            else : 
                index1 = index2 

            index2 = index2 + 1 

        index1 = 1 
        index2 = 1
        while index2 < len( nums ) : 

            
            if nums[ index1 ] == '_' and nums[index2] != '_':
                nums[index1] = nums[index2]
                nums[index2] = '_'
                index1 = index1 + 1
               
            else : 
                if nums[ index1 ] != '_' : 
                    index1 = index1 + 1 
            
            index2 = index2 + 1
        k = 1       
        while nums[ k ] != "_" and k < len( nums ) : 
            k = k + 1
        
        return k 
   

def removeDuplicates1( nums: List[int]) -> int:
        
      i = 0 
      j = 1 
      while j < len(nums) : 
           
           if nums[i] != nums[j] : 
                i = i + 1 
                nums[i] = nums[j]
           j = j + 1  
      return i + 1 


nums = [ 1 , 1 , 2 ]

k = removeDuplicates1( nums )
print(  k )
print(nums[: k ])