
# write some code using unittest to test our add_state_names_column() function works as desired

import unittest
from pandas import DataFrame

from my_lambdata.assignment_oop import DataFrameProcessor

class TestAssignment2(unittest.TestCase):

    def test_add_state_names(self):
        #self.assertEqual(enlarge(9), 900)

        df = DataFrame({"abbrev": ["CA", "CO", "CT", "DC", "TX"]})
        processor = DataFrameProcessor(df=df)

        # ensure our test is setup properly
        self.assertEqual(len(processor.df.columns), 1)
        self.assertEqual(list(processor.df.columns), ['abbrev'])
        self.assertEqual(processor.df.iloc[0]["abbrev"], 'CA')

        # what code can we write, referencing df
        # to know if our function did what it was supposed to do
        # (adding a column of corresponding state names)
        #mapped_df = add_state_names_column(df)
        processor.add_state_names_column()

        self.assertEqual(len(processor.df.columns), 2)
        self.assertEqual(list(processor.df.columns), ['abbrev', "name"])
        self.assertEqual(processor.df.iloc[0]["abbrev"], 'CA')
        self.assertEqual(processor.df.iloc[0]["name"], 'Cali')


if __name__ == '__main__':
    unittest.main() # invoking all of our test class's methods
