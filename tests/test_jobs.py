import unittest
import requests
import json

class TestJobs(unittest.TestCase):
    PORT_NUM = '51076'
    print("Testing port number: ", PORT_NUM)
    SITE_URL = "http://student04.cse.nd.edu:" + PORT_NUM
    JOBS_URL = SITE_URL + "/jobs/"

if __name__ == "__main__":
    unittest.main()
