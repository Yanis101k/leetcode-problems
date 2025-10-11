from typing import List 
def maxArea(height: List[int]) -> int:
    """
    Problem:
      Given an array 'height' where each element represents a vertical line at that index,
      find the maximum amount of water a container can store when choosing two lines.
      The container's area is min(height[i], height[j]) * (j - i).

    Approach (Two Pointers, Greedy):
      - Start with two pointers at the extremes: left = 0, right = n - 1.
      - The current area is limited by the shorter line (the "bottleneck").
      - To possibly increase area as we shrink the width, we must try to get a taller
        bottleneck. Therefore:
          * Move the pointer at the SHORTER line inward, hoping to find a taller line.
          * Moving the taller line inward cannot help increase the min height and
            only reduces width, so it's never better than moving the shorter one.
      - Track the maximum area seen while the pointers move towards each other.

    Correctness intuition:
      - Area = min(h_left, h_right) * width. Width always decreases when pointers move.
      - The only way to offset the loss of width is to increase the limiting height.
      - Only moving the shorter side can potentially increase min(h_left, h_right),
        so any optimal solution can be found by this rule.

    Time Complexity:
      - O(n): Each pointer moves at most n steps (one pass).

    Space Complexity:
      - O(1): Constant extra space.
    """

    # Optional guard: if fewer than 2 lines, container area is 0.
    if len(height) < 2:
        return 0

    left, right = 0, len(height) - 1
    best = 0

    while left < right:
        # Current container area using the two lines at left and right.
        width = right - left
        h = min(height[left], height[right])
        area = width * h

        # Update maximum area found so far.
        if area > best:
            best = area

        # Move the pointer at the shorter line inward to seek a taller bottleneck.
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return best