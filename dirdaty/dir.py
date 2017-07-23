from ctypes import c_ubyte
from numpy import pi, exp
import sys

class dir8(c_ubyte):
    '''
    8-bit direction.
    '''
    #Representations
    def __str__(self):
        return '%f\260'%(float(self.value)*360/256)

    def __unicode__(self):
        return u'%f\u00b0'%(float(self.value)*360/256)

    def __repr__(self):
        if sys.version[0] == 2:
            return '%f\260'%(float(self.value)*360/256)
        else:
            return u'%f\u00b0'%(float(self.value)*360/256)

    #Logical tests
    def __lt__(self, other):
        return self.value < other.value

    def __le__(self, other):
        return self.value <= other.value

    def __gt__(self, other):
        return self.value > other.value

    def __ge__(self, other):
        return self.value >= other.value

    def __eq__(self, other):
        return self.value == other.value

    def __ne__(self, other):
        return self.value != other.value

    #Arithmetic operations
    def __add__(self, other):
        return dir8(self.value + other.value)

    def __neg__(self):
        return dir8(-self.value)

    def __sub__(self, other):
        return dir8(self.value - other.value)

    def __mul__(self, other):
        return dir8(self.value*other)

    def __truediv__(self, other):
        return dir8(self.value // other)

    def __div__(self, other):
        return dir8(self.value // other)

    def __pow__(self, other):
        return dir8(self.value**other)

    #Other
    def __complex__(self):
        '''
        Projects angle onto the unit circle
        '''
        return exp(1j*self.value*pi/128)

    @classmethod
    def from_degrees(cls, degrees):
        return cls(round(degrees*256/360))

    @classmethod
    def from_radians(cls, radians):
        return cls(round(radians*128/pi))

    