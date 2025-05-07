# Data-Processing-Code-for-AI-and-CS-ED

This repository contains three Python scripts that perform statistical tests used in the **Generative AI and Education** research group at **Harrisburg University of Science and Technology**:

1. **Levene's Test** (`LevenesTest.py`): Tests for equality of variances between two groups.
2. **Mann-Whitney U Test** (`MannWhitneyUTest.py`): Compares the distributions of two independent groups.
3. **Shapiro-Wilk Normality Test** (`ShapiroWilkNormalityTest.py`): Tests whether a dataset follows a normal distribution.

## Requirements

The scripts require Python 3 and the following dependencies:
- `pandas`
- `scipy`

To install the required packages, run:

```
pip install -r requirements.txt
```

## Usage

Each script requires a CSV file as input and performs the respective statistical test on predefined columns.

### Running Levene's Test

```
python LevenesTest.py <data_file.csv>
```

This script tests for variance equality between predefined column pairs in the dataset.

### Running Mann-Whitney U Test

```
python MannWhitneyUTest.py <data_file.csv>
```

This script performs the Mann-Whitney U test to compare predefined groups.

### Running Shapiro-Wilk Normality Test

```
python ShapiroWilkNormalityTest.py <data_file.csv>
```

This script tests whether predefined columns in the dataset follow a normal distribution.

## Notes

-   Ensure that your CSV file has column names that match those expected by the scripts.
    
-   The results are printed to the console.
    

## Example CSV Format

Your CSV file should be structured as follows:

```
Historical Lab 01,Historical Lab 02,Experiment Lab 01,Experiment Lab 02
12.5,14.2,10.8,9.6
13.1,15.0,11.3,10.2
...
```

Ensure that your dataset contains the correct column names, as the scripts rely on them. 

Missing values in a given row are handled automatically, as it is expected that experiment data may have fewer entries than historical data.
