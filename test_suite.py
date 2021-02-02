import unittest
import helloworld

def suite():
    t1 = unittest.TestLoader().loadTestsFromTestCase(helloworld)
    test_suite = unittest.TestSuite([t1])
    unittest.TextTestRunner(verbosity=2).run(test_suite)
