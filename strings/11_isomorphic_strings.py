from typing import Dict , List 
def isIsomorphic1( s: str, t: str) -> bool:
        
        if len(s) != len(t) :
            return False

        char_pos_s : Dict[ str : List[int] ]  = {}

        for index , char in  enumerate(s) :

            if char in char_pos_s : 
                char_pos_s[char].append( index )
            else : 
                char_pos_s[char] =[index] 
        
        char_pos_t : Dict[ str : List[int] ]  = {}

        for index , char in  enumerate(t) :

            if char in char_pos_t : 
                char_pos_t[char].append( index )
            else : 
                char_pos_t[char] =[index] 

        positions1 = list (char_pos_s.values())
        positions2 = list ( char_pos_t.values())

        return positions1 == positions2 

# TIME COMPLEXITY: O(n)
    # We loop once over s → O(n)
    # We loop once over t → O(n)
    # Converting .values() and comparing lists → O(n)
    # Total = O(n)
    #
    # SPACE COMPLEXITY: O(n)
    # Two dictionaries store all indices → total elements ≈ n
    # Each character’s list of positions adds up to n total.
    # Total extra space = O(n)
            
print( isIsomorphic1( "foo" , "baa" ))