from openai import OpenAI
import os
from dotenv import load_dotenv

# Преобразования для DataFrame
def filter_data(df, condition):
    return df.query(condition)

def select_columns(df, columns):
    return df[columns]

def sort_data(df, column):
    return df.sort_values(by=column)

def group_and_aggregate(df, group_by, agg_column):
    return df.groupby(group_by)[agg_column].sum()

def get_top_n(df, column, n):
    return df.sort_values(by=column, ascending=False).head(n)

def get_bottom_n(df, column, n):
    return df.sort_values(by=column, ascending=True).head(n)

def get_average(df, column):
    return df[column].mean()

def get_sum(df, column):
    return df[column].sum()

def get_max(df, column):
    return df[column].max()

def get_min(df, column):
    return df[column].min()

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

prompt = input("Enter your prompt:")

completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a helpful assistant that manages transformations over a pandas dataframe."
                                      "Help user to solve their task."
                                      "You can use any of the following functions:"
                                      "filter_data, select_columns, sort_data, group_and_aggregate, get_top_n, get_bottom_n, get_average, get_sum, get_max, get_min"},
        {
            "role": "user",
            "content": f"{prompt}"
        }
    ]
)

print(completion.choices[0].message.content)