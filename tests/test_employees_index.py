import unittest
import requests
import json

class TestEmployees(unittest.TestCase):

    PORT_NUM = '51076' #change port number to match your port number
    print("Testing Port number: ", PORT_NUM)
    SITE_URL = 'http://student04.cse.nd.edu:' + PORT_NUM
    EMPLOYEES_URL = SITE_URL + '/employees/'
    RESET_URL = SITE_URL + '/reset/'

    def reset_data(self):
        e = {}
        r = requests.put(self.RESET_URL, data = json.dumps(e))

    def is_json(self, resp):
        try:
            json.loads(resp)
            return True
        except ValueError:
            return False

    def test_employees_index_get(self):
        self.reset_data()
        r = requests.get(self.EMPLOYEES_URL)
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())

        employees = resp['employees']
        for employee in employees:
            if employee['Id'] == 13.0:
                testemployee = employee

        self.assertEqual(testemployee['Id'], 13.0)
        self.assertEqual(testemployee['EmployeeName'], 'EDWARD HARRINGTON')
        self.assertEqual(testemployee['JobTitle'], 'EXECUTIVE CONTRACT EMPLOYEE')
        self.assertEqual(testemployee['BasePay'], 294580.02)
        self.assertEqual(testemployee['TotalPay'], 294580.02)
        self.assertEqual(testemployee['Year'], 2011.0)
        self.assertEqual(testemployee['Agency'], 'San Francisco')

    def test_employees_index_post(self):
        self.reset_data()

        e = {}
        e['Id'] = 148654.0
        e['EmployeeName'] = 'BOB SMITH'
        e['JobTitle'] = 'WAITER'
        e['BasePay'] = 100000.0
        e['TotalPay'] = 101000.0
        e['Year'] = 2011.0
        e['Agency'] = 'San Francisco'
        r = requests.post(self.EMPLOYEES_URL, data = json.dumps(e))
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())
        self.assertEqual(resp['result'], 'success')
        #self.assertEqual(resp['Id'] = '148654.0')

        r = requests.get(self.EMPLOYEES_URL + str(int(e['Id'])))
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())
        self.assertEqual(resp['Id'], e['Id'])
        self.assertEqual(resp['EmployeeName'], e['EmployeeName'])
        self.assertEqual(resp['JobTitle'], e['JobTitle'])
        self.assertEqual(resp['BasePay'], e['BasePay'])
        self.assertEqual(resp['TotalPay'], e['TotalPay'])
        self.assertEqual(resp['Year'], e['Year'])
        self.assertEqual(resp['Agency'], e['Agency'])

    def test_employees_index_delete(self):
        self.reset_data()
        
        e = {}
        r = requests.delete(self.EMPLOYEES_URL, data = json.dumps(e))
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())
        self.assertEqual(resp['result'], 'success')

        r = requests.get(self.EMPLOYEES_URL)
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())
        employees = resp['employees']
        self.assertFalse(employees)

if __name__ == "__main__":
    unittest.main()
