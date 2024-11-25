Jacob Hawkins
11/24/2024

----

Program Description: 
- This program will analyze exam grades from a CSV file, calculate various statistics, pass/fail counts, and the overall pass percentage.

----

Logical Steps:
1. Load the data
2. Extract exam scores
3. Print the first five rows of the data
4. Compute the mean, median, SD, minimum and maximum for each exam column
5. Compute the overall of each stat listed in #4 above
6. Determine pass/fail counts
7. Calculate overall pass percentage
8. Display results

----

Variables:
1. file_path: the file path to the CSV
2. df: a pandas dataframe that golds the data loaded from the CSV
3. exam_scores: a NumPy array containing only the numerical exam scores from the dataframe
4. exam_statistics: a dictionary storing statistical calculations
5. overall_statistics: a dictionary containing statistical calculations
6. pass_fail_counts: a dictiopnary that holds the number of students who passed and failed
7. total_students: the total number of grades
8. pass_percentage: the percentage of grades across all exams that are above the score of 60. 

----

Functions:
1. analyze_grade(file_path)
	Description: Reads the CSV file, processes the data to calculate the results required, and displays it.
	Parameters: file_path: the path to the CSV file.
	Returns: none.

----

Link to repository: https://github.com/sometimeslingual/12a
