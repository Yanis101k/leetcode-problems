def isPalindrome1( x: int) -> bool:
        
        # palindrome number should be positive 
        # because with minus sign it cannot be a palindrom 
        if x < 0 : 
            return False

        # convert the number to a string 
        number = str( x )
        
        # create two pointers one at the start and other at the end 
        # the two will get colser if both point to the same character 
        # if they point to diffrent character that means is not palindrom
        # the two pointers will exceed each other  ( left < right ) if the number is palaindrom 

        left = 0
        right = len(number) - 1 
        
        while left < right : 
              
              if number[right] != number[left] : 
                return False
              right-=1 
              left+=1
         
        return True 

        # time complexity : O(n) we go through the string and make 1/2 string size checkings
        # space complixety : O(n) we used a string that will contain n digits which is number of digits of our string   

def isPalindrome2( x: int) -> bool:
        
        # get number of digits of the the integer 

        number_of_digits = 1
        
        copy_of_x = x 

        while True : 
            copy_of_x = int (copy_of_x / 10 )

            if copy_of_x == 0 : 
                 break 
            number_of_digits += 1 
           
        # get the reversed number of x 
        reversed_x = 0 
        copy_of_x = x 

        while number_of_digits != 0 : 
            
         position = int ((copy_of_x % 10 )) * pow( 10 ,      number_of_digits -1 )
         reversed_x = reversed_x + position
         copy_of_x = copy_of_x / 10    
         number_of_digits -= 1
        
        # x should equal to it reverse if is palaindrom 
        return x == reversed_x

        # time complexity : O(n) n is number of digits of x 
        # space complexity : O(1)   
print( isPalindrome2( 943234 ))