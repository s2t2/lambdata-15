# my_lambdata/assignment_oop.py

from pandas import DataFrame

# how can we refactor this functional approach into an object oriented approach?
# (using a class)

class DataFrameProcessor():
    def __init__(self, df):
        """
        Params (df) a DataFrame with a column called "abbrev" that has state abbreviations.
        """
        self.df = df

    def add_state_names_column(self):
        """
        Add a column of corresponding state names to a dataframe.

        Return a copy of the original dataframe, but with an extra column.
        """
        names_map = {"CA": "Cali", "CO": "Colo", "CT": "Conn"}

        # this way will return a transformed copy of the dataframe
        #new_df = self.df.copy()
        #new_df["name"] = new_df["abbrev"].map(names_map) # see: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.map.html
        #return new_df

        # this way will mutate the existing df
        self.df["name"] = self.df["abbrev"].map(names_map) # see: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.map.html

if __name__ == "__main__":

    df = DataFrame({"abbrev": ["CA", "CO", "CT", "DC", "TX"]})
    #print(df.head())

    #mapped_df = add_state_names_column(df)
    #print(mapped_df.head())

    processor = DataFrameProcessor(df=df)
    print(processor.df.head())
    processor.add_state_names_column()
    print(processor.df.head())

    #new_df = processor.add_state_names_column()
    #print(new_df.head())
