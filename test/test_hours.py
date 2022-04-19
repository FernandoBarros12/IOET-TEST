'''Automated tests for hour_format function'''
import unittest
from datetime import time
from src.analyze_data import AnalyzeData

class TestHour(unittest.TestCase):
    '''
    Test class for hour_format
    '''
    def test_hour(self):
        '''
        Test string convertion to time
        '''
        #Converts string to time type
        comparison_1=time(12,0)
        comparison_2=time(13,0)
        comparison_3=time(14,0)
        example=AnalyzeData()
        self.assertAlmostEqual(example.hour_format("12:00"),comparison_1)
        self.assertAlmostEqual(example.hour_format("13:00"),comparison_2)
        self.assertAlmostEqual(example.hour_format("14:00"),comparison_3)

    def test_types(self):
            '''
            Test type errors
            '''
            example_type=AnalyzeData()
            self.assertRaises(TypeError,example_type.hour_format, 2)
            self.assertRaises(TypeError,example_type.hour_format, True)
            self.assertRaises(TypeError,example_type.hour_format, 2.2)
   
   