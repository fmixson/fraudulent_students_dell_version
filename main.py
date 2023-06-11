import pandas as pd
import openpyxl
import re

# df = pd.read_csv('C:/Users/family/Desktop/Programming/Bad Actors/Copy of Liberal Arts AHC and Undecided Summer 2023 ENR 2023.05.01.csv')
df_holds = pd.read_csv('C:/Users/flmix/Documents/Fraudulent Students/CER_SR_FRAUD_CHECK_Holds 1236_ 6-6-23.csv')
df = pd.read_csv('C:/Users/flmix/Documents/Fraudulent Students/CER_SR_FRAUD_CHECK_6-6-23.csv')
pd.set_option('display.max_columns', None)
print(df.dtypes)
df.sort_values(by=['ID'])
# df['Cum Units Passed'] = df['Cum Units Passed'].str.replace(',','').astype(float)
# df['Cum Units Pass'] = df['Cum Units Passed'].astype(float)






df = df[df['Total'] == 0]
df = df.fillna(0)
df['Take Prgrs'] = df['Take Prgrs'].astype(float)
# df['Postal'] = df['Postal'].astype(int)
print(df.dtypes)
df = df[df['Take Prgrs'] > 11]
df = df[df['Major'] != 'Retail Management-AA']
df = df[df['Major'] != 'Retail Management-AB']
df = df[df['Major'] != 'Retail Management-AC']
df = df[df['Major'] != 'Retail Management-CT']

df = df[df['Drop Dt'] == 0].reset_index()

# for i in range(len(df_holds)):
#     for j in range(len(df)):
#         if df_holds.loc[i, 'ID'] == df.loc[j, 'ID']:
#             df.loc[j, 'Holds'] = df_holds.loc[i, 'Srv Ind Cd']
df.to_excel('Test.xlsx')

df.reset_index(inplace=True)

class ScoreCount:

    def __init__(self, id, df, student_df, student_holds_df):
        self.id = id
        self.df = df
        self.student_df = student_df
        self.student_holds_df = student_holds_df
        self.score = 2

    def assign_holds(self):
        # for i in range(len(self.student_holds_df)):
            # for j in range(len(self.student_df)):
            #     if self.student_holds_df.loc[i, 'Class Nbr'] == self.student_df.loc[i,'Class Nbr']:
        if len(self.student_holds_df) > 0:
            if self.student_holds_df.loc[0, 'Srv Ind Cd'] == 'ADM':
                self.score += 2
            if self.student_holds_df.loc[0, 'Srv Ind Cd'] == 'IDV':
                self.score += 10



    # def course_total(self):
    #     # student_df = self.df[self.df['ID'] == self.id]
    #     print(student_df)
    #     if len(student_df) > 3:
    #         student_df1 = student_df[student_df['Session'] == '6DB']
    #         if len(student_df1) >= 3:
    #             self.score += 1
    #             # potential_bad_actors.append(self.id)
    #         student_df2 = student_df[student_df['Session'] == '6S']
    #         if len(student_df2) >= 3:
    #             self.score += 1
    #             # potential_bad_actors.append(self.id)
    #         student_df3 = student_df[student_df['Session'] == '6T']
    #         if len(student_df3) >= 3:
    #             self.score += 1
    #             # potential_bad_actors.append(self.id)


    def email_address(self):
        # student_df = self.df[self.df['ID'] == self.id]
        # student_df = student_df.reset_index()
        print(self.student_df.iloc[0, 13])
        hotmail = re.search("hotmail", self.student_df.iloc[0, 13])
        yahoo = re.search("yahoo", self.student_df.iloc[0, 13])

        if hotmail or yahoo:
            self.score += 1

    def postal_code(self):
        # student_df = self.df[self.df['ID'] == self.id]
        # student_df = student_df.reset_index()
        zipcode = self.student_df.iloc[0, 11]

        print(type(zipcode))
        if len(zipcode) == 9:
            zipcode = int(zipcode)
            if zipcode > 930000000:
                self.score += 1
            zipcode = str(zipcode)
        if len(zipcode) == 5:
            zipcode = int(zipcode)
            if zipcode > 93000:
                self.score += 1

    def student_age(self):
        # student_df = self.df[self.df['ID'] == self.id]
        # student_df = student_df.reset_index()
        if self.student_df.iloc[0, 12] > 30:
            self.score += 1
        print('id', self.id, 'self.score', self.score)
        for i in range(len(self.df)):
            if id == self.df.loc[i, 'ID']:
                self.df.loc[i,'Score'] = self.score

                return self.df



student_ids = []
potential_bad_actors = []
for i in range(len(df)):
    if df.loc[i,'ID'] not in student_ids:
        student_ids.append(df.loc[i, 'ID'])

for id in student_ids:
    student_df = df[df['ID'] == id]
    student_holds_df = df_holds[df_holds['ID']==id].reset_index()

    # create holds and student df and upload them method that puts holds on them.

    student = ScoreCount(id=id, df=df, student_df=student_df, student_holds_df=student_holds_df)
    student.assign_holds()
    # student.course_total()
    student.email_address()
    student.postal_code()
    score_df = student.student_age()

score_df.to_excel('Bad_Actors.xlsx')


print(len(student_ids))
print(len(potential_bad_actors))
