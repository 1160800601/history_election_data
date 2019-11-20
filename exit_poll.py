import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

YEARS = [2008, 2012, 2016]
STATES = ['National', 'California', 'Arizona']
FACTORS = ['gender', 'age', 'education', 'income']
AGE_VALUES = ['18-29', '30-44', '45-64', '65 and older']
GENDER_VALUES = ['male', 'female']
EDU_VALUES = ['high school or less', 'some college', 'college graduate', 'postgraduate']
INCOME_VALUES = ['under $50k', '$50k-$100k', '$100k or more']
COLORS = ['r', 'g', 'b', 'y']

class exit_poll:
    def __init__(self):
        self.df = pd.read_csv('data/exit_poll.csv')

    def plot_age(self, state):
        age_df = self.df[(self.df['state'] == state) & (self.df['factor'] == 'age')]
        arr = [[], [], [], []]
        for year in YEARS:
            temp_df = age_df[age_df['year'] == year]
            i = 0
            for age_value in AGE_VALUES:
                arr[i].append(temp_df[temp_df['value'] == age_value]['diff'].values[0])
                i += 1
            print()
        plt.figure(figsize=(4, 6))
        plt.suptitle("By Age\n\n" + state)
        plt.xlim(2006, 2018)
        plt.ylim(-0.5, 0.5)
        plt.plot([2006, 2018], [0, 0], 'r--')
        plt.xticks([2008, 2012, 2016])
        plt.yticks([])
        plt.xlabel('year')
        plt.ylabel("republican                          democrat")
        for i in range(4):
            plt.plot(YEARS, arr[i], COLORS[i], label=AGE_VALUES[i])
            plt.plot(YEARS, arr[i], 'ko')
        plt.legend()
        save_path = "his_feature/by_age_" + state
        # plt.show()
        plt.savefig(save_path)

    def plot_gender(self, gender):
        gender_df = self.df[(self.df['state'] == state) & (self.df['factor'] == 'gender')]
        arr = [[], []]
        for year in YEARS:
            temp_df = gender_df[gender_df['year'] == year]
            i = 0
            for gender_val in GENDER_VALUES:
                arr[i].append(temp_df[temp_df['value'] == gender_val]['diff'].values[0])
                i += 1
            print()
        plt.figure(figsize=(4, 6))
        plt.suptitle("By Gender\n\n" + state)
        plt.xlim(2006, 2018)
        plt.ylim(-0.5, 0.5)
        plt.plot([2006, 2018], [0, 0], 'r--')
        plt.xticks([2008, 2012, 2016])
        plt.yticks([])
        plt.xlabel('year')
        plt.ylabel("republican                          democrat")
        for i in range(2):
            plt.plot(YEARS, arr[i], COLORS[i], label=GENDER_VALUES[i])
            plt.plot(YEARS, arr[i], 'ko')
        plt.legend()
        save_path = "his_feature/by_gender_" + state
        # plt.show()
        plt.savefig(save_path)

    def plot_edu(self, state):
        edu_df = self.df[(self.df['state'] == state) & (self.df['factor'] == 'education')]
        arr = [[], [], [], []]
        for year in YEARS:
            temp_df = edu_df[edu_df['year'] == year]
            i = 0
            for edu_val in EDU_VALUES:
                arr[i].append(temp_df[temp_df['value'] == edu_val]['diff'].values[0])
                i += 1
            print()
        plt.figure(figsize=(4, 6))
        plt.suptitle("By Education\n\n" + state)
        plt.xlim(2006, 2018)
        plt.ylim(-0.5, 0.5)
        plt.plot([2006, 2018], [0, 0], 'r--')
        plt.xticks([2008, 2012, 2016])
        plt.yticks([])
        plt.xlabel('year')
        plt.ylabel("republican                          democrat")
        for i in range(4):
            plt.plot(YEARS, arr[i], COLORS[i], label=EDU_VALUES[i])
            plt.plot(YEARS, arr[i], 'ko')
        plt.legend()
        save_path = "his_feature/by_edu_" + state
        # plt.show()
        plt.savefig(save_path)

    def plot_income(self, state):
        income_df = self.df[(self.df['state'] == state) & (self.df['factor'] == 'income')]
        arr = [[], [], []]
        for year in YEARS:
            temp_df = income_df[income_df['year'] == year]
            i = 0
            for income_val in INCOME_VALUES:
                arr[i].append(temp_df[temp_df['value'] == income_val]['diff'].values[0])
                i += 1
            print()
        plt.figure(figsize=(4, 6))
        plt.suptitle("By Income\n\n" + state)
        plt.xlim(2006, 2018)
        plt.ylim(-0.5, 0.5)
        plt.plot([2006, 2018], [0, 0], 'r--')
        plt.xticks([2008, 2012, 2016])
        plt.yticks([])
        plt.xlabel('year')
        plt.ylabel("republican                          democrat")
        for i in range(3):
            plt.plot(YEARS, arr[i], COLORS[i], label=INCOME_VALUES[i])
            plt.plot(YEARS, arr[i], 'ko')
        plt.legend()
        save_path = "his_feature/by_income_" + state
        # plt.show()
        plt.savefig(save_path)

ep = exit_poll()
# ep.plot_income("National")
# ep.plot_age('National')
for state in ['Pennsylvania']:
    ep.plot_age(state)
    ep.plot_gender(state)
    ep.plot_edu(state)
    ep.plot_income(state)
print()

