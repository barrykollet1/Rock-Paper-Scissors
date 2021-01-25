import random


class RockPaperScissors:

    def __init__(self):
        self.all_options = ['rock', 'fire', 'scissors', 'snake', 'human', 'tree', 'wolf', 'sponge',
                            'paper', 'air', 'water', 'dragon', 'devil', 'lightning', 'gun']
        self.default_options = ['rock', 'scissors', 'paper']
        self.options = []

    def test_win(self, user_choice, auto_choice):
        if user_choice == auto_choice:
            print(f"There is a draw ({auto_choice})")
            return 50
        else:
            win_options = []
            i = self.all_options.index(user_choice) + 1
            while len(win_options) < (len(self.all_options) - 1) // 2:
                if i >= len(self.all_options):
                    i = 0
                win_options.append(self.all_options[i])
                i += 1
            if auto_choice not in win_options:
                print(f"Sorry, but the computer chose {auto_choice}")
                return 0
            else:
                print(f"Well done. The computer chose {auto_choice} and failed")
                return 100

    @staticmethod
    def get_score(player):
        players = {}
        f = open('rating.txt')
        for line in f.readlines():
            players[line.split()[0]] = line.split()[1]
        f.close()
        return int(players[player]) if player in players else 0

    def play(self):
        user_name = input("Enter your name: ")
        score = self.get_score(user_name)
        print("Hello,", user_name)

        user_options = input().strip()
        if user_options != '':
            self.options = user_options.split(',')
        else:
            self.options = self.default_options
        print("Okay, let's start")
        while True:
            user_input = input()
            if user_input == '!exit':
                print("Bye!")
                break
            elif user_input == '!rating':
                print(f"Your rating: {score}")
            elif user_input in self.options:
                score += self.test_win(user_input, random.choice(self.options))
            else:
                print("Invalid input")


my_game = RockPaperScissors()
my_game.play()
