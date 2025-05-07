import pandas as pd
import scipy.stats as stats
import sys

def shapiro_wilk_test(data, column_name):
    """
    Performs the Shapiro-Wilk normality test on a given dataset column.

    Parameters:
        data (pd.DataFrame): The dataset containing the column to test.
        column_name (str): The name of the column to analyze.

    Returns:
        str: A formatted string with the test statistic, p-value, and normality conclusion.
    """
    # Check if variance is zero, as normality cannot be tested in that case
    if data[column_name].var() == 0:
        return f"Shapiro-Wilk Test for {column_name}: Zero variance; test not applicable."

    # Perform the Shapiro-Wilk test, dropping NaN values
    stat, p = stats.shapiro(data[column_name].dropna())
    
    # Determine whether data follows a normal distribution based on the p-value
    if p > 0.05:
        normality = "Normal"
    else: 
        normality = "Not Normal"
    
    return f"Shapiro-Wilk Test for {column_name}: Statistic={stat:.4f}, P-value={p:.4f}, {normality}"

def main():
    """
    Main function to:
    - Read a dataset from a CSV file.
    - Perform the Shapiro-Wilk test on predefined columns.
    - Print the test results.
    """
    # Ensure the script is run with a file path argument
    if len(sys.argv) < 2:
        print("Usage: python ShapiroWilkNormalityTest.py <data_file.csv>")
        sys.exit(1)  # Exit if no file path is provided

    file_path = sys.argv[1]  # Retrieve file path from command-line arguments
    data = pd.read_csv(file_path)  # Load dataset into a Pandas DataFrame

    # Define columns to test for normality
    columns_to_test = ["Historical Lab 01", "Experiment Lab 01", "Historical Lab 02", "Experiment Lab 02"]

    # Perform the Shapiro-Wilk test on each column
    results = []
    for col in columns_to_test:
        result = shapiro_wilk_test(data, col)
        results.append(result)

    # Print all test results
    print("\n".join(results))

if __name__ == "__main__":
    main()
