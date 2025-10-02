def romanToInt(s: str) -> int:
    # Mapping of Roman numerals to their integer values
    roman_int = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    
    # This variable will hold the final result
    int_number = 0
    n = len(s)  # length of the Roman numeral string
    
    # Iterate through each Roman numeral character in the string
    for i in range(n):
        # If the current value is smaller than the next value,
        # it means we have a subtractive pair (e.g., IV = 4, IX = 9).
        if i < n - 1 and roman_int[s[i]] < roman_int[s[i + 1]]:
            # Subtract the current value instead of adding
            int_number -= roman_int[s[i]]
        else:
            # Otherwise, add the current value normally
            int_number += roman_int[s[i]]
    
    return int_number


"""
Approach:
---------
- Roman numerals are usually written largest to smallest, added together.
  Example: XIII = 10 + 1 + 1 + 1 = 13
- But sometimes a smaller numeral comes before a larger one,
  which means subtraction (e.g., IV = 5 - 1 = 4).
- Algorithm:
  1. Loop through the string.
  2. If current numeral < next numeral → subtract it.
  3. Otherwise → add it.
  4. Return the total.

Example Walkthrough ("MCMXCIV" = 1994):
- M = 1000 (add → 1000)
- C before M → subtract 100 (total = 900 + 1000 so far)
- X before C → subtract 10 (total = +90)
- I before V → subtract 1 (total = +4)
Final total = 1994

Complexity:
-----------
- Time Complexity: O(n), where n = length of the string
  (we scan each character once, dictionary lookups are O(1)).
- Space Complexity: O(1)
  (dictionary size is constant, result uses a few variables only).
"""


print( romanToInt( "MCMXCIV" ))