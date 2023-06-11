import pandas as pd
import openpyxl
import re

# df = pd.read_csv('C:/Users/family/Desktop/Programming/Bad Actors/Copy of Liberal Arts AHC and Undecided Summer 2023 ENR 2023.05.01.csv')
df_holds = pd.read_csv('C:/Users/flmix/Documents/Fraudulent Students/CER_SR_FRAUD_CHECK_Holds 1236_ 6-6-23.csv')
df = pd.read_csv('C:/Users/flmix/Documents/Fraudulent Students/CER_SR_FRAUD_CHECK_6-6-23.csv')
sorted_df = df.sort_values('ID').reset_index()
sorted_df_holds = df_holds.sort_values('ID').reset_index()
pd.set_option('display.max_columns', None)
print(sorted_df)
print(sorted_df_holds)

for i in range(len(sorted_df)):
    for j in range(len(sorted_df_holds)):
        if sorted_df.loc[i, 'ID'] < sorted_df_holds.loc[j, 'ID']:
            break
        if sorted_df.loc[i, 'ID'] == sorted_df_holds.loc[j, 'ID']:
            sorted_df.loc[i, 'Holds'] = sorted_df_holds.loc[j, 'Srv Ind Cd']
            if j <= (len(sorted_df_holds)-1):
                if sorted_df_holds.loc[j, 'ID'] != sorted_df_holds.loc[j+1, 'ID']:
                    break
sorted_df.to_excel('Holds.xlsx')
# sections = []
# for i in range(len(df_holds)):
#     if df.loc[i,'ID'] not in sections:
#         sections.append(df.loc[i, 'ID'])
#
# for section in sections:
