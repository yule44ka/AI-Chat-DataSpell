import pandas as pd


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