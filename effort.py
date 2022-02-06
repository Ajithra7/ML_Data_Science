import pandas as pd
student_marks = pd.Series(['vijaya' :80,'rahul':92,'meghna':6])
student_age = pd.Series(['vijaya' :32,'rahul' :92,'meghna' :30])
student_df = pd.DataFrame(['marks' :student_marks,'age' student-age])
print(student_df)
print(student_df.sort_values(by=['marks']))
print(student_df.sort_values(by=['marks',ascending=False]))
