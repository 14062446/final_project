from GenerateMatrices import *
from WeatherDataGeneration import *
from WeatherDataAdd import *
import unittest
import os


'''This module includes tests for our data generation functions. Please note that these will take the longest to run, so we have included them in a separate file.'''


class Test2(unittest.TestCase):
    
    def test_matrix_generation(self):
        try:
            os.remove('PlusMatrix.csv')
            os.remove('MinusMatrix.csv')
            os.remove('NetChangeMatrix.csv')
        except OSError:
            pass
        
        save_matrices()
        
        self.assertTrue(os.path.isfile('PlusMatrix.csv'))
        self.assertTrue(os.path.isfile('MinusMatrix.csv'))
        self.assertTrue(os.path.isfile('NetChangeMatrix.csv'))
        
    def test_weather_functions(self):
        try:
            os.remove('WeatherDataCleaned.csv')
        except OSError:
            pass
        
        data = weatherDataLoad()
        data = precipIndicator(data)
        data = weatherDataDateColumn(data)
        data = weatherWDateDataClean(data)
        data = storeWeatherData(data)
        
        self.assertTrue(os.path.isfile('WeatherDataCleaned.csv'))
        
    def test_aggregation(self):
        try:
            os.remove('AggregatedDF.csv')
        except OSError:
            pass
        
        generateNetWeatherMatrix()
        
        self.assertTrue(os.path.isfile('AggregatedDF.csv'))
        
if __name__ == '__main__':
    unittest.main()        
         