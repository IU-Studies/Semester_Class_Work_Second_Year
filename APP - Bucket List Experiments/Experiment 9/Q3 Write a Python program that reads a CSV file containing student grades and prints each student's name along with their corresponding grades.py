""" Write a Python program that reads a CSV file containing student grades and prints each student's name
along with their corresponding grades. """

import csv

def read_student_grades(file_path):
    with open(file_path, mode='r') as file:
        csv_reader = csv.reader(file)  
        header = next(csv_reader)  

        for row in csv_reader:
            student_name = row[0]  
            grades = row[1:]  
            print("Student Name:", student_name)
            print("Grades:", grades)
            print()  

csv_file_path = 'student_grades.csv'

read_student_grades(csv_file_path)
