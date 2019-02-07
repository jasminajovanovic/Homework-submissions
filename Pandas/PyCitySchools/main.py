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

# Combine the data into a single dataset
school_data_complete = pd.merge(student_data, school_data, how="left", on=["school_name", "school_name"])

total_schools = school_data.shape[0]
print (f"There are a total of {total_schools} schools")
total_students = student_data.shape[0]
print (f"There are a total of {total_students} students")
total_budget = school_data['budget'].sum()
print (f"Total budget for all schools is: {total_budget}")
print (f"Per student budget is {total_budget/total_students:.2f}")
print (f"Average math score is {student_data['math_score'].mean():.2f}")
print (f"Average reading score is {student_data['reading_score'].mean():.2f}")


spending_bins = [0, 585, 615, 645, 675]
group_names = ["<$585", "$585-615", "$615-645", "$645-675"]


size_bins = [0, 1000, 2000, 5000]
group_names = ["Small (<1000)", "Medium (1000-2000)", "Large (2000-5000)"]



