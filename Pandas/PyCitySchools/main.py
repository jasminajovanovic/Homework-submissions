#!/usr/bin/env python
# coding: utf-8

# Dependencies and Setup
import pandas as pd
import numpy as np

# File to Load (Remember to Change These)
school_data_to_load = "Resources/schools_complete.csv"
student_data_to_load = "Resources/students_complete.csv"

# Read School and Student Data File and store into Pandas Data Frames
school_data = pd.read_csv(school_data_to_load)
student_data = pd.read_csv(student_data_to_load)

student_data.head()
# Combine the data into a single dataset
school_data_complete = pd.merge(student_data, school_data, how="left", on=["school_name", "school_name"])

total_schools = school_data.shape[0]
total_students = student_data.shape[0]
total_budget = school_data['budget'].sum()
total_math_pass = dict((student_data["math_score"]>70).value_counts())[True]
total_reading_pass = dict((student_data["reading_score"]>70).value_counts())[True]
average_math_score = student_data['math_score'].mean()
average_reading_score = student_data['reading_score'].mean()

district_summary = pd.DataFrame(
    {'Total Schools' : [total_schools],
    'Total Students' : [total_students],
    'Total Budget' : [total_budget],
    'Per Student budget' : [total_budget/total_students],
    'Average Math Score' : [round(average_math_score, 2)],
    'Average Reading Score': [round(average_reading_score,2)],
    '% Students Pass Math' : ['{0:.2%}'.format(total_math_pass/total_students)],
    '% Students Pass Reading' : ['{0:.2%}'.format(total_reading_pass/total_students)]})


district_summary

# spending_bins = [0, 585, 615, 645, 675]
# group_names = ["<$585", "$585-615", "$615-645", "$645-675"]
#
#
# size_bins = [0, 1000, 2000, 5000]
# group_names = ["Small (<1000)", "Medium (1000-2000)", "Large (2000-5000)"]
