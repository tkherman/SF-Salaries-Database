import sys

class _salaries_database:

    def __init__(self):
        self.employees = dict()
        self.jobs = dict()

    """
        Employees
            - store employees information in a dictionary
            - key = id
            - value = a dictionary of employee information with keys:
              Id, EmployeeName, JobTitle, BasePay, TotalPay, Year, Agency
    """
    def load_employees(self, salaries_file):
        with open(salaries_file, "r") as f:
            # Get column headers
            columns = next(f).split(",")

            for line in f:
                employee = line.rstrip().split(",")

                # Combine fields that begins with " and seaparted by ,
                if employee[1][0] == '"':
                    index = 2
                    while index < len(employee) and employee[index][-1] != '"':
                        index += 1
                    employee[1:index+1] = ["".join(employee[1:index+1])]

                if employee[2][0] == '"':
                    index = 3
                    while index < len(employee) and employee[index][-1] != '"':
                        index += 1
                    employee[2:index+1] = ["".join(employee[2:index+1])]

                info =  dict()

                for i in range(len(columns)):
                    if employee[i].replace(".", "").replace("-", "").isdigit():
                        info[columns[i]] = float(employee[i])
                    else:
                        info[columns[i]] = employee[i]

                del info['OvertimePay']
                del info['OtherPay']
                del info['Benefits']
                del info['TotalPayBenefits']
                del info['Notes']
                del info['Status\n']

                self.employees[info['Id']] = info

    # Return a dictionary of info on the employee with that eid
    def get_employee(self, eid):
        return self.employees.get(eid)

    # Return a list of eids
    def get_employees(self):
        return self.employees.keys()

    # Set the employee with eid
    def set_employee(self, eid, data):
        # If employee exist under eid, remove the eid from its job's list
        if self.employees.get(eid):
            current_employee = self.employees[eid]
            self.jobs[current_employee['JobTitle']].remove(current_employee['Id'])

        self.employees[eid] = data

        # Update self.jobs with new employee
        try:
            self.jobs[data['JobTitle']].append(data['Id'])
        except KeyError:
            self.jobs[data['JobTitle']] = [data['Id']]

    # Delete the employee specified by eid
    def delete_employee(self, eid):
        if self.employees.get(eid):
            current_employee = self.employees[eid]
            self.jobs[current_employee['JobTitle']].remove(current_employee['Id'])

        del self.employees[eid]

    # Clear self.smployee
    def delete_all_employees(self):
        self.employees.clear()

    """
        JOBS
            - store employee Ids of different jobs
            - store as dictionary
            - key = JobTitle
            - value = list of Ids
    """
    def load_jobs(self, salaries_file):
        with open(salaries_file, "r") as f:
            # Get column headers
            columns = next(f).split(",")

            for line in f:
                employee = line.rstrip().split(",")

                # Combine fields that begins with " and seaparted by ,
                if employee[1][0] == '"':
                    index = 2
                    while index < len(employee) and employee[index][-1] != '"':
                        index += 1
                    employee[1:index+1] = ["".join(employee[1:index+1])]

                if employee[2][0] == '"':
                    index = 3
                    while index < len(employee) and employee[index][-1] != '"':
                        index += 1
                    employee[2:index+1] = ["".join(employee[2:index+1])]

                try:
                    self.jobs[employee[2]].append(float(employee[0]))
                except KeyError:
                    self.jobs[employee[2]] = [float(employee[0])]

    # Returns a list of jobs
    def get_jobs(self):
        return self.jobs.keys()

    # Returns a list of eid of employee under the job title
    def get_job(self, JobTitle):
        return self.jobs.get(JobTitle)

    # Return average salary of a job
    def get_average_totalpay(self, JobTitle):
        avg_pay = 0

        for eid in self.jobs[JobTitle]:
            avg_pay += self.employees[eid]['TotalPay']

        avg_pay /= len(self.jobs[JobTitle])

        return avg_pay

    # Return average BasePay of a job
    def get_average_basepay(self, JobTitle):
        avg_pay = 0

        for eid in self.jobs[JobTitle]:
            avg_pay += self.employees[eid]['BasePay']

        avg_pay /= len(self.jobs[JobTitle])

        return avg_pay

    # Return a dictionary of "BestSalary" and "BestJob", calculated using TotalPay
    def get_best_salary_job(self):
        result = {'BestSalary': 0, 'BestJob': ""}

        # Loop through each jobs in database
        for job_title in  self.get_jobs():
            # Calculate average salary for each job
            avg_salary = self.get_average_totalpay(job_title)

            if avg_salary > result['BestSalary']:
                result['BestSalary'] = avg_salary
                result['BestJob'] = job_title

        return result

    # Return a dictionary of "MostPopularJob", "EmployeeCount:"
    def get_most_popular_job(self):
        result = {'MostPopularJob': "", 'EmployeeCount': 0}

        # Loop through each jobs in database
        for job_title in self.get_jobs():
            if len(self.jobs[job_title]) > result['EmployeeCount']:
                result['EmployeeCount'] = len(self.jobs[job_title])
                result['MostPopularJob'] = job_title

        return result
