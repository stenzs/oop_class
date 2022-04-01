import random

switcher = {
            "камень": 0,
            "бумага": 1,
            "ножницы": 2
        }

class Player:

    def __init__(self, name):
        self.name = name
        self.__points__ = 0
        self.choice = ""

    def choose(self):
        self.choice = input("{name}, выбери камень, ножницы или бумагу: ".format(name=self.name))
        print("{name} выбрал {choice}".format(name=self.name, choice=self.choice))

    def ii_choose(self):
        self.choice = random.choice(list(switcher.keys()))
        print("{name} выбрал {choice}".format(name=self.name, choice=self.choice))

    def to_numerical_choice(self):
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
        while True:
            player1.choose()
            try:
                player1.to_numerical_choice()
                break
            except Exception:
                print("Ошибка, такое выбирать нельзя, давай заново")
        player2.ii_choose()
        result = self.compare_choices(player1, player2)
        print("Результат раунда: {result}".format(result=self.get_result_as_string(result)))
        if result > 0:
            player1.increment_point()
        elif result < 0:
            player2.increment_point()

    def compare_choices(self, player1, player2):
        return self.rules[player1.to_numerical_choice()][player2.to_numerical_choice()]

    @staticmethod
    def get_result_as_string(result):
        res = {
            0: "ничья",
            1: "победа",
            -1: "поражение"
        }
        return res[result]


class Game:

    def __init__(self):
        self.end_game = False
        self.first_player = Player(input("Введите свое имя: "))
        self.second_player = Player("Бот")

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
