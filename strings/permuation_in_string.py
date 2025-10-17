from collections import Counter  

def checkInclusion1(s1: str, s2: str) -> bool:
    """
    Approach:
    - Brute-force: slide a window of len(s1) over s2.
    - For each window, compare its character Counter to s1's Counter.

    Time complexity:  O((n - m) * m)   (n = len(s2), m = len(s1))
    Space complexity: O(26) ≈ O(1)     (constant alphabet size)
    """
    s1_counter = Counter(s1)
    i = 0
    while i <= len(s2) - len(s1):
        if Counter(s2[i : i + len(s1)]) == s1_counter:
            return True
        i += 1
    return False


def checkInclusion(s1: str, s2: str) -> bool:
    """
    Approach:
    - Sliding window with frequency arrays (size 26 for lowercase letters).
    - Expand and reset window efficiently without re-counting each substring.

    Time complexity:  O(n)   (each char visited at most twice)
    Space complexity: O(26) ≈ O(1)
    """
    len_s1, len_s2 = len(s1), len(s2)
    if len_s1 > len_s2:
        return False

    base_mp = [0]*26
    for ch in s1:
        base_mp[ord(ch) - ord('a')] += 1

    mp = base_mp.copy()
    left, right = 0, 0
    count = len_s1

    while right < len_s2:
        idx = ord(s2[right]) - ord('a')

        if mp[idx] > 0:
            mp[idx] -= 1
            right += 1
            count -= 1
            if count == 0:
                return True
        else:
            left += 1
            right = left
            count = len_s1
            mp = base_mp.copy()
    return False