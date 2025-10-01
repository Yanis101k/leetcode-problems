from typing import List 

def productExceptSelf( nums: List[int]) -> List[int]:
    """
    Approach:
    ----------
    The goal is to compute an output array such that:
    output[i] = product of all elements in nums except nums[i],
    without using division, and in O(n) time.

    Idea:
    - Use prefix and suffix products.
    - First pass (left to right): store product of all elements to the left of each index.
    - Second pass (right to left): multiply with product of all elements to the right of each index.
    - This way, each position gets product_except_self = prefix_product * suffix_product.

    Time Complexity:
    - O(n): Two linear passes (left-to-right and right-to-left).
    - Each pass visits every element once.

    Space Complexity:
    - O(1) extra space (ignoring output array `res`).
    - We only store two integers (`left` and `right`) for prefix and suffix products.
    """

    n = len(nums)                  # Length of input array
    res = [1] * n                  # Initialize result array with 1s (will store final answer)
    
    # -----------------------------
    # First pass: compute prefix products
    # -----------------------------
    left = 1                       # Running product of all elements to the left
    for i in range(n):
        res[i] = left              # At index i, store product of all nums before i
        left = left * nums[i]      # Update left product by including nums[i]
    
    # -----------------------------
    # Second pass: compute suffix products
    # -----------------------------
    right = 1                      # Running product of all elements to the right
    for i in range(n - 1, -1, -1): # Traverse from rightmost index down to 0
        res[i] = res[i] * right    # Multiply stored prefix with suffix product
        right = right * nums[i]    # Update right product by including nums[i]
    
    return res                     # Final result with product_except_self for each index
