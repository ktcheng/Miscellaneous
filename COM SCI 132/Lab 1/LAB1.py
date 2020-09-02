# Lab 1

def sumSquares(aList):
    """
        >>> sumSquares(5)
        'error'
        >>> sumSquares('5')
        'error'
        >>> sumSquares(6.15)
        'error'
        >>> sumSquares([1,5,-3,5,9,8,4])
        221.0
        >>> sumSquares(['3',5,-3,5,9,8,4,'Hello'])
        229.0
    """
    
    result = 0.0
    
    if type(aList) == list:
        
        # Performs arithmetic on all valid list elements
        for element in aList:
            try:
                num = (float(element))**2
                result += num
            except:
                None
    
    else:
        result = "error"
        
    return result
