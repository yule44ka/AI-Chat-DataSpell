import os
import json
import pandas as pd
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

# Check for API key
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OpenAI API key not found. Check the .env file.")

# Initialize OpenAI client
client = OpenAI(api_key=api_key)


class DataFrameTransformer:
    """
    Class for managing DataFrame transformations.
    """

    def __init__(self, df: pd.DataFrame):
        self.df = df

    def select_columns(self, columns: list) -> None:
        """Select columns."""
        try:
            self.df = self.df[columns]
        except Exception as e:
            print(f"Error selecting columns: {e}")

    def sort_data(self, column: str = None, by: str = None, ascending: bool = True) -> None:
        """Sort by column."""
        column = column or by  # Support both parameter types
        if not column:
            raise ValueError("The 'column' or 'by' parameter for sorting is not specified.")
        self.df = self.df.sort_values(by=column, ascending=ascending)

    def display(self, n: int = 5) -> None:
        """Display the first n rows of the DataFrame."""
        print(self.df.head(n))


def describe_dataframe(df: pd.DataFrame) -> str:
    """
    Create a description of the current DataFrame for passing to the OpenAI model.
    """
    return (
        f"The current DataFrame has the following columns: {', '.join(df.columns)}.\n"
        f"Here are the first few rows:\n{df.head().to_string(index=False)}"
    )


def generate_transformation_sequence(prompt: str, df_description: str) -> list:
    """
    Generate a sequence of transformations using OpenAI.
    """
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a helpful assistant that generates structured transformations for a pandas dataframe. "
                        "Always respond in JSON format with a list of transformations. Each transformation must have the following structure: "
                        "{'operation': 'operation_name', 'params': {'param1': value1, 'param2': value2, ...}}. "
                        "The available operations are: select_columns, sort_data. "
                        "Here is the description of the current DataFrame:\n" + df_description
                    ),
                },
                {"role": "user", "content": prompt},
            ],
        )
        # Log the response
        print("Full response from OpenAI:", response)

        structured_output = response.choices[0].message.content.strip()
        if not structured_output:
            raise ValueError("Empty response from OpenAI")

        structured_output = clean_json_response(structured_output)

        # Try to decode the JSON
        try:
            return json.loads(structured_output)
        except json.JSONDecodeError as e:
            print(f"JSON decoding error: {e}")
            print(f"Response from OpenAI: {structured_output}")
            return []
    except Exception as e:
        print(f"Error while calling OpenAI: {e}")
        return []


def clean_json_response(response_content: str) -> str:
    """Remove Markdown formatting from the model's response."""
    if response_content.startswith("```json"):
        response_content = response_content[7:]  # Remove "```json"
    if response_content.endswith("```"):
        response_content = response_content[:-3]  # Remove "```"
    return response_content.strip()


def apply_transformations(df: pd.DataFrame, transformations: list) -> pd.DataFrame:
    """
    Apply a sequence of transformations to the DataFrame.
    """
    transformer = DataFrameTransformer(df)

    valid_operations = {"select_columns", "sort_data"}

    for i, step in enumerate(transformations, start=1):
        try:
            operation = step.get("operation")
            params = step.get("params", {})

            # Check for valid operation
            if operation not in valid_operations:
                print(f"Step {i}: Unknown operation '{operation}', skipping.")
                continue

            # Call the corresponding method
            if operation == "select_columns":
                transformer.select_columns(**params)
            elif operation == "sort_data":
                transformer.sort_data(**params)

        except Exception as e:
            print(f"Error in step {i} ({step}): {e}")

    return transformer.df


def load_dataframe_from_file(file_path: str) -> pd.DataFrame:
    """
    Load a DataFrame from a file (e.g., CSV).
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    # Assuming the file is in CSV format
    return pd.read_csv(file_path)


def save_dataframe_to_file(df: pd.DataFrame, file_path: str) -> None:
    """
    Save the DataFrame to a file (e.g., CSV).
    """
    df.to_csv(file_path, index=False)
    print(f"Changes saved to file: {file_path}")


# Example usage
if __name__ == "__main__":
    # Request file path
    file_path = input("Enter the path to the CSV file: ")

    # Load DataFrame from file
    try:
        df = load_dataframe_from_file(file_path)
    except FileNotFoundError as e:
        print(e)
        exit(1)

    # Description of the current DataFrame
    df_description = describe_dataframe(df)

    # User inputs the transformation prompt
    user_prompt = input("Enter a prompt for DataFrame transformation: ")

    # Generate the sequence of transformations
    transformations = generate_transformation_sequence(user_prompt, df_description)

    if transformations:
        print("Generated transformations:")
        print(json.dumps(transformations, indent=4))

        # User confirmation
        confirm = input("Apply these transformations? (y/n): ").strip().lower()
        if confirm == "y":
            # Apply transformations
            transformed_df = apply_transformations(df, transformations)
            print("\nResult:")
            print(transformed_df)

            # Confirmation to save changes
            save_confirm = input("Save changes to the file? (y/n): ").strip().lower()
            if save_confirm == "y":
                save_dataframe_to_file(transformed_df, file_path)  # Save to original file
            else:
                print("Changes not saved.")
        else:
            print("Transformations canceled.")
    else:
        print("Failed to generate transformations.")
