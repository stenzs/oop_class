class Player:

    def __init__(self, name):
        self.name = name
        self.__points__ = 0
        self.choice = ""

    def choose(self):
        self.choice = input("{name}, выбери камень, ножницы или бумагу: ".format(name=self.name))
        print("{name} выбрал {choice}".format(name=self.name, choice=self.choice))

    def to_numerical_choice(self):
        switcher = {
            "камень": 0,
            "бумага": 1,
            "ножницы": 2
        }
        return switcher[self.choice]

    def increment_point(self):
        self.__points__ += 1


class Game_round:

    def __init__(self, player1, player2):
        self.rules = [
            [0, -1, 1],
            [1, 0, -1],
            [-1, 1, 0]
        ]
        player1.choose()
        player2.choose()
        result = self.compare_choices(player1, player2)
        print("Результат раунда: {result}".format(result=self.get_result_as_string(result)))
        if result > 0:
            player1.increment_point()
        elif result < 0:
            player2.increment_point()

    def compare_choices(self, player1, player2):
        return self.rules[player1.to_numerical_choice()][player2.to_numerical_choice()]

    def get_result_as_string(self, result):
        res = {
            0: "ничья",
            1: "победа",
            -1: "поражение"
        }
        return res[result]

    def award_points(self):
        print("implement")


class Game:

    def __init__(self):
        self.end_game = False
        self.first_player = Player("Spock")
        self.second_player = Player("Kirk")

    def start(self):
        while not self.end_game:
            Game_round(self.first_player, self.second_player)
            self.check_and_condition()

    def check_and_condition(self):
        answer = input("Продолжить игру? y/n")
        if answer == "y":
            Game_round(self.first_player, self.second_player)
            self.check_and_condition()
        else:
            print("Игра закончена, {player1_name} набрал {player1_points}, и {player2_name} набрал {player2_points}"
                  .format(player1_name=self.first_player.name,
                          player1_points=self.first_player.__points__,
                          player2_name=self.second_player.name,
                          player2_points=self.second_player.__points__))
            self.determine_winner()
            self.end_game = True

    def determine_winner(self):
        result_string = "Это ничья"
        if self.first_player.__points__ > self.second_player.__points__:
            result_string = "Победитедль {name}".format(name=self.first_player.name)
        elif self.first_player.__points__ < self.second_player.__points__:
            result_string = "Победитедль {name}".format(name=self.second_player.name)
        print(result_string)


game = Game()
game.start()
