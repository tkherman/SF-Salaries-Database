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

	def test_employees_get(self):
		self.reset_data()
		employee_id = 13.0
		r = requests.get(self.EMPLOYEES_URL + str(int(employee_id)))
		self.assertTrue(self.is_json(r.content.decode('utf-8')))
		resp = json.loads(r.content.decode('utf-8'))
		self.assertEqual(resp['Id'], 13.0)
		self.assertEqual(resp['EmployeeName'], 'EDWARD HARRINGTON')
		self.assertEqual(resp['JobTitle'], 'EXECUTIVE CONTRACT EMPLOYEE')
		self.assertEqual(resp['BasePay'], 294580.02)
		self.assertEqual(resp['TotalPay'], 294580.02)
		self.assertEqual(resp['Year'], 2011.0)
		self.assertEqual(resp['Agency'], 'San Francisco')

	def test_employees_put(self):
		self.reset_data()
		employee_id = 20.0
		r = requests.get(self.EMPLOYEES_URL + str(int(employee_id)))
		self.assertTrue(self.is_json(r.content.decode('utf-8')))
		resp = json.loads(r.content.decode('utf-8'))
		self.assertEqual(resp['Id'], 20.0)
		self.assertEqual(resp['EmployeeName'], 'ELLEN MOFFATT')
		self.assertEqual(resp['JobTitle'], 'ASSISTANT MEDICAL EXAMINER')
		self.assertEqual(resp['BasePay'], 257510.59)
		self.assertEqual(resp['TotalPay'], 274550.25)
		self.assertEqual(resp['Year'], 2011.0)
		self.assertEqual(resp['Agency'], 'San Francisco')

		e = {}
		e['Id'] = 20.0
		e['EmployeeName'] = 'BOB SMITH'
		e['JobTitle'] = 'WAITER'
		e['BasePay'] = 100000.0
		e['TotalPay'] = 101000.0
		e['Year'] = 2011.0
		e['Agency'] = 'San Francisco'
		r = requests.put(self.EMPLOYEES_URL + str(int(employee_id)), data = json.dumps(e))
		self.assertTrue(self.is_json(r.content.decode('utf-8')))
		resp = json.loads(r.content.decode('utf-8'))
		self.assertEqual(resp['result'], 'success')

		r = requests.get(self.EMPLOYEES_URL + str(int(employee_id)))
		self.assertTrue(self.is_json(r.content.decode('utf-8')))
		resp = json.loads(r.content.decode('utf-8'))
		self.assertEqual(resp['Id'], e['Id'])
		self.assertEqual(resp['EmployeeName'], e['EmployeeName'])
		self.assertEqual(resp['JobTitle'], e['JobTitle'])
		self.assertEqual(resp['BasePay'], e['BasePay'])
		self.assertEqual(resp['TotalPay'], e['TotalPay'])
		self.assertEqual(resp['Year'], e['Year'])
		self.assertEqual(resp['Agency'], e['Agency'])

	def test_employees_delete(self):
		self.reset_data()
		employee_id = 30.0

		e = {}
		r = requests.delete(self.EMPLOYEES_URL + str(int(employee_id)), data = json.dumps(e))
		self.assertTrue(self.is_json(r.content.decode('utf-8')))
		resp = json.loads(r.content.decode('utf-8'))
		self.assertEqual(resp['result'], 'success')

		r = requests.get(self.EMPLOYEES_URL + str(int(employee_id)))
		self.assertTrue(self.is_json(r.content.decode('utf-8')))
		resp = json.loads(r.content.decode('utf-8'))
		self.assertEqual(resp['result'], 'error')

if __name__ == "__main__":
	unittest.main()