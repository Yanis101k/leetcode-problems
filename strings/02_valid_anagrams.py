from collections import Counter


def is_anagram1(s: str, t: str) -> bool:
    """
    Time:  O(n) — we loop over s once, t once, and again over the dictionary.
    Space: O(n) — in the worst case (all characters unique), dictionary stores n keys.
           If characters are restricted (like only lowercase letters), space is O(1).

    explanation:
    
    - First, count how many times each character appears in s (using a dictionary).
    - Then, for every character in t, reduce the count in the dictionary.
    - If a character in t isn’t found, or we try to reduce below 0, it’s not an anagram.
    - Finally, check that no counts are left over.
    - If everything matches perfectly, the strings are anagrams.
    """
    if len(s) != len(t):
        return False

    char_occurence = {}
    for char in s:
        char_occurence[char] = char_occurence.get(char, 0) + 1

    for char in t:
        if not (char in char_occurence):
            return False
        if char_occurence[char] == 0:
            return False
        char_occurence[char] -= 1

    for char in char_occurence:
        if char_occurence[char] > 0:
            return False

    return True


def is_anagram2(s: str, t: str) -> bool:
    """
    Time:  O(n) — loop once over s, once over t. Dictionary operations are O(1) average.
    Space: O(n) — dictionary could hold up to n unique characters (O(1) if limited set).

     explanation:
    - Count all characters in s.
    - While scanning t, decrease counts.
    - If any character isn’t present, return False.
    - If a count becomes 0, remove the key from the dictionary to keep it small.
    - At the end, if dictionary is empty, it means perfect match → an anagram.
    """
    if len(s) != len(t):
        return False

    char_occurence = {}
    for char in s:
        char_occurence[char] = char_occurence.get(char, 0) + 1

    for char in t:
        if not (char in char_occurence):
            return False
        char_occurence[char] -= 1
        if char_occurence[char] == 0:
            del char_occurence[char]

    return len(char_occurence) == 0


def is_anagram3(s: str, t: str) -> bool:
    """
    Time:  O(n log n) — because we sort both strings (sorting dominates).
    Space: O(1) or O(n) depending on sorting implementation (Python creates new lists).

    explanation:
    - If two strings are anagrams, sorting them will result in the same order of characters.
    - So, just sort s and t and compare.
    - This is simple to write and easy to understand, but less efficient for very large strings.
    """
    return sorted(s) == sorted(t)


def is_anagram4(s: str, t: str) -> bool:
    """
    Time:  O(n) — building two Counters (hash maps) takes linear time.
    Space: O(n) — in the worst case (all unique characters).

    explanation:
    - Use Python's built-in Counter, which counts occurrences of each character.
    - Compare the two Counters directly.
    - If they’re equal, the strings have the same letters in the same counts → an anagram.
    - This is the cleanest solution in Python, but depends on importing collections.Counter.
    """
    return Counter(s) == Counter(t)


# Example run
print(is_anagram1("anagram", "nagaram"))  # True
print(is_anagram2("anagram", "nagaram"))  # True
print(is_anagram3("anagram", "nagaram"))  # True
print(is_anagram4("anagram", "nagaram"))  # True

