import os
import sys
sys.path.insert(1, 'tests/')
import unittest
import test_cities
import test_delete
import test_country
import test_distance
import test_reset

def do_tests():
    
    cities = unittest.TestLoader().loadTestsFromModule(test_cities)
    unittest.TextTestRunner(verbosity=1).run(cities)

    delete = unittest.TestLoader().loadTestsFromModule(test_delete)
    unittest.TextTestRunner(verbosity=1).run(delete)

    country = unittest.TestLoader().loadTestsFromModule(test_country)
    unittest.TextTestRunner(verbosity=1).run(country)

    distance = unittest.TestLoader().loadTestsFromModule(test_distance)
    unittest.TextTestRunner(verbosity=1).run(distance)

    reset = unittest.TestLoader().loadTestsFromModule(test_reset)
    unittest.TextTestRunner(verbosity=1).run(reset)
if __name__ == '__main__':
	do_tests()
