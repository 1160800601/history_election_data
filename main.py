import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

YEARS = [1976, 1980, 1984, 1988, 1992, 1996, 2000, 2004, 2008, 2012, 2016]
STATES = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California',
          'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida',
          'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana',
          'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine',
          'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi',
          'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire',
          'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota',
          'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island',
          'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah',
          'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']
STATE_ELECTORAL_VOTE = {'Alabama': 9, 'Alaska': 3, 'Arizona': 11, 'Arkansas': 4, 'California': 55,
                        'Colorado': 9, 'Connecticut': 7, 'Delaware': 3, 'District of Columbia': 0, 'Florida': 29,
                        'Georgia': 16, 'Hawaii': 4, 'Idaho': 4, 'Illinois': 20, 'Indiana': 11,
                        'Iowa': 6, 'Kansas': 6, 'Kentucky': 8, 'Louisiana': 8, 'Maine': 4,
                        'Maryland': 10, 'Massachusetts': 11, 'Michigan': 16, 'Minnesota': 10, 'Mississippi': 6,
                        'Missouri': 10, 'Montana': 3, 'Nebraska': 5, 'Nevada': 6, 'New Hampshire': 4,
                        'New Jersey': 14, 'New Mexico': 5, 'New York': 29, 'North Carolina': 15, 'North Dakota': 3,
                        'Ohio': 18, 'Oklahoma': 7, 'Oregon': 7, 'Pennsylvania': 20, 'Rhode Island': 4,
                        'South Carolina': 9, 'South Dakota': 3, 'Tennessee': 11, 'Texas': 38, 'Utah': 6,
                        'Vermont': 3, 'Virginia': 13, 'Washington': 12, 'West Virginia': 5, 'Wisconsin': 10,
                        'Wyoming': 3}
# SWING_STATES = ['New Mexico', 'Virgina', 'Colorado', 'Maine', 'Nevada',
#                 'Minnesota', 'New Hampshire', 'Michigan', 'Wisconsin', 'Pennsylvania',
#                 'Florida', 'North Carolina', 'Arizona', 'Georgia', 'Ohio', 'Texas']


class his_data:
    def read_csv(self):
        # self.df = pd.read_csv("data/re1976-2016-president.csv")
        self.df = pd.read_csv('data/washed_data.csv')
        self.new_df = self.df

    def loc(self):
        # self.df.replace('democratic-farmer-labor', 'democrat')
        self.new_df = self.df.loc[(self.df.party == 'democrat') | (self.df.party == 'republican'),
                                  ['year', 'state', 'state_po', 'candidate', 'party', 'candidatevotes']]

    def print_party(self):
        print(self.df.party)

    def state_history_election(self, state):
        state_df = self.new_df.loc[(self.new_df.state == state)]
        d_votes = []
        r_votes = []
        d_1 = []
        plt.title(state)
        # if state in SWING_STATES:
        #     plt.ylim((0.35, 0.65))
        # else:
        #     plt.ylim((0, 1))
        # line = [(1976, 1), (2016, 1)]
        # (line_xs, line_ys) = zip(*line)
        for year in YEARS:
            state_year_df = state_df.loc[state_df.year == year]
            democrat_vote = state_year_df.loc[state_year_df.party == 'democrat']['candidatevotes'].values[0]
            republican_vote = state_year_df.loc[state_year_df.party == 'republican']['candidatevotes'].values[0]
            d_votes.append(democrat_vote)
            r_votes.append(republican_vote)
            d_1.append(democrat_vote / (republican_vote + democrat_vote))
        lim = 0
        for i in d_1:
            lim = max(lim, abs(i - 0.5))
        lim += 0.1
        f, ax = plt.subplots(1, 1)
        plt.ylim((0.5-lim, 0.5+lim))
        # sns.pointplot(ax=ax, x=YEARS, y=d_1, color='red')
        # sns.pointplot(ax=ax, x=YEARS, y=np.ones(11) - d_1, color='blue')
        plt.xlabel('year')
        plt.ylabel('proportion')
        plt.plot(YEARS, d_1, 'r', label='democrat')
        plt.plot(YEARS, np.ones(11) - d_1, 'b', label='republican')
        plt.plot(YEARS, d_1, 'ro-', YEARS, np.ones(11) - d_1, 'bo-')
        file_path = 'fig_new/' + str(round(d_1[10], 3)) + '_' + state + '.png'
        plt.legend()
        plt.savefig(file_path)
        plt.close()
        # plt.show()
        print()




def draw_pic():
    hd = his_data()
    hd.read_csv()
    for state in STATES:
        hd.state_history_election(state)


def wash_data():
    hd = his_data()
    hd.read_csv()
    hd.loc()
    hd.new_df.to_csv('data/washed_data.csv', index=0)


draw_pic()
# wash_data()

# hd = his_data()
# hd.read_csv()
# # hd.print_party()
# # hd.loc()
# for state in STATES:
#     hd.state_history_election(state)
# # hd.state_history_election('Michigan')
# print()
