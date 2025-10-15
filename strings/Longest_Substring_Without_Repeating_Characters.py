def lengthOfLongestSubstring( s: str) -> int:
        
        j = 0 
        char_pos = { }

        current_substring_len = 0 
        max_substring_len = current_substring_len
        while( j < len( s ) ) : 

            if s[j] in char_pos : 
                j = char_pos[s[j]]
                max_substring_len = max( max_substring_len , current_substring_len )
                char_pos = { }
                current_substring_len = 0 
            else : 
                char_pos[ s[j] ] = j 
                current_substring_len += 1 
            j+=1

        return max( max_substring_len , current_substring_len ) 


print( lengthOfLongestSubstring ( "abcabcbb" ))