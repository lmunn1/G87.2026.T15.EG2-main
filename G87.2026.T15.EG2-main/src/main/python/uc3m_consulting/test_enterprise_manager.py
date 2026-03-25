import os
from unittest import TestCase
from uc3m_consulting import EnterpriseManager


class TestEnterpriseManager(TestCase):
    def setUp(self):
        self.file_path = "corporate_operations.json"
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_TC1(self):
        obj = EnterpriseManager()

        result = obj.register_project(
            company_cif= 'A58818501',
            project_acronym='PRO01',
            project_description='ProjectOne',
            department='HR',
            date='31/12/2027',
            budget=50000.00
        )
        print(result)
        self.assertEqual(result, '6ccd2e9ff01bab51ca55e76bf99a53c3')
