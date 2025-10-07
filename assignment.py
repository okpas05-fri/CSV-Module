
import csv

# task 1.

# headers = ["Name", "Age", "Grade"]
# students_data = [
#     {"Name": "Alice", "Age": 17, "Grade": "A"},
#     {"Name": "Bob", "Age": 16, "Grade": "B"},
#     {"Name": "Charlie", "Age": 18, "Grade": "A"},
#     {"Name": "David", "Age": 17, "Grade": "C"},
#     {"Name": "Eve", "Age": 16, "Grade": "A"},
#     {"Name": "Frank", "Age": 18, "Grade": "B"}
# ]

# # Create and write to the CSV file
# with open("students.csv", mode="w", newline="") as file:
#     writer = csv.DictWriter(file, fieldnames=headers)
#     writer.writeheader()  # Write the header row
#     writer.writerows(students_data)  # Write the student records

# print("students.csv created successfully with student data.")

#task2.
# reading from a csv file as a list:
# with open("students.csv", "r") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)

#task 3:
 # appending new data to the existing csv file:
# new_students = [["Peter", 40, "C"], ["Jonathan", 26, "A"]]
# with open("students.csv", "a", newline="") as latest_entry:
#     csv_writer = csv.writer(latest_entry)
#     csv_writer.writerows(new_students)
# print(f"New_students Appended successfully")    

 # reading the updated csv file:
# with open("students.csv", "r") as updated_file:
#         reader = csv.reader(updated_file)
#         for r in reader:
#             print(r)
        
# task 4.
# Read the CSV file and perform calculations
# total_students = 0
# grade_a_students = 0

# with open("students.csv", mode="r") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         total_students += 1
#         if row["Grade"] == "A":
#             grade_a_students += 1

# print(f"Total number of students: {total_students}")
# print(f"Number of students with Grade 'A': {grade_a_students}")

# task 5.

# # Sample student grades (replace with your actual data)
# student_grades = [92, 85, 78, 65, 95, 88, 72, 59, 81, 70, 99, 68, 75, 83, 90, 62]

# # Initialize a dictionary to store grade category counts
# grade_counts = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}

# # Categorize grades and count students in each category
# for grade in student_grades:
#     if grade >= 90:
#         grade_counts['A'] += 1
#     elif grade >= 80:
#         grade_counts['B'] += 1
#     elif grade >= 70:
#         grade_counts['C'] += 1
#     elif grade >= 60:
#         grade_counts['D'] += 1
#     else:
#         grade_counts['F'] += 1

# # Define the CSV file name
# csv_file_name = 'grades_summary.csv'

# # Write the summary to the CSV file
# with open(csv_file_name, 'w', newline='') as csvfile:
#     fieldnames = ['Grade Category', 'Number of Students']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

#     writer.writeheader()  # Write the header row
#     for category, count in grade_counts.items():
#         writer.writerow({'Grade Category': category, 'Number of Students': count})

# print(f"Grade summary written to {csv_file_name}")
                    



                

    
