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
            department='FINANCE',
            date='31/12/2027',
            budget=50000.00
        )
        print(result)
        self.assertEqual(result, '5321c7d564405216c12f2e5b3b999718')

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

    def test_TC5(self):
            obj = EnterpriseManager()

            result = obj.register_project(
                'A58818501',
                'PROJ01',
                'TreasureHunters2',
                'HR',
                '21/01/2026',
                300000.00
            )

            print(result)
            self.assertEqual(result, '75752c286fa78d286fe482d0a3e3e687')

    def test_TC6(self):
        obj = EnterpriseManager()

        result = obj.register_project(
            'A58818501',
            'PROJ01',
            'TreasureHunters2',
            'HR',
            '21/05/2025',
            300000.00
        )

        print(result)
        self.assertEqual(result, 'ce8a4bf21407d6e589944a45c53decf3')

    def test_TC7(self):
        obj = EnterpriseManager()

        result = obj.register_project(
            'A58818501',
            'PROJ01',
            'TreasureHunters2',
            'HR',
            '21/05/2026',
            1000000.00
        )

        print(result)
        self.assertEqual(result, 'd49b99e410bbf18b9454785b24066acf')

