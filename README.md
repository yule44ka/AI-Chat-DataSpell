# AI DataFrame Transformation Assistant

This tool allows you to apply AI-driven transformations to a pandas DataFrame using OpenAI's GPT model. The assistant helps generate and apply various transformations, such as selecting columns and sorting data, based on user input.

## Features
- Load and save DataFrames from/to CSV files.
- Describe the structure of a DataFrame.
- Generate transformation sequences based on user prompts using OpenAI GPT-4.
- Apply transformations like selecting columns and sorting data.
- Simple command-line interface for ease of use.
A
## Setup and run

1. Go to the directory `assisatnt`:
    ```bash
      cd assistant
      ```
2. Setup:
   ```bash
   ./setup.sh
   ```
3. Run:
    ```bash
   ./run.sh
   ```
Example of dataframe is `ex.csv`.
## Usage

- Run the `main.py` script to start the application:

    ```bash
    python main.py
    ```

## Example

```bash
    Enter the path to the CSV file: data.csv
    What transformations would you like to perform?: Sort by age
    Transformations:
    Sort by Age in ascending order.
    Apply these transformations? (y/n): y
    Result:
          Name  Age  Salary Department
    0    Alice   25   50000         HR
    1    David   29  120000    Finance
    2  Charlie   30   75000         IT
    3      Bob   32   60000         IT
    4      Eve   40  110000         HR
    Save changes to the file? (y/n): y
    Changes saved to file: ex.csv
```

