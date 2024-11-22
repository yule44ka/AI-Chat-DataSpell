# AI-Chat-DataSpell

This project provides assistant that help to work with pandas dataframe.

## Installation

1. Install the necessary dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2. Create a `.env` file and add your OpenAI API key:
    ```env
    OPENAI_API_KEY=your_openai_api_key
    ```

## Usage

Run the `main.py`:

```bash
python main.py
```

### Data Transformation

The following functions for DataFrame processing are available:

- `filter_data(df, condition)` - Filters data based on a condition.
- `select_columns(df, columns)` - Selects specific columns.
- `sort_data(df, column)` - Sorts data by a column.
- `group_and_aggregate(df, group_by, agg_column)` - Groups and aggregates data.
- `get_top_n(df, column, n)` - Retrieves the top N rows.
- `get_bottom_n(df, column, n)` - Retrieves the bottom N rows.
- `get_average(df, column)` - Calculates the average of a column.
- `get_sum(df, column)` - Calculates the sum of a column.
- `get_max(df, column)` - Retrieves the maximum value of a column.
- `get_min(df, column)` - Retrieves the minimum value of a column.
