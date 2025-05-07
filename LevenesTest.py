import pandas as pd
import scipy.stats as stats
import sys

def levenes_test(data, group1_col, group2_col, group1_label, group2_label):
    """
    Performs Levene's test for equality of variances between two groups.

    Parameters:
        data (pd.DataFrame): The dataset containing the groups.
        group1_col (str): Column name of the first group.
        group2_col (str): Column name of the second group.
        group1_label (str): Label for the first group (for display).
        group2_label (str): Label for the second group (for display).

    Returns:
        str: A formatted string with the test statistic, p-value, and conclusion.
    """
    # Check if both groups have non-zero variance before performing the test
    if data[group1_col].var() != 0 and data[group2_col].var() != 0:
        stat, p = stats.levene(data[group1_col], data[group2_col], nan_policy='omit')
        return f"Levene's test ({group1_label} vs {group2_label}): Statistic={stat:.4f}, P-value={p:.4f}"
    else:
        return f"Levene's test ({group1_label} vs {group2_label}): One or both groups have zero variance; test not applicable."

def main():
    """
    Reads input data from a CSV file, runs the Levene's test for predefined group comparisons,
    and prints the results to the console.
    """
    
    # Ensure the script is run with a file path argument
    if len(sys.argv) < 2:
        print("Usage: python LevenesTest.py <data_file.csv>")
        sys.exit(1)  # Exit if no file path is provided

    file_path = sys.argv[1]  # Retrieve the CSV file path from command-line arguments
    data = pd.read_csv(file_path)  # Load dataset into a Pandas DataFrame

    # Define group comparisons: (column1, column2, label1, label2)
    comparisons = [
        ("Historical Lab 01", "Historical Lab 02", "Historical Lab 01", "Historical Lab 02"),
        ("Experiment Lab 01", "Experiment Lab 02", "Experiment Lab 01", "Experiment Lab 02"),
    ]

    # Perform Levene's test on each comparison
    results = []
    for comp in comparisons:
        result = levenes_test(data, *comp)
        results.append(result)

    # Print all test results
    print("\n".join(results))

if __name__ == "__main__":
    main()
