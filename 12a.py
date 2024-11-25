import numpy as np
import pandas as pd

def analyze_grades(file_path):
    # load the data from the CSV file into a numpy array
    df = pd.read_csv(file_path)

    # extracting exam scores, ignoring the first two columns
    exam_scores = df.iloc[:, 2:].to_numpy()

    # print the first few rows of the dataset to understand its structure
    print("First Five Rows of the Dataset:")
    print(exam_scores[:5])
    print()

    # calculate statistics for each exam
    exam_statistics = {
        "Mean": np.mean(exam_scores, axis=0),
        "Median": np.median(exam_scores, axis=0),
        "Standard Deviation": np.std(exam_scores, axis=0),
        "Minimum": np.min(exam_scores, axis=0),
        "Maximum": np.max(exam_scores, axis=0),
    }

    print("Exam Statistics:")
    for stat, values in exam_statistics.items():
        print(f"{stat}: {values}")
    print()

    # calculate overall statistics for the entire dataset
    overall_statistics = {
        "Mean": np.mean(exam_scores),
        "Median": np.median(exam_scores),
        "Standard Deviation": np.std(exam_scores),
        "Minimum": np.min(exam_scores),
        "Maximum": np.max(exam_scores),
    }

    print("Overall Statistics:")
    for stat, value in overall_statistics.items():
        print(f"{stat}: {value}")
    print()

    # determine the number of students who passed and failed each exam
    pass_fail_counts = {
        "Pass": np.sum(exam_scores >= 60, axis=0),
        "Fail": np.sum(exam_scores < 60, axis=0),
    }

    print("Pass/Fail Counts:")
    for result, counts in pass_fail_counts.items():
        print(f"{result}: {counts}")
    print()

    # calculate the overall pass percentage across all exams
    total_students = exam_scores.size
    pass_percentage = (np.sum(exam_scores >= 60) / total_students) * 100

    print(f"Overall Pass Percentage: {pass_percentage:.2f}%")

# file path to the CSV file
file_path = "grades.csv"

# call the function
if __name__ == "__main__":
    analyze_grades(file_path)
