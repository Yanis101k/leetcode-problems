def mergeHighDefinitionIntervals(intervals):
    
    # empty array 
    if not intervals : 
        return []
    
    # sort the intervals using the begin valeu of each interval 
    intervals.sort(key=lambda x: x[0])

    non_overlappingg_intervals = [] 
    begin = intervals[0][0]
    end = intervals[0][1]
    
    for index  in range( 1 , len(intervals )) :
        # if the end of our previous interval end is greater or equal than the begin of current interval 
        # we merge this interval and select the greater end between prev and current interval 
        if end >= intervals[index][0] : 
           end = max ( intervals[index][1] , end ) 

        else : 
            # if the end of our previous interval end is less than begin of current interval 
            # we add the previous interval to the list and start building a new interval with new begin and end 

            non_overlappingg_intervals.append( [ begin , end ] )
            begin = intervals[index][0]
            end = intervals[index][1]

    non_overlappingg_intervals.append( [ begin , end ] )
    return non_overlappingg_intervals
    
    # space complexity : O(N) N equal to legth of our inputed list 
    # in case where all our intervals don't overlap we need an output that wil have the langth of input N
    # time complixity : O(N log(N) ) N equal to legth of our inputed list 
    # the sorting of the list is ( N log(N) ) 


intervals =  [ [5,5]] 


print( mergeHighDefinitionIntervals(intervals) )