from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Problem:
          Given a sorted list of integers 'numbers' (1-indexed in the problem statement),
          find two distinct elements whose sum equals 'target' and return their indices.
          The input array is sorted in non-decreasing order.

        Approach (Two Pointers):
          - Because the array is sorted, we can efficiently find the pair using two pointers.
          - Initialize:
                left  = start of the list (0)
                right = end of the list (len(numbers) - 1)
          - While left < right:
              1. Compute the sum: current_sum = numbers[left] + numbers[right]
              2. If current_sum == target:
                     Return [left + 1, right + 1]   # 1-based indices
              3. If current_sum > target:
                     Decrease right pointer (sum too large)
              4. Else:
                     Increase left pointer (sum too small)
          - If no pair is found, return an empty list (though the problem guarantees one).

        Why it works:
          - Moving 'left' increases the sum (since numbers are sorted ascending).
          - Moving 'right' decreases the sum.
          - This allows us to zero in on the correct pair in one linear pass.

        Time Complexity:
          - O(n): Each pointer moves at most once through the array.

        Space Complexity:
          - O(1): Constant extra space.
        """

        left = 0
        right = len(numbers) - 1

        while left < right:
            current_sum = numbers[left] + numbers[right]

            if current_sum == target:
                return [left + 1, right + 1]  # Return 1-based indices as required

            elif current_sum > target:
                right -= 1  # Sum too large, move right pointer leftward
            else:
                left += 1   # Sum too small, move left pointer rightward

        return []  # (Unreachable if input guarantees a solution