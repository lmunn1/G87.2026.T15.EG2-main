from unittest import TestCase

from uc3m_consulting import EnterpriseManager, EnterpriseManagementException


class TestRF1(TestCase):
    def test_TC0(self):
       self.assertEqual(1, 1)

    def test_TC1(self):
        o=EnterpriseManager()
        result=o.register_project('B12345678','PRO01','car automatic development','HR','01/01/2026',60000)
        self.assertEqual(result,"af6c439801893f25b2d1d023ea9fe470")

    def test_TC2(self):
        o=EnterpriseManager()
        result=o.register_project('B12345678','PRO02CARTE','car automatic development','FINANCE','01/01/2026',60000)
        self.assertEqual(result,"c9d3fb3f2ad641e41dc34225b6a3be17")

    def test_TC3(self):
        o=EnterpriseManager()
        result=o.register_project('B12345678','PRO01','driving automatic development','LEGAL','01/01/2026',60000)
        self.assertEqual(result,"910762933f23cd672a812a56fc0271d3")

    def test_TC5(self):
        o=EnterpriseManager()
        with self.assertRaises(EnterpriseManagementException) as cm:
            o.register_project('44455666','PRO01','first test','LOGISTICS','01/01/2026',60000)
        self.assertEqual(cm.exception,"Wrong CIF value")

    def test_TC6(self):
        o=EnterpriseManager()
        with self.assertRaises(EnterpriseManagementException) as cm:
            o.register_project('B12345678','PRO01','first test','LOGISTICS','01/01/2026',200)
        self.assertEqual(cm.exception,"Low budget")
