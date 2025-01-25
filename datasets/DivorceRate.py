'''
Divorce rate on europe per every 100 marriages
'''

import pandas as pd 

file_path= r'C:\Users\Admin\Desktop\GOOGLE DATA CERTIFICATE\CAPSTONE_GOOGLE_CERT\database_europe birthrate\DATABASE\divorce\divorce_per_100Marriage.csv'
df = pd.read_csv(file_path)
print(df.head())