import unittest
from company_model import CompanyModel
from testutil import NamedNumber

class TestCompanyModel(unittest.TestCase):
    def setUp(self):
        self.company = CompanyModel()

    def test_add_department(self):
        self.company.add_user('Nisse', 'Donald Duck')
        assert True

    def test_get_head_count_for(self):
    	#self.company.add_user('Nisse', 'Donald Duck')
    	self.company.get_headcount_for('Donald Duck')
    	assert True


if __name__ == '__main__':
	unittest.main()