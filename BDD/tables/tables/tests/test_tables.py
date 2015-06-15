import unittest
from steps.company_model import CompanyModel
from steps.testutil import NamedNumber

class TestCompanyModel(unittest.TestCase):
    def setUp(self):
        self.company = CompanyModel()

    def test_add_department(self):
        self.company.add_user('Nisse', 'Donald Duck')
        assert True