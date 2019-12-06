import pandas as pd
import numpy as np

in_path = "data/exit_polls_08_12_16.csv"
out_path = "data/exit_polls_08_12_16_tidy.csv"
new_col = ['year', 'state', 'question_id', 'question', 'opinion', 'category', 'total',
           'democrat', 'republican', 'other']

df = pd.read_csv(in_path)
new_df = pd.DataFrame(columns=new_col)
temp_arr = []
new_index = 0
for index, row in df.iterrows():
    if index % 4 == 0:
        temp_arr = [row['year'], row['state'], row['question_id'], row['question'], row['opinion'], row['category'], row['value']]
    elif index % 4 == 1:
        temp_arr.append(row['value'])
    elif index % 4 == 2:
        temp_arr.append(row['value'])
    elif index % 4 == 3:
        temp_arr.append(row['value'])
        new_df.loc[new_index] = temp_arr
        new_index += 1
        temp_arr = []
    print(index/62479*100)
new_df.to_csv(out_path)

