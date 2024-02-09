import pandas as pd

header = ['Name', 'M1 Score', 'M2 Score']
data_to_append = [['Emma', 75, 90], ['Mike', 60, 78]]
df_to_append = pd.DataFrame(data_to_append, columns=header)


df_to_append.to_csv('Stu_data_written.csv', mode='a', header=False, index=False)
