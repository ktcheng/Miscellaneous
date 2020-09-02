# Lab 8

def isPrime(n, k=2):
    '''
        >>> isPrime(5)
        True
        >>> isPrime(1)
        False
        >>> isPrime(9)
        False
        >>> isPrime(85)
        False
        >>> isPrime(1019)
        True
    '''
    
    # Recursion condition checker
    bool_list = []
    
    if n <= 1: # 1 is not prime
        value = False
        bool_list.append(value)
        
    elif n == 2: # 2 is prime
        value = True
        bool_list.append(value)
        
    elif n > 2 and k < n: # k is a default variable to check primality
        # Checks for valid factors
        value = n / k
        
        if value % 1 != 0:
            # Continues checking; runs through recursion
            value = True
            bool_list.append(value)
        else:
            # Rules out prime number
            value = False
            bool_list.append(value)

    if True in bool_list and k < (n ** 0.5):
        # Checks k up until square root of n
        return isPrime(n, k + 1)
    
    elif False in bool_list:
        return False # Number is not prime
    
    elif True in bool_list:
        return True # Number is prime
