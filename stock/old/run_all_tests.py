import unittest

import test_myclass
import test_mockbors  # mock for Bors
import test_mockmorningstar      # mock for Morningstar :-)

import test_bors        # test Bors for real, we need internet ...
import test_morningstar  # test Morningstar

loader = unittest.TestLoader()

suite = loader.loadTestsFromModule(test_myclass)

suite.addTests(loader.loadTestsFromModule(test_mockbors))
suite.addTests(loader.loadTestsFromModule(test_mockmorningstar))

suite.addTests(loader.loadTestsFromModule(test_bors))
suite.addTests(loader.loadTestsFromModule(test_morningstar))

runner = unittest.TextTestRunner(verbosity=10)
result = runner.run(suite)
