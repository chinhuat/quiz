"""
A generic unsigned integer data type implementation
"""
class UInt:

    """
    Set default values for bits and obj to enable method overloading.
    Note the second argument can be any object instead of an integer.
    """
    def __init__(self, bits=0, obj=0):
        
        # internal variables
        self._bits = bits
        self._min = 0
        self._max = (1 << self._bits) - 1

        # allow initializing from any data types that can be casted to integer
        self._value = int(obj)

        self._check_range()

    """
    When overflow or underflow occurs, roll-over to start from the other end.
    """
    def _check_range(self):

        if self._value < self._min or self._value > self._max:
            self._value %= (self._max + 1)
    

    """
    This method overloads add operator to support UInt32 + int, int + UInt32
    and UInt32 + UInt32.
    """
    def __add__(self, obj):

        # allow adding any data types that can be casted to integer
        self._value += int(obj)
        self._check_range()

        return self


    """
    This method overloads int() to cast this class to an integer.
    """
    def __int__(self):

        return self._value


class UInt32(UInt):

    def __init__(self, obj=0):

        # initialize superclass to 32-bit
        UInt.__init__(self, 32, obj)


class UInt16(UInt):
    
    def __init__(self, obj=0):

        # initialize superclass to 16-bit    
        UInt.__init__(self, 16, obj)

