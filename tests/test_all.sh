#!/bin/bash

printf "testing /employees/\n"
/afs/nd.edu/user14/csesoft/2017-fall/anaconda3/bin/python3 test_employees_index.py

printf "\ntesting /employees/:employee_id\n"
/afs/nd.edu/user14/csesoft/2017-fall/anaconda3/bin/python3 test_employees.py

printf "\ntesting /jobs/ and /jobs/:job_title"
/afs/nd.edu/user14/csesoft/2017-fall/anaconda3/bin/python3 test_jobs.py

printf "\ntesting /salaries/ and /salaries/:job_title"
/afs/nd.edu/user14/csesoft/2017-fall/anaconda3/bin/python3 test_salaries.py