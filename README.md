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

Run the `main.py` script to start the application:

```bash
    python main.py
```

## Functions

- **`describe_dataframe(df)`**  
  Creates a description of the DataFrame, including its columns and the first few rows.


- **`generate_transformation_sequence(prompt, df_description)`**  
  Generates a sequence of transformations based on the user's prompt and the DataFrame description.


- **`apply_transformations(df, transformations)`**  
  Applies a list of transformations to the DataFrame.


- **`load_dataframe_from_file(file_path)`**  
  Loads a DataFrame from a CSV file.


- **`save_dataframe_to_file(df, file_path)`**  
  Saves the DataFrame to a CSV file.


## Example

```bash
      Enter the path to the CSV file: data.csv
      Enter a prompt for DataFrame transformation: Sort the data by 'age' column
      Generated transformations:
      [
          {
              "operation": "sort_data",
              "params": {
                  "column": "age",
                  "ascending": true
              }
          }
      ]
      Apply these transformations? (y/n): y
      Result:
         name  age
      0  Alice   22
      1    Bob   25
      2   Carol   30
      Save changes to the file? (y/n): y
      Changes saved to file: data.csv
```


