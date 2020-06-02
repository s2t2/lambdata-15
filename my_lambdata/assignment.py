# my_lambdata/assignment.py

from pandas import DataFrame

# TODO: helper function from Assignment
# State abbreviation -> Full Name and visa versa.
# FL -> Florida, etc.

def add_state_names_column(my_df):
    """
    Add a column of corresponding state names to a dataframe.

    Params (my_df) a DataFrame with a column called "abbrev" that has state abbreviations.

    Return a copy of the original dataframe, but with an extra column.
    """
    new_df = my_df.copy()

    names_map = {"CA": "Cali", "CO": "Colo", "CT": "Conn"}

    new_df["name"] = new_df["abbrev"].map(names_map) # see: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.map.html

    return new_df

if __name__ == "__main__":

    df = DataFrame({"abbrev": ["CA", "CO", "CT", "DC", "TX"]})
    print(df.head())

    mapped_df = add_state_names_column(df)
    print(mapped_df.head())
