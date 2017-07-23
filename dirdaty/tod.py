'''
Time of day
'''
from ctypes import c_ubyte
from datetime import time
from numpy import pi, exp

class tod8(c_ubyte):

    def __repr__(self):
        t = self.value*1440/256
        return time(int(t//60), int(t%60)).strftime('%H:%M')

    def __unicode__(self):
        return self.__repr__()

    def __str__(self):
        return self.__repr__()

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
        return tod8(self.value + other.value)

    def __neg__(self):
        return tod8(-self.value)

    def __sub__(self, other):
        return tod8(self.value - other.value)

    def __mul__(self, other):
        return tod8(self.value*other)

    def __truediv__(self, other):
        return tod8(self.value // other)

    def __div__(self, other):
        return tod8(self.value // other)

    def __pow__(self, other):
        return tod8(self.value**other)

    #Other
    def __complex__(self):
        '''
        Projects time onto the unit circle
        '''
        return exp(1j*self.value*pi/128)

    @classmethod
    def from_time(cls, time):
        '''
        Encodes a datetime.time object into 8-bit time format
        '''
        return tod8(int((60*time.hour + time.minute)*256/1440))