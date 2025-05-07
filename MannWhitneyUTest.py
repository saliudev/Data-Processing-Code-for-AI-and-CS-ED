import pandas as pd
import scipy.stats as stats
import sys

def mann_whitney_u_test(data, group1_col, group2_col, group1_label, group2_label, alternative):
    """
    Perform the Mann-Whitney U test to compare the distributions of two independent groups.

    Parameters:
    data (pd.DataFrame): The pandas DataFrame containing the data.
    group1_col (str): The name of the column for the first group.
    group2_col (str): The name of the column for the second group.
    group1_label (str): The label/name for the first group (for display purposes).
    group2_label (str): The label/name for the second group (for display purposes).
    alternative (str): The type of alternative hypothesis ("less", "greater", or "two-sided").

    Returns:
    str: A formatted string displaying the result of the Mann-Whitney U test including the test statistic, p-value, and significance.
    
    """
    # Perform the Mann-Whitney U test on the provided groups and calculate the p-value
    stat, p = stats.mannwhitneyu(data[group1_col].dropna(), data[group2_col].dropna(), alternative=alternative, method='exact')
    
    # Determine significance based on the p-value
    if p < 0.05:
        sig = 'Significant'
    else: 
        sig = 'Not Significant'
    
    # Return the formatted result of the Mann-Whitney U test
    return f"Mann-Whitney U Test ({group1_label} vs {group2_label}): Statistic={stat:.4f}, P-value={p:.4f}, {sig}"

def main():
    """
    Reads input data from a CSV file, runs the Mann-Whitney U test for predefined group comparisons,
    and prints the results to the console.
    """
    
    # Ensure the script is run with a file path argument
    if len(sys.argv) < 2:
        print("Usage: python ManWhiteneyUTest.py <data_file.csv>")
        sys.exit(1)  # Exit if no file path is provided
    
    # Read the data from the specified CSV file into a pandas DataFrame
    file_path = sys.argv[1]  # Retrieve file path from command-line arguments
    data = pd.read_csv(file_path)

    # Define the comparisons between groups to perform the Mann-Whitney U test on
    comparisons = [
        # Comparing two experimental labs to check if one consistently has lower values than the other.
        ("Experiment Lab 01", "Experiment Lab 02", "Experiment Lab 01", "Experiment Lab 02", "less"),
        
        # Comparing an experimental lab to its historical counterpart to see if the experimental method shows improvement.
        ("Experiment Lab 01", "Historical Lab 01", "Experiment Lab 01", "Historical Lab 01", "greater"),
        
        # Comparing the second experimental lab to its historical counterpart to analyze performance differences.
        ("Experiment Lab 02", "Historical Lab 02", "Experiment Lab 02", "Historical Lab 02", "greater"),
    ]


    # Initialize an empty list to store results
    results = []
    
    # Loop through the comparisons and perform the Mann-Whitney U test for each pair of groups
    for comp in comparisons:
        result = mann_whitney_u_test(data, *comp) # Uses unpacking operator to unpack arguments in the array to the function
        results.append(result)

    # Print all the results, one per line
    print("\n".join(results))

if __name__ == "__main__":
    main()