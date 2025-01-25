'''
Birthrate around the world, cleaning to get from 2000 to last year avalible
'''


import pandas as pd
import os

# Load the dataset
file_path = r'C:\Users\Admin\Desktop\GOOGLE DATA CERTIFICATE\CAPSTONE_GOOGLE_CERT\database_europe birthrate\DATABASE\birthrate\birthrate per 1k_eurostat.csv'
df = pd.read_csv(file_path)

# Drop 'Indicator Name' and 'Indicator Code' columns
columns_to_drop = ['Indicator Name', 'Indicator Code','2023']
df.drop(columns=columns_to_drop, inplace=True)


# Filter columns to keep only 'Country Name' and years >= 2000
columns_to_keep = ['Country Name'] +['Country Code']+ [col for col in df.columns if col.isdigit() and int(col) >= 2000]
df_filtered = df[columns_to_keep]

# Round the values in year columns
year_columns = [col for col in df_filtered.columns if col.isdigit()]
df_filtered[year_columns] = df_filtered[year_columns].round(2)

# Define the output path
output_path = r'C:\Users\Admin\Desktop\GOOGLE DATA CERTIFICATE\CAPSTONE_GOOGLE_CERT\database_europe birthrate\DATABASE\birthrate\Birthrate_clean_TO_USE.xlsx'

# Save the cleaned dataset to a new file
df_filtered.to_excel(output_path, index=False)