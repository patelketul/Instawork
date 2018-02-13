import unittest,sys,os
sys.path.append(str((os.path.abspath(__file__))).split("ParallelTesting")[0]+"ParallelTesting")

from Tests.FirstTest import FirstTest

if __name__=="__main__":
    args = sys.argv
    browser = args[1]
    s1 = unittest.TestLoader().loadTestsFromTestCase(FirstTest)
    unittest.TextTestRunner(verbosity=2).run(s1)