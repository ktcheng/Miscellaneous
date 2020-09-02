# Lab 3

def countWords(txt):
    """
        >>> article1='''
        ... He will be the president of the company; right now
        ... he's a vice president.
        ... But he ..... himself,  is no sure of it...
        ... (Later he will see the importance of these 3.)
        ... '''
        >>> expected={'he': 3,"he's": 1, 'will': 2, 'be': 1, 'the': 3, 'president': 2, 'of': 3, 'company': 1, 'right': 1, 'now': 1, 'is': 1, 'a': 1, 'vice': 1, 'but': 1, 'himself': 1, 'no': 1, 'sure': 1, 'it': 1, 'later': 1, 'see': 1, 'importance': 1, 'these': 1}
        >>> countWords(article1)==expected
        True
        >>> countWords(55)
        'error'
        >>> countWords([3.5,6])
        'error'
    """
    
    # Generates word count dictionary
    count = dict()
    txt1 = ""
    
    try:
        
        # Regenerates message without nonletters
        for char in txt:
            if char in "?.,\/:;()":
                None
            elif char in "1234567890":
                None
            else:
                txt1 += char.lower()
        
        # Separates string into individual words
        string = txt1.split()
        
        for word in string:
            word.strip()
            
            # Adds to dictionary if not duplicate
            if word in count:
                count[word] += 1
            else:
                count[word] = 1
        return count
    
    except:
        msg = "error"
        return msg

def studentGrades(gradeList):
    """
        >>> grades = [
        ...     ['Student', 'Quiz 1', 'Quiz 2', 'Quiz 3'],
        ...     ['John', 100, 90, 80],
        ...     ['McVay', 88, 99, 111],
        ...     ['Rita', 45, 56, 67],
        ...     ['Ketan', 59, 61, 67],
        ...     ['Saranya', 73, 79, 83],
        ...     ['Min', 89, 97, 101]]
        >>> studentGrades(grades)
        [90, 99, 56, 62, 78, 95]
        >>> grades = [
        ...     ['Student', 'Quiz 1', 'Quiz 2'],
        ...     ['John', 100, 90],
        ...     ['McVay', 88, 99],
        ...     ['Min', 89, 97]]
        >>> studentGrades(grades)
        [95, 93, 93]
        >>> studentGrades(55)
        'error'
    """
    
    # List of student averages
    new_list = []
    
    # Input validation checker
    try:
        
        # Separates 2D list by element
        for i in gradeList[1:]:
            y = sum(i[1:]) # Sum of test scores
            z = len(i[1:]) # Number of tests taken
            avg = int(y / z)
            new_list.append(avg)
        return new_list
    
    except:
        msg = "error"
        return msg
