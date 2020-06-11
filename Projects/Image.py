#!/usr/bin/env python3
import csv

def read_employees(filename):
   csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
   employee_file = csv.DictReader(open(filename), dialect = 'empDialect')
   employee_list = []
   for data in employee_file:
     employee_list.append(data)
   return employee_list

def process_data(employee_list):
   department_list = []
   for employee_data in employee_list:
     department_list.append(employee_data['Department'])
   department_data = {}
   for department_name in set(department_list):

