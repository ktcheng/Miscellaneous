# Lab 2

def joinedList(n):
    """
        >>> joinedList(5)
        [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]
        >>> joinedList(-3)
        [-3, -2, -1, -1, -2, -3]
        >>> joinedList('5')
        'error'
        >>> joinedList([2,8,[9]])
        'error'
        >>> joinedList(0)
        []
    """
    
    # Checks for valid input
    try:
        if int(n) > 0:
            joined_list = []
            
            # Ascending Numbers
            for i in range(n):
                joined_list.append(i + 1)
            
            # Descending Numbers
            while True:
                joined_list.append(n)
                n -= 1
                if n == 0:
                    break
            return joined_list
        
        elif int(n) < 0:
            joined_list = []
            j = -1 # Negative number placeholder
            
            # Ascending Numbers
            for i in range(n, 0):
                joined_list.append(i)
            
            # Descending Numbers
            while True:
                joined_list.append(j)
                j -= 1
                if j == (n - 1):
                    break
            return joined_list
        
        else:
            # Number input is zero
            joined_list = []
            return joined_list
    except:
        msg = "error"
        return msg

def removePunctuation(txt):
    """
        # txt : string
        # It replaces every character that is not an alphabet letter
        # into a space, and returns it.

        >>> removePunctuation("I like chocolate cake!!(!! It's the best flavor..;.$ for real")
        'I like chocolate cake      It s the best flavor      for real'
        >>> removePunctuation("Dots...................... many dots..X")
        'Dots                       many dots  X'
        >>> removePunctuation(55)
        'error'
        >>> removePunctuation([3.5,6])
        'error'

    """
    
    # Checks for valid input
    if type(txt) == str:
        msg = ""
        for char in txt:
            
            # Replaces nonletters with spaces
            if char.isalpha():
                msg += char
            else:
                msg += " "
                
    else:
        msg = "error"
    return msg 
