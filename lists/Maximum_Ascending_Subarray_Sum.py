
def maximum_ascending_subarray_sum( nums ) : 

   

    current_sum = nums[0] 
    max_sum = current_sum
    j = 1 


    while j < len( nums ) : 
        if nums[j] <= nums[ j -1 ] : 
            if current_sum > max_sum : 
                max_sum = current_sum 

            current_sum = nums[j]
        else : 
            
            current_sum = current_sum + nums[j]

        j+=1
    
    if current_sum > max_sum : 
       max_sum = current_sum 
    return max_sum


print( maximum_ascending_subarray_sum(  [10,20,30,5,10,50] )) 