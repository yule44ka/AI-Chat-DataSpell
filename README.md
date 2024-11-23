# AI DataFrame Transformation Assistant

This tool allows you to apply AI-driven transformations to a pandas DataFrame using OpenAI's GPT model. The assistant helps generate and apply various transformations, such as selecting columns and sorting data, based on user input.

## Installation

1. Install the necessary dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2. Create a `.env` file in the root directory and add your OpenAI API key:
    ```env
    OPENAI_API_KEY=your_openai_api_key
    ```

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

