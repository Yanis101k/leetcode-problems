from collections import Counter

def firstUniqChar( s: str) -> int:
        char_freq = Counter(s) 

        for index , char in enumerate( s ) : 
            if char_freq[char] == 1 : 
                return  index 
        

        return -1 ; 

# time complexity : O(N), N is the length of our string 
# we need to go over all the charcters in our string in order to assign them to the Counter 
# space complexity : O(K) , K is the number of uniq elements in the string 
# each uniq element in the string will need one memory space in the Counter  