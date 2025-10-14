
def moveZeroes( nums ) : 

    i = 0 
    
    j = 1 

    for j in range ( 1 , len(nums) ) :

        if nums[i] == 0 : 
            
            if nums[j] != 0 : 
                nums[j] , nums[i] = nums[i] , nums[j]
                i+=1
            
        else : 
               i=+1

nums = [ 0 , 1 , 8 , 0 , 9  , 10  , 11 , 0 , 12 ]
moveZeroes( nums )
print( nums )