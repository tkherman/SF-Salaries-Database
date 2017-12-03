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
