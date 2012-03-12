import unittest

import test_db
import test_ping
import test_regexp

loader = unittest.TestLoader()

suite = loader.loadTestsFromModule(test_ping)

suite.addTests(loader.loadTestsFromModule(test_db))
suite.addTests(loader.loadTestsFromModule(test_regexp))

runner = unittest.TextTestRunner(verbosity=10)
result = runner.run(suite)
