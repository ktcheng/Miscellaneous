# Lab 7

def triangle(n):
    return recursive_triangle(n, n)

def recursive_triangle(k, n):
    '''
        >>> recursive_triangle(2,4)
        '  **\\n   *'
        >>> print(recursive_triangle(2,4))
          **
           *
        >>> triangle(4)
        '****\\n ***\\n  **\\n   *'
        >>> print(triangle(4))
        ****
         ***
          **
           *
    ''' 
    # k = number of *; n = number of spaces (width of line)
    
    # Resultant String
    msg = ""
    
    # Recursion end condition
    if (not (k > n)) and k > 0:
        
        # Final recursion instance
        if k == 1:
            msg = (" " * (n - k)) + (("*") * k)
            
        else:
            msg = (" " * (n - k)) + (("*") * k) + "\n"
            msg += str(recursive_triangle(k - 1, n))
            
    return msg
