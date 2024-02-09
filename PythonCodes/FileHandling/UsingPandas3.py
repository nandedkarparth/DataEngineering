import pandas as pd

header = ['Name', 'M1 Score', 'M2 Score']
data = [['Alex', 62, 80], ['Brad', 45, 56], ['Joey', 85, 98]]
df = pd.DataFrame(data, columns=header)


df.to_csv('Stu_data_written.csv', index=False)
