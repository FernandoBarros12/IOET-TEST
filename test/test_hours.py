'''Testing hours formatting function'''
import unittest
from datetime import time
from src.functions import hour_format

class TestHour(unittest.TestCase):
    '''
    Test class
    '''
    def test_hour(self):
        '''
        Return:
        '''
        #Converts string to time type
        a_uno=time(12,0)
        b_dos=time(13,0)
        c_tres=time(14,0)
        self.assertAlmostEqual(hour_format("12:00"),a_uno)
        self.assertAlmostEqual(hour_format("13:00"),b_dos)
        self.assertAlmostEqual(hour_format("14:00"),c_tres)
