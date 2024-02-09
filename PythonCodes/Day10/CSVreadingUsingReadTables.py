# import pandas module
import pandas as pd

# creating a data frame
df = pd.read_table("CSVData.csv", delimiter=",")
print(df.head())