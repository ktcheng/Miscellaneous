# Lab 4

def encrypt(message, key):
    """
        >>> encrypt("Hello world",12)
        'Tqxxa iadxp'
        >>> encrypt("We are Penn State!!!",6)
        'Ck gxk Vktt Yzgzk!!!'
        >>> encrypt("We are Penn State!!!",5)
        'Bj fwj Ujss Xyfyj!!!'
        >>> encrypt(5.6,3)
        'error'
        >>> encrypt('Hello',3.5)
        'error'
        >>> encrypt(5.6,3.15)
        'error'
    """
    
    # Input validation checker
    try:
        msg = ""
        for char in message:
            
            if char.isalpha() == True:
                
                if char.isupper() == True:
                    
                    # ord(string) = integer; chr(integer) = string
                    x = ord(char)
                    x = x + key
                    
                    if x > 90:
                        x = x - 26
                        new_char = chr(x)
                        msg += new_char
                    else:
                        new_char = chr(x)
                        msg += new_char
                        
                else:
                    x = ord(char)
                    x = x + key
                    
                    if x > 122:
                        x = x - 26
                        new_char = chr(x)
                        msg += new_char
                    else:
                        new_char = chr(x)
                        msg += new_char
                        
            # Encryption doesn't affect non-alphabet characters
            else:
                msg += char
        return msg
    
    except:
        msg = "error"
        return msg

def decrypt(message, key):
    """
        >>> decrypt("Tqxxa iadxp",12)
        'Hello world'
        >>> decrypt("Ck gxk Vktt Yzgzk!!!",6)
        'We are Penn State!!!'
        >>> decrypt("Bj fwj Ujss Xyfyj!!!",5)
        'We are Penn State!!!'
        >>> decrypt(5.6,3)
        'error'
        >>> decrypt('Hello',3.5)
        'error'
        >>> decrypt(5.6,3.15)
        'error'
    """
    
    try:
        msg = ""
        for char in message:
            
            if char.isalpha() == True:
                
                if char.isupper() == True:
                    x = ord(char)
                    x = x - key
                    
                    if x < 65:
                        x = x + 26
                        new_char = chr(x)
                        msg += new_char
                    else:
                        new_char = chr(x)
                        msg += new_char
                        
                else:
                    x = ord(char)
                    x = x - key
                    
                    if x < 97:
                        x = x + 26
                        new_char = chr(x)
                        msg += new_char
                    else:
                        new_char = chr(x)
                        msg += new_char
                        
            else:
                msg += char       
        return msg
    
    except:
        msg = "error"
        return msg
