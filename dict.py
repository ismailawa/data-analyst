#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 10:48:28 2024

@author: Ismailawa Aliyu
"""

student = {"fullname": "Aisha Abubakar", "age": 25, "gender": "Female", "grades": [100,90,87,67]}

print(type(student))
#<class 'dict'>
print(student)
#{'fullname': 'Aisha Abubakar', 'age': 25, 'gender': 'Female', 'grades': [100, 90, 87, 67]}

print(student['fullname'])
#Aisha Abubakar

print(student['grades'][0])
#100

students = [
    {"fullname": "Aisha Abubakar", "age": 25, "gender": "Female", "grades": [100,90,87,67]},
    {"fullname": "Joan Adamu", "age": 28, "gender": "Female", "grades": [100,90,87,67]}
 ]

print(students[0][0])
#print(students[0]["grades"][0])








