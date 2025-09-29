from typing import List 
from collections import Counter 
import heapq   # Python’s built-in min-heap implementation

def topKFrequent1(self, nums: List[int], k: int) -> List[int]:
    # Step 1: Count the frequency of each number
    freq = Counter(nums)

    # Step 2: Sort unique numbers by frequency (descending order)
    # key=freq.get means sort by frequency
    sorted_nums = sorted(freq.keys(), key=freq.get, reverse=True)

    # Step 3: Take the first k elements
    return sorted_nums[:k]


"""
------------------------------------
Approach:
1. Count frequencies of all numbers.
2. Sort the unique numbers by frequency in descending order.
3. Slice the first k elements as the result.

------------------------------------
Time Complexity:
- Counting frequencies: O(n)     (where n = len(nums))
- Sorting unique elements: O(U log U)  (where U = number of unique elements)
- Slicing first k: O(k)
=> Overall: O(n + U log U)

This is slower than heap or bucket for large U, 
but simplest to write and fine for small inputs.

------------------------------------
Space Complexity:
- freq dictionary: O(U)
- sorted list: O(U)
- result: O(k)
=> Overall: O(U + k)
"""

def topKFrequent2(self, nums: List[int], k: int) -> List[int]:
    # Step 1: Count the frequency of each number in nums
    # Counter builds a dictionary: number -> frequency
    freq = Counter(nums)

    # Step 2: Find the maximum frequency
    # This helps us size the "bucket" array
    max_freq = max(freq.values())
    
    # Step 3: Create buckets (list of lists)
    # Index i of buckets will hold all numbers that appear exactly i times
    buckets = [[] for _ in range(max_freq + 1)]
    for num, f in freq.items():
        buckets[f].append(num)

    # Step 4: Collect results starting from highest frequency down
    res = []
    for f in range(max_freq, 0, -1):  # iterate from max frequency to 1
        for num in buckets[f]:        # go through all numbers with frequency f
            res.append(num)
            if len(res) == k:         # stop once we collected k elements
                return res

    # Step 5: Return result (covers case where k >= number of unique elements)
    return res


"""
------------------------------------
Approach:
1. Count frequencies of all numbers.
2. Use "bucket sort" idea: bucket[i] = list of numbers with frequency i.
3. Traverse buckets from highest frequency to lowest until we collect k elements.

------------------------------------
Time Complexity:
- Counting frequencies: O(n)   (where n = len(nums))
- Building buckets: O(U)       (where U = number of unique elements ≤ n)
- Traversing buckets: O(n)     (in worst case we scan all elements once)
=> Overall: O(n)

------------------------------------
Space Complexity:
- freq dictionary: O(U)
- buckets array: O(n) in worst case (each element frequency 1)
- result: O(k)
=> Overall: O(n)
"""




def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    # Step 1: Count the frequency of each number in nums
    freq = Counter(nums)

    # Step 2: Use a min-heap of size k
    # Each heap entry will be a tuple: (frequency, number)
    # The heap keeps the k most frequent elements
    heap = []

    for num, f in freq.items():
        # Push current (frequency, num) into the heap
        heapq.heappush(heap, (f, num))

        # If heap grows beyond size k, remove the smallest frequency
        if len(heap) > k:
            heapq.heappop(heap)

    # Step 3: Extract numbers from heap (only k remain)
    res = [num for (f, num) in heap]

    return res


"""
------------------------------------
Approach:
1. Count frequencies of all numbers using Counter.
2. Maintain a min-heap of size k:
   - Push (frequency, number) pairs.
   - If heap size > k, pop the smallest frequency.
   - This way, heap always contains the k most frequent elements.
3. Extract the numbers from the heap.

------------------------------------
Time Complexity:
- Counting frequencies: O(n)   (where n = len(nums))
- Heap operations: O(U log k)  (where U = number of unique elements)
   - Each of U elements may be pushed/popped into a heap of size ≤ k.
   - Push/Pop cost: O(log k).
- Overall: O(n + U log k)

This is more efficient than O(n log n) if k ≪ U.

------------------------------------
Space Complexity:
- freq dictionary: O(U)
- heap: O(k)
- result: O(k)
=> Overall: O(U + k)
"""