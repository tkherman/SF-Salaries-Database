from _salaries_database import _salaries_database
import unittest

class TestSalariesDatabase(unittest.TestCase):

    sdb = _salaries_database()

    def reset_data(self):
        self.sdb.delete_all_employees()
        self.sdb.load_employees("Salaries.csv")
        self.sdb.load_jobs("Salaries.csv")

    def test_get_employee(self):
        self.reset_data()
        employee = self.sdb.get_employee(1)
        self.assertEqual(employee['Id'], 1)
        self.assertEqual(employee['EmployeeName'], "NATHANIEL FORD")
        self.assertEqual(employee['JobTitle'], "GENERAL MANAGER-METROPOLITAN TRANSIT AUTHORITY")
        self.assertEqual(employee['BasePay'], 167411.18)

    def test_set_employee(self):
        self.reset_data()
        employee = self.sdb.get_employee(1)
        employee['EmployeeName'] = "Herman Tong"
        self.sdb.set_employee(1, employee)
        employee = self.sdb.get_employee(1)
        self.assertEqual(employee['EmployeeName'], "Herman Tong")
        self.assertEqual(employee['JobTitle'], "GENERAL MANAGER-METROPOLITAN TRANSIT AUTHORITY")

    def test_delelte_employee(self):
        self.reset_data()
        self.sdb.delete_employee(1)
        employee = self.sdb.get_employee(1)
        self.assertEqual(employee, None)

    def test_get_job(self):
        self.reset_data()
        employee = dict()
        employee['Id'] = 2.0
        employee['EmployeeName'] = "Herman Tong"
        employee['JobTitle'] = "Software Engineering Intern"
        employee["BasePay"] = 5.0
        employee["TotalPay"] = 6.0
        employee["Year"] = 2017
        employee["Agency"] = "Seattle"
        self.sdb.set_employee(2.0, employee)
        job = self.sdb.get_job("Software Engineering Intern")
        self.assertEqual(job[0], 2.0)

if __name__ == "__main__":
    unittest.main()
