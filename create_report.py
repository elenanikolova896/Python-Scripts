#We have a csv file called employee_list.csv. The goal of the script is to read the CSV file and generate a report with the total number of people in each department. 
To achieve this, we have divided the script into three functions.

#!/usr/bin/env python3
import csv

#the first function: read_employees() receives a CSV file as a parameter and returns a list of dictionaries from that file.

def read_employees(csv_file_location):
  #The main purpose of this dialect is to remove any leading spaces while parsing the CSV file.
    csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
    employee_list = []
    with open(csv_file_location) as file:
        employee_file = csv.DictReader(file, dialect='empDialect')
        for data in employee_file:
   #I need to Append the dictionaries to an empty initialised list employee_list as I iterate over the CSV file.
            employee_list.append(data)
    return employee_list

employee_list = read_employees('scripts/employee_list.csv')

#The second function process_data() should now receive the list of dictionaries, i.e., employee_list as a parameter and return a dictionary of department

def process_data(employee_list):
  #Inside the function, an empty list called department_list is initialized to hold department names.
    department_list = []
    for employee_data in employee_list:
        department_list.append(employee_data['Department'])

  #A new dictionary called department_data is initialized to hold the department names as keys and the counts as values.
    department_data = {}
    for department_name in set(department_list):
        department_data[department_name] = department_list.count(department_name)
    return department_data

dictionary = process_data(employee_list)

#Next is the function write_report. This function writes a dictionary of department: amount to a file.

def write_report(dictionary, report_file):
    with open(report_file, "w+") as f:
        for k in sorted(dictionary):
            f.write(str(k) + ':' + str(dictionary[k]) + '\n')

# Replace '<full_path_to_report_file>' with the actual full path where you want to create the report.txt file
write_report(dictionary, '<full_path_to_report_file>/report.txt')



