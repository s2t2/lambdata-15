# my_lambdata/assignment.py

from pandas import DataFrame

# how can we use an inheritance approach?

class CustomFrame(DataFrame):
    """
    A DataFrame with a column called "abbrev" that has state abbreviations.
    """

    def add_state_names_column(self):
        """
        Add a column of corresponding state names to a dataframe.
        """
        names_map = {"CA": "Cali", "CO": "Colo", "CT": "Conn"}
        self["name"] = self["abbrev"].map(names_map) # see: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.map.html


if __name__ == "__main__":

    #df = DataFrame({"abbrev": ["CA", "CO", "CT", "DC", "TX"]})
    #print(df.head())
    #mapped_df = add_state_names_column(df)
    #print(mapped_df.head())

    custom_frame = CustomFrame({"abbrev": ["CA", "CO", "CT", "DC", "TX"]})
    print(custom_frame.head())

    custom_frame.add_state_names_column()
    print(custom_frame.head())


    another_frame = CustomFrame({"abbrev": ["DC", "WY", "OH", "NY", "TX"]})
    print(another_frame.head())

    another_frame.add_state_names_column()
    print(another_frame.head())
