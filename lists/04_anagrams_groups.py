from typing import List , Dict 
from collections import Counter

from typing import List
from collections import Counter

from typing import List
from collections import Counter

def groupAnagrams1(strs: List[str]) -> List[List[str]]:
    # Approach:
    # Brute-force grouping using a double loop.
    # - We iterate over each string i.
    # - If it hasn't been "grouped" yet, we create a new group starting with strs[i].
    # - Then we scan the remaining strings j > i and compare Counters:
    #     if Counter(strs[i]) == Counter(strs[j]), we add strs[j] to the same group.
    #
    # Data structures:
    # - already_grouped: a set of strings we've already placed into some group.
    #   NOTE: because this is a set of string *values*, exact duplicate strings
    #         (e.g., two identical "eat") are treated as one; this collapses duplicates.
    # - anagrams_grouped: list of groups (each group is a list of strings).

    already_grouped = set()
    anagrams_grouped = []

    for i in range(len(strs)):
        if strs[i] not in already_grouped:
            already_grouped.add(strs[i])
            anagrams_list = [strs[i]]

            # Compare strs[i] with every later string strs[j]
            for j in range(i + 1, len(strs)):
                # Building Counter(strs[i]) and Counter(strs[j]) each time
                # and comparing them to check anagram equality
                if Counter(strs[i]) == Counter(strs[j]):
                    anagrams_list.append(strs[j])
                    already_grouped.add(strs[j])

            anagrams_grouped.append(anagrams_list)

    return anagrams_grouped

    # ------------------------------
    # ⏱ Time Complexity Analysis:
    # Let n = number of strings, k = max string length.
    #
    # Outer loop runs up to n times.
    # Inner loop (in worst case) runs ~n/2 on average → O(n) per outer iteration.
    # For each (i, j) comparison:
    #   - Counter(strs[i]) = O(k)
    #   - Counter(strs[j]) = O(k)
    #   - Equality check between Counters = O(k)
    # Combined per comparison ≈ O(k).
    #
    # Total worst-case time: O(n^2 * k).
    #
    # ------------------------------
    # 💾 Space Complexity Analysis:
    # - already_grouped can hold up to O(n) distinct string *values* (each up to length k) → O(n * k).
    # - anagrams_grouped stores all input strings once across groups → O(n * k).
    # - Temporary Counters are O(k) each; they are created per comparison but not kept → O(k) auxiliary.
    #
    # Overall space: O(n * k).


def groupAnagrams2(strs: List[str]) -> List[List[str]]:
    # Approach:
    # We use a hash map (dictionary) to group anagrams together.
    # Key   = a tuple of sorted (character, frequency) pairs
    #         Example: "eat" -> Counter("eat") = {'e':1,'a':1,'t':1}
    #                  sorted items -> (('a',1),('e',1),('t',1))
    #         "tea" produces the same key, so both go to the same group.
    # Value = list of strings (anagrams) that share this signature
    #
    # This approach is general and works for ANY characters (not only lowercase a–z).

    grouped_anagrams = {}

    for s in strs:
        # Build a frequency dictionary of the string → Counter(s)
        # Sort its items to get a consistent order → O(u log u),
        # where u = number of unique characters in the string.
        # Convert to tuple so it can be used as a dict key.
        sig = tuple(sorted(Counter(s).items()))

        # Add the string to the correct anagram group
        if sig in grouped_anagrams:
            grouped_anagrams[sig].append(s)
        else:
            grouped_anagrams[sig] = [s]

    # Return the grouped anagrams
    return list(grouped_anagrams.values())

    # ------------------------------
    # ⏱ Time Complexity Analysis:
    # Let n = number of strings, k = maximum length of a string
    #
    # For each string:
    #   - Counter(s): O(k) (scan the string)
    #   - sorted(Counter(s).items()): O(u log u),
    #       worst case u = k (all characters unique) → O(k log k)
    #   - Tuple conversion: O(u) ≤ O(k)
    #   - Dictionary operations (lookup + insert/append): O(1) average
    #
    # Total = O(n · k log k) in the worst case
    #
    # ------------------------------
    # 💾 Space Complexity Analysis:
    # - Dictionary keys: each key stores up to u character-frequency pairs
    #   → O(n · k) in the worst case
    # - Dictionary values: store all strings in lists → O(n · k)
    # - Temporary Counters: O(k) per string, reused
    #
    # Overall = O(n · k)





def groupAnagrams3( strs: List[str]) -> List[List[str]]:
        # Approach:
        # We use a hash map (dictionary) to group anagrams together.
        # Key   = a 26-length tuple that represents the frequency of each letter (a–z) in the string
        # Value = list of strings (anagrams) that share the same character frequency signature
        #
        # Example:
        #   Input: ["eat", "tea", "tan", "ate", "nat", "bat"]
        #   "eat" -> freq vector = [1,0,0,...,1,...,1,...,0] -> tuple(...) becomes the key
        #   "tea" -> produces the same key
        #   Both are grouped together in the dictionary
        #
        # This avoids sorting strings (O(k log k)) and instead uses counting (O(k)).

        key_anagrams: Dict[tuple, List[str]] = {}

        for s in strs:
            # Build a frequency vector of size 26 for lowercase English letters
            freq_char = [0] * 26
            for char in s:
                freq_char[ord(char) - ord('a')] += 1

            # Convert to tuple so it can be used as a dictionary key (must be immutable + hashable)
            sig = tuple(freq_char)

            # Insert the string into the correct anagram group
            if sig in key_anagrams:
                key_anagrams[sig].append(s)
            else:
                key_anagrams[sig] = [s]

        # Return all the grouped anagrams
        return list(key_anagrams.values())

        # ------------------------------
        # ⏱ Time Complexity Analysis:
        # Let n = number of strings, k = maximum length of a string
        #
        # For each string:
        #   - Building frequency vector takes O(k)
        #   - Creating tuple from 26 counts = O(26) → O(1) (constant time)
        #   - Dictionary operations (lookup + insert/append) = O(1) average
        #
        # Total = O(n · k)
        #
        # ------------------------------
        # 💾 Space Complexity Analysis:
        # - Frequency vector per string = O(26) = O(1), reused each iteration
        # - Dictionary keys: at most n unique signatures, each is size 26 → O(n · 26) = O(n)
        # - Dictionary values: store all strings in lists → O(n · k) (to store the characters of all strings)
        #
        # Overall = O(n · k)

    
print( groupAnagrams3( ["eat" , "eat" ,"tea","tan","ate","nat","bat"]) ) 