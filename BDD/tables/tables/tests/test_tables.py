import unittest

class TestCompanyModel(unittest.TestCase):
    def setUp(self):
        self.company = CompanyModel()

    def test_add_department(self):
        self.company.add_department('Nisse')
        assert False