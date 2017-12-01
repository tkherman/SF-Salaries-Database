import unittest
import requests
import json
import urllib

class TestJobs(unittest.TestCase):
    PORT_NUM = '51076'
    print("Testing port number: ", PORT_NUM)
    SITE_URL = "http://student04.cse.nd.edu:" + PORT_NUM
    JOBS_URL = SITE_URL + "/jobs/"
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

    def test_jobs_get(self):
        self.reset_data()
        r = requests.get(self.JOBS_URL)
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())

        found = False
        for jobtitle in resp['JobTitles']:
            if jobtitle == "GENERAL MANAGER-METROPOLITAN TRANSIT AUTHORITY":
                found = True

        self.assertTrue(found)
    
    def test_jobs_get_title(self):
        self.reset_data()
        r = requests.get(self.JOBS_URL + urllib.parse.quote("GENERAL MANAGER-METROPOLITAN TRANSIT AUTHORITY"))
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())

        self.assertEqual([1.0, 84.0], resp['Ids'])

    def test_delete_title(self):
        self.reset_data()
        r = requests.delete(self.JOBS_URL + urllib.parse.quote("GENERAL MANAGER-METROPOLITAN TRANSIT AUTHORITY"))
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())

        self.assertEqual('success', resp['result'])

        r = requests.get(self.JOBS_URL + "1")
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())
        self.assertEqual('error', resp['result'])
        
        r = requests.get(self.JOBS_URL + "84")
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())
        self.assertEqual('error', resp['result'])
        

if __name__ == "__main__":
    unittest.main()
