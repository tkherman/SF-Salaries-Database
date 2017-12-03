import unittest
import requests
import json
import urllib

class TestSalaries(unittest.TestCase):
    PORT_NUM = '51076'
    print("Testing port number: ", PORT_NUM)
    SITE_URL = "http://student04.cse.nd.edu:" + PORT_NUM
    SALARIES_URL = SITE_URL + "/salaries/"
    RESET_URL = SITE_URL + "/reset/"

    def reset_data(self):
        m = {}
        r = requests.put(self.RESET_URL, data=json.dumps(m))

    def is_json(self, resp):
        try:
            json.loads(resp)
            return True
        except ValueError:
            return False

    def test_salaries_get(self):
        self.reset_data()
        r = requests.get(self.SALARIES_URL)
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())

        self.assertEqual(resp['BestSalary'], 399211.275)
        self.assertEqual(resp['BestJob'], "GENERAL MANAGER-METROPOLITAN TRANSIT AUTHORITY")

    def test_salaries_get_title(self):
        self.reset_data()
        r = requests.get(self.SALARIES_URL + urllib.parse.quote("FIRE SAFETY INSPECTOR II"))
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())

        self.assertEqual(resp["AverageSalary"], 152596.47)


if __name__ == "__main__":
    unittest.main()
