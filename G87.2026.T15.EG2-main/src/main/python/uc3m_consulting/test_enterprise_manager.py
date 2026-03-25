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

    def test_TC2(self):
        obj = EnterpriseManager()

        result = obj.register_project(
        'A58818501',
        'PROJEC2026',
        'TreasureHunters2',
        'HR',
        '21/05/2026',
        300000.00
        )
        print(result)
        self.assertEqual(result, '4f8da926a15bd3730e4ac6b36a3021ff')

    def test_TC3(self):
        obj = EnterpriseManager()

        result = obj.register_project(
        'A58818501',
        'PROJ01',
        'DescriptionThatDescriptionThis',
        'HR',
        '21/05/2026',
        300000.00
        )

        print(result)
        self.assertEqual(result, '9e740467be0d332761fcb2ca62e95d9b')

    def test_TC4(self):
        obj = EnterpriseManager()

        result = obj.register_project('A58818501',
        'PROJ01',
        'TreasureHunters2',
        'HR',
        '01/05/2026',
        300000.00
        )

        print(result)
        self.assertEqual(result, 'c40688a65c8da55fb336061ce5756e58')
