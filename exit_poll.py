import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

YEARS = [2008, 2012, 2016]
STATES = ['National', 'California']
FACTORS = ['gender', 'age', 'education', 'income']
AGE_VALUES = ['18-29', '30-44', '45-64', '65 and older']


class exit_poll:
    def __init__(self):
        self.df = pd.read_csv('data/exit_poll.csv')

    def plot_age(self, state):
        age_df = self.df[(self.df['state'] == state) & (self.df['factor'] == 'age')]
        # 值是共和党与民主党的百分点差值
        arr = [[], [], [], []]
        for year in YEARS:
            temp_df = age_df[age_df['year'] == year]
            i = 0
            for age_value in AGE_VALUES:
                arr[i].append(temp_df[temp_df['value'] == age_value]['diff'].values[0])
                i += 1
            print()
        plt.figure(figsize=(12, 4))
        plt.suptitle("By Age\n" + state)
        for i in range(4):
            plt.subplot(1, 4, i+1)
            if i > 0:
                plt.yticks([])
            plt.xlim(2006, 2018)
            plt.ylim(-0.5, 0.5)
            plt.plot(YEARS, arr[i])
            plt.plot(YEARS, arr[i], 'bo-')
            plt.plot([2006, 2018], [0, 0], 'r--')
            plt.xticks([2008, 2012, 2016])
            plt.title(AGE_VALUES[i])
        # plt.title(state)
        plt.show()
        print()


ep = exit_poll()
ep.plot_age('National')
print()
