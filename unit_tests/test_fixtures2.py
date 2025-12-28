'''
Testing class level fixtures. We define an employee class with specific fields that can be
populated. After that we get create a function to create empoyees from CSV files and setup 
a test with the SAMPLE_CSV.
'''
import os
import unittest
from tempfile import NamedTemporaryFile
import csv

SAMPLE_CSV = '''name,age,salary,job
Alice,25,50000,Analyst
Cooper,47,60000,Engineer
Ben,51,100000,Manager
Catherine,60,150000,CEO
'''

class Employee:

    __slots__ = ['name', 'age', 'salary', 'job']

    def __init__(self, name, age, salary, job):
        self.name = name
        self.age = age
        self.salary = salary
        self.job = job


def create_employees_from_csv(file_path):
    with open(file_path, 'r') as f:
        reader = csv.DictReader(f)
        employees = []

        for row in reader:
            employees.append(Employee(
                name=row['name'],
                age=int(row['age']),
                salary=float(row['salary']),
                job=row['job']
            ))

    return employees


class TestCreateEmployeesFromCSV(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.temp_file = NamedTemporaryFile(
            delete=False,
            mode='w',
            newline='',
            suffix='.csv'
        )
        cls.temp_file_name = cls.temp_file.name
        cls.temp_file.write(SAMPLE_CSV)
        cls.temp_file.close()
        cls.employees = create_employees_from_csv(cls.temp_file_name)
    
    @classmethod
    def tearDownClass(cls):
        os.remove(cls.temp_file_name)

    def test_total_employees(self):
        self.assertEqual(len(self.employees), 4)

    def test_test_employee_attributes(self):
        self.assertEqual(self.employees[0].name, 'Alice')
        self.assertEqual(self.employees[0].age, 25)
        self.assertEqual(self.employees[0].salary, 50000)
        self.assertEqual(self.employees[0].job, 'Analyst')

    def test_employee_name(self):
        self.assertEqual(self.employees[1].name, 'Cooper')
        self.assertEqual(self.employees[2].name, 'Ben')
        self.assertEqual(self.employees[3].name, 'Catherine')


if __name__=='__main__':
    unittest.main(verbosity=2)