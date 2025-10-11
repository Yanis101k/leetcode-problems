
def isPalindrome( s: str) -> bool:

        # remove the non-alphanumeric characters and convert  the upper case letters to lower case in s 
        new_s = ""

        for ch in s : 
            if ch.isalnum() :
                if ch.isupper() : 
                    ch = ch.lower()
                new_s = new_s + ch 
        # create two pointers 
        # left point to the left side and the right point to the right side 
        # to the string be a palindrom the content of the two pointers should be the same until the two pointers exceed each other or they are in the same place 
        left = 0 
        right = len( new_s ) - 1 

        while( left <= right ) : 
            if new_s[left] != new_s[right] : 
                return False 
            left = left + 1
            right = right - 1 
        return  True

        # time complixety : O(n²) : n is the number of alphanumiric characters 
        # in our string s because in this solution to create new_s at each alphanumiric character in s new_s string is created again .
        # space complixity : O(n) : n is the number of alphanumiric characters because our new_s will just containe alphanumiric characters