def findLongestArithmeticProgression1(arr, k):
    """
    Approach:
    - Remove duplicates and use a set for O(1) lookups.
    - For each unique number, move forward by k while next value exists.
    - Track and return the maximum chain length.

    Time complexity:  O(n * L)  (n = unique numbers, L = chain length)
    Space complexity: O(n)      (for the set)
    """
    if not arr: 
        return 0 
    s = set(arr)
    arr = list(s)
    max_subsequence = 1 
    
    for sequence in arr:
        current_sequence = 1
        while (sequence + k) in s:
            current_sequence += 1
            sequence += k
        max_subsequence = max(current_sequence, max_subsequence)
    return max_subsequence 


def findLongestArithmeticProgression2(arr, k):
    """
    Approach:
    - Remove duplicates and sort numbers.
    - For each element, use DP: dp[x] = dp[x - k] + 1 if exists, else 1.
    - Return the maximum length found.

    Time complexity:  O(n log n)  (due to sorting)
    Space complexity: O(n)        (for the dictionary)
    """
    if not arr: 
        return 0 
    
    arr = sorted(set(arr))
    dp = {}

    for element in arr:
        if element - k in dp:
            dp[element] = dp[element - k] + 1
        else:
            dp[element] = 1
              
    return max(dp.values())

print ( findLongestArithmeticProgression2( [8, 1, -1, 0, 3, 6, 2, 4, 5, 7, 9] , 2 ) ) 