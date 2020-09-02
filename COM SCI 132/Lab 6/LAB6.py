# Lab 6

class Vector:
    '''
        >>> Vector([1,2])+Vector([5])
        'Error - Invalid dimensions'
        >>> Vector([1,2])+Vector([5,2])
        Vector([6, 4])
        >>> Vector([1,2])-Vector([5,2])
        Vector([-4, 0])
        >>> Vector([1,2])*Vector([5,2])
        9
        >>> x=Vector([2,4,6])
        >>> y=Vector([2,4,6])
        >>> c=x+y
        >>> type(c)
        <class 'LAB6.Vector'>
        >>> print(c)
        Vector([4, 8, 12])
        >>> x==y
        True
        >>> x-Vector([1,2])
        'Error - Invalid dimensions'
        >>> x+5
        'Error - Invalid operation'
        >>> x*y
        56
        >>> x*5
        Vector([10, 20, 30])
        >>> 5*x
        Vector([10, 20, 30])
    '''

    def __init__(self, vector_list):
        self.vector = vector_list 
      
    if __name__ == '__main__':
        # Changes name to filename
        __name__ = 'LAB6'
    
    def __str__(self):
        # String format for returning vector
        x = "Vector({})".format(self.vector)
        return x
    
    # Represents vector object as defined string above
    __repr__ = __str__
    
    def __add__(self, other):
        
        if type(self) == type(other):
            
            if len(self.vector) == len(other.vector):
                v_list = [] # Resultant Vector
                
                for a, b in zip(self.vector, other.vector):
                    # Adds corresponding components together
                    total = a + b
                    v_list.append(total)
                return Vector(v_list)
            
            else:
                x = "Error - Invalid dimensions"
                return x
            
        else:
            x = "Error - Invalid operation"
            return x
    
    def __sub__(self, other):
        
        if type(self) == type(other):
            if len(self.vector) == len(other.vector):
                v_list = []
                
                for a, b in zip(self.vector, other.vector):
                    total = a - b
                    v_list.append(total)
                return Vector(v_list)
            
            else:
                x = "Error - Invalid dimensions"
                return x
            
        else:
            x = "Error - Invalid operation"
            return x
    
    def __mul__(self, other):
        
        # Vector dot product multiplication
        if type(self) == type(other):
            if len(self.vector) == len(other.vector):
                dot_product_sum = 0
                
                for a, b in zip(self.vector, other.vector):
                    total = a * b
                    dot_product_sum += total
                return dot_product_sum
            
            else:
                x = "Error - Invalid dimensions"
                return x
            
        # Vector scalar multiplication
        elif type(other) == int:
            v_list = []
            
            for i in self.vector:
                total = i * other
                v_list.append(total)
            return Vector(v_list)
                
    # Makes multiplication commutative
    def __rmul__(self, other):
        x = self * other
        return x
    
    # Vector equality checker
    def __eq__(self, other):
        if type(self) == type(other):
            
            if len(self.vector) == len(other.vector):
                x = True
                return x
            else:
                x = False
                return x
            
        else:
            x = False
            return x
