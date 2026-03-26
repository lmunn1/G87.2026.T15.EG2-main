import os
import unittest
from uc3m_consulting import EnterpriseManager, EnterpriseManagementException


class TestEnterpriseManager(unittest.TestCase):
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

    def test_TC8(self):
        obj = EnterpriseManager()
        with self.assertRaises(EnterpriseManagementException):
            obj.register_project(
                company_cif=123456789,
                project_acronym='PROJ01',
                project_description='TreasureHunters2',
                department='HR',
                date='21/05/2026',
                budget=300000.00
            )

    def test_TC9(self):
        obj = EnterpriseManager()
        with self.assertRaises(EnterpriseManagementException):
            obj.register_project(
                company_cif='A58818502',
                project_acronym='PROJ01',
                project_description='TreasureHunters2',
                department='HR',
                date='21/05/2026',
                budget=300000.00
            )

    def test_TC10(self):
        obj = EnterpriseManager()
        with self.assertRaises(EnterpriseManagementException):
            obj.register_project(
                company_cif='A5881850',
                project_acronym='PROJ01',
                project_description='TreasureHunters2',
                department='HR',
                date='21/05/2026',
                budget=300000.00
            )

    def test_TC11(self):
        obj = EnterpriseManager()
        with self.assertRaises(EnterpriseManagementException):
            obj.register_project(
                company_cif='A588185018',
                project_acronym='PROJ01',
                project_description='TreasureHunters2',
                department='FINANCE',
                date='21/05/2026',
                budget=300000.00
            )

    def test_TC12(self):
        obj = EnterpriseManager()
        with self.assertRaises(EnterpriseManagementException):
            obj.register_project(
                company_cif='358818501',
                project_acronym='PROJ01',
                project_description='TreasureHunters2',
                department='FINANCE',
                date='21/05/2026',
                budget=300000.00
            )

    def test_TC13(self):
        obj = EnterpriseManager()
        with self.assertRaises(EnterpriseManagementException):
            obj.register_project(
                company_cif='A5881K501',
                project_acronym='PROJ01',
                project_description='TreasureHunters2',
                department='FINANCE',
                date='21/05/2026',
                budget=300000.00
            )

    def test_TC14(self):
        obj = EnterpriseManager()
        with self.assertRaises(EnterpriseManagementException):
            obj.register_project(
                company_cif='A58818501',
                project_acronym=12345,
                project_description='TreasureHunters2',
                department='FINANCE',
                date='21/05/2026',
                budget=300000.00
            )

    def test_TC15(self):
        obj = EnterpriseManager()
        with self.assertRaises(EnterpriseManagementException):
            obj.register_project(
                company_cif='A58818501',
                project_acronym='PROJ',
                project_description='TreasureHunters2',
                department='HR',
                date='21/05/2026',
                budget=300000.00
            )

    def test_TC16(self):
        obj = EnterpriseManager()
        with self.assertRaises(EnterpriseManagementException):
            obj.register_project(
                company_cif='A58818501',
                project_acronym='NEWPROJECTS',
                project_description='TreasureHunters2',
                department='HR',
                date='21/05/2026',
                budget=300000.00
            )

    def test_TC17(self):
        obj = EnterpriseManager()
        with self.assertRaises(EnterpriseManagementException):
            obj.register_project(
                company_cif='A58818501',
                project_acronym='PR 01',
                project_description='TreasureHunters2',
                department='HR',
                date='21/05/2026',
                budget=300000.00
            )

    def test_TC18(self):
        obj = EnterpriseManager()
        with self.assertRaises(EnterpriseManagementException):
            obj.register_project(
                company_cif='A58818501',
                project_acronym='PROJ01',
                project_description=12345,
                department='HR',
                date='21/05/2026',
                budget=300000.00
            )

    def test_TC19(self):
        obj = EnterpriseManager()
        with self.assertRaises(EnterpriseManagementException):
            obj.register_project(
                company_cif='A58818501',
                project_acronym='PROJ01',
                project_description='Project01',
                department='HR',
                date='21/05/2026',
                budget=300000.00
            )

    def test_TC20(self):
        obj = EnterpriseManager()
        with self.assertRaises(EnterpriseManagementException):
            obj.register_project(
                company_cif='A58818501',
                project_acronym='PROJ01',
                project_description='DescriptionThatDescriptionThis1',
                department='HR',
                date='21/05/2026',
                budget=300000.00
            )

    def test_TC21(self):
        obj = EnterpriseManager()
        with self.assertRaises(EnterpriseManagementException):
            obj.register_project(
                company_cif='A58818501',
                project_acronym='PROJ01',
                project_description='TreasureHunters2',
                department=1234,
                date='21/05/2026',
                budget=300000.00
            )

    def test_TC22(self):
        obj = EnterpriseManager()
        with self.assertRaises(EnterpriseManagementException):
            obj.register_project(
                company_cif='A58818501',
                project_acronym='PROJ01',
                project_description='TreasureHunters2',
                department='MATH',
                date='21/05/2026',
                budget=300000.00
            )

    def test_TC23(self):
        obj = EnterpriseManager()
        with self.assertRaises(EnterpriseManagementException):
            obj.register_project(
                company_cif='A58818501',
                project_acronym='PROJ01',
                project_description='TreasureHunters2',
                department='HR',
                date=21012026,
                budget=300000.00
            )

    def test_TC24(self):
        obj = EnterpriseManager()
        with self.assertRaises(EnterpriseManagementException):
            obj.register_project(
                company_cif='A58818501',
                project_acronym='PROJ01',
                project_description='TreasureHunters2',
                department='HR',
                date='2026/01/21',
                budget=300000.00
            )

    def test_TC25(self):
        obj = EnterpriseManager()
        with self.assertRaises(EnterpriseManagementException):
            obj.register_project(
                company_cif='A58818501',
                project_acronym='PROJ01',
                project_description='TreasureHunters2',
                department='HR',
                date='00/01/2026',
                budget=300000.00
            )

    def test_TC26(self):
        obj = EnterpriseManager()
        with self.assertRaises(EnterpriseManagementException):
            obj.register_project(
                company_cif='A58818501',
                project_acronym='PROJ01',
                project_description='TreasureHunters2',
                department='HR',
                date='32/01/2026',
                budget=300000.00
            )

    def test_TC27(self):
        obj = EnterpriseManager()
        with self.assertRaises(EnterpriseManagementException):
            obj.register_project(
                company_cif='A58818501',
                project_acronym='PROJ01',
                project_description='TreasureHunters2',
                department='HR',
                date='21/00/2026',
                budget=300000.00
            )

    def test_TC28(self):
        obj = EnterpriseManager()
        with self.assertRaises(EnterpriseManagementException):
            obj.register_project(
                company_cif='A58818501',
                project_acronym='PROJ01',
                project_description='TreasureHunters2',
                department='HR',
                date='21/13/2026',
                budget=300000.00
            )

    def test_TC29(self):
        obj = EnterpriseManager()
        with self.assertRaises(EnterpriseManagementException):
            obj.register_project(
                company_cif='A58818501',
                project_acronym='PROJ01',
                project_description='TreasureHunters2',
                department='HR',
                date='21/01/2024',
                budget=300000.00
            )

    def test_TC30(self):
        obj = EnterpriseManager()
        with self.assertRaises(EnterpriseManagementException):
            obj.register_project(
                company_cif='A58818501',
                project_acronym='PROJ01',
                project_description='TreasureHunters2',
                department='HR',
                date='21/01/2028',
                budget=300000.00
            )

    def test_TC31(self):
        obj = EnterpriseManager()
        with self.assertRaises(EnterpriseManagementException):
            obj.register_project(
                company_cif='A58818501',
                project_acronym='PROJ01',
                project_description='TreasureHunters2',
                department='HR',
                date='29/02/2025',
                budget=300000.00
            )

    def test_TC32(self):
        obj = EnterpriseManager()
        with self.assertRaises(EnterpriseManagementException):
            obj.register_project(
                company_cif='A58818501',
                project_acronym='PROJ01',
                project_description='TreasureHunters2',
                department='HR',
                date='09/01/2023',
                budget=300000.00
            )

    def test_TC33(self):
        obj = EnterpriseManager()
        with self.assertRaises(EnterpriseManagementException):
            obj.register_project(
                company_cif='A58818501',
                project_acronym='PROJ01',
                project_description='TreasureHunters2',
                department='HR',
                date='21/05/2026',
                budget='300000.00'
            )

    def test_TC34(self):
        obj = EnterpriseManager()
        with self.assertRaises(EnterpriseManagementException):
            obj.register_project(
                company_cif='A58818501',
                project_acronym='PROJ01',
                project_description='TreasureHunters2',
                department='HR',
                date='21/05/2026',
                budget=49999.99
            )

    def test_TC35(self):
        obj = EnterpriseManager()
        with self.assertRaises(EnterpriseManagementException):
            obj.register_project(
                company_cif='A58818501',
                project_acronym='PROJ01',
                project_description='TreasureHunters2',
                department='HR',
                date='21/05/2026',
                budget=1000000.01
            )

    def test_TC36(self):
        obj = EnterpriseManager()
        with self.assertRaises(EnterpriseManagementException):
            obj.register_project(
                company_cif='A58818501',
                project_acronym='PROJ01',
                project_description='TreasureHunters2',
                department='HR',
                date='21/05/2026',
                budget=300000.0
            )

    def test_TC37(self):
        obj = EnterpriseManager()
        with self.assertRaises(EnterpriseManagementException):
            obj.register_project(
                company_cif='A58818501',
                project_acronym='PROJ01',
                project_description='TreasureHunters2',
                department='HR',
                date='21/05/2026',
                budget=300000.001
            )