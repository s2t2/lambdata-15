
#import pandas
#import pandas as pd
from pandas import DataFrame

from my_lambdata.my_mod import enlarge

print("HELLO")

print(enlarge(8))


#df = pandas.DataFrame({"state": ["CT", "CO", "CA", "TX"]})
#df = pd.DataFrame({"state": ["CT", "CO", "CA", "TX"]})
df = DataFrame({"state": ["CT", "CO", "CA", "TX"]})
print(df.head())
