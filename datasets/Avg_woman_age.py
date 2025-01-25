'''
LET'S CLEAN THE AVERAGE AGE TO WOMAN GET MARRIED
'''

import pandas as pd 


#Load dataset

df = pd.read_csv('C:/Users/Admin/Desktop/GOOGLE DATA CERTIFICATE/Capstone/database_europe birthrate/DATABASE/avg age woman marriage/age-at-marriage-women.csv')


#Renamed some columns

df.rename(columns={'Estimated average age at marriage, women': 'Women Avg Married Age','Entity':'Country'}, inplace=True)


#Creating new df to keep just the values where year >=2000

df_filtered = df[df['Year'] >=2000]


#Round the ages to a whole number

df_filtered['Women Avg Married Age'] = df_filtered['Women Avg Married Age'].round()


#Sort by year asc

df_sorted_by_year = df_filtered.sort_values(by=['Year','Country'], ascending=[True,True])


print(df.head())

#Export to an Excel on a specific path
path_to = 'C:/Users/Admin/Desktop/GOOGLE DATA CERTIFICATE/Capstone/database_europe birthrate/DATABASE/avg age woman marriage/Women Avg Married Age.xlsx'
df_sorted_by_year.to_excel(path_to, index=False)
