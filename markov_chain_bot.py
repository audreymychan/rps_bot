from numpy import random
from utils import evaluate

class MarkovChainBot:
    def __init__(self):
        self.history = {'player': [], 'bot': []}
        self.results = []

        self.win_combos_count = {'rr': 1, 'rp': 1, 'rs': 1, 'pr': 1, 'pp': 1, 'ps': 1, 'sr': 1, 'sp': 1, 'ss': 1}
        self.lose_combos_count = {'rr': 1, 'rp': 1, 'rs': 1, 'pr': 1, 'pp': 1, 'ps': 1, 'sr': 1, 'sp': 1, 'ss': 1}
        self.tie_combos_count = {'rr': 1, 'rp': 1, 'rs': 1, 'pr': 1, 'pp': 1, 'ps': 1, 'sr': 1, 'sp': 1, 'ss': 1}
        self.win_transition_matrix = [[1/3] * 3 for i in range(3)]
        self.lose_transition_matrix = [[1/3] * 3 for i in range(3)]
        self.tie_transition_matrix = [[1/3] * 3 for i in range(3)]

        self.transition_matrix = [[0] * 3 for i in range(3)]

    def capture(self, player_throw, bot_throw, result):
        self.history['player'].append(player_throw)
        self.history['bot'].append(bot_throw)
        print(result)
        if len(self.history['player']) >= 2:
            self.update_transition_matrix()
            print('\n')
            print (self.results[-1])
            print(self.transition_matrix)
        self.results.append(result)

    def predict(self):
        # y = random.choice(['rock', 'paper', 'scissors'])

        if len(self.history['player']) <= 2:
            y = random.choice(['rock', 'paper', 'scissors'], p = [0.287792,0.358498,0.353710])
        else:
            if self.history['player'][-1] == 'rock':
                p = self.transition_matrix[0]
            elif self.history['player'][-1] == 'paper':
                p = self.transition_matrix[1]
            else:
                p = self.transition_matrix[2]
            y = random.choice(['paper','scissors','rock'], p = p)

        return y

    def update_transition_matrix(self):
        step = self.history['player'][-2][0] + self.history['player'][-1][0]
        choices = ['r','p','s']

        if self.results[-1] == 'win':
            self.win_combos_count[step] += 1
            rock = sum([value for key, value in self.win_combos_count.items() if key[0] == 'r'])
            paper = sum([value for key, value in self.win_combos_count.items() if key[0] == 'p'])
            scissors = sum([value for key, value in self.win_combos_count.items() if key[0] == 's'])

            for row_index, row in enumerate(self.win_transition_matrix):
                for col_index, value in enumerate(row):
                    a = int(self.win_combos_count[choices[row_index] + choices[col_index]])
                    if row_index == 0:
                        c = a/rock
                    elif row_index == 1:
                        c = a/paper
                    else:
                        c = a/scissors
                    row[col_index] = float(c)
            self.transition_matrix = self.win_transition_matrix

        elif self.results[-1] == 'lose':
            self.lose_combos_count[step] += 1
            rock = sum([value for key, value in self.lose_combos_count.items() if key[0] == 'r'])
            paper = sum([value for key, value in self.lose_combos_count.items() if key[0] == 'p'])
            scissors = sum([value for key, value in self.lose_combos_count.items() if key[0] == 's'])

            for row_index, row in enumerate(self.lose_transition_matrix):
                for col_index, value in enumerate(row):
                    a = int(self.lose_combos_count[choices[row_index] + choices[col_index]])
                    if row_index == 0:
                        c = a/rock
                    elif row_index == 1:
                        c = a/paper
                    else:
                        c = a/scissors
                    row[col_index] = float(c)
            self.transition_matrix = self.lose_transition_matrix

        elif self.results[-1] == 'tie':
            self.tie_combos_count[step] += 1
            rock = sum([value for key, value in self.tie_combos_count.items() if key[0] == 'r'])
            paper = sum([value for key, value in self.tie_combos_count.items() if key[0] == 'p'])
            scissors = sum([value for key, value in self.tie_combos_count.items() if key[0] == 's'])

            for row_index, row in enumerate(self.tie_transition_matrix):
                for col_index, value in enumerate(row):
                    a = int(self.tie_combos_count[choices[row_index] + choices[col_index]])
                    if row_index == 0:
                        c = a/rock
                    elif row_index == 1:
                        c = a/paper
                    else:
                        c = a/scissors
                    row[col_index] = float(c)
            self.transition_matrix = self.tie_transition_matrix

    def throw(self, player_throw):
        bot_throw = self.predict()
        result = evaluate(player_throw, bot_throw)
        self.capture(player_throw, bot_throw, result)
        return bot_throw
