class Machine:
    def __init__(self, number, chances, answer):
        self.number = number
        self.chances = chances
        self.answer = answer
        self.is_correct = False

    def machine_set_number(self):
        self.number = range(1,100)
        print(self.number)

    def is_player_correct(self):
        if self.chances > 0 and self.answer == self.number:
            self.is_correct = True
            print('You guessed the correct number {number} in {chances} chances! Great job {name}!'.format(number=self.number, chances=self.chances, name=Player.name))
    
class Player:
    def __init__(self, name, guess):
        self.name = name
        self.guess = guess
        self.nan = False
    
    def set_player_name(self):
        self.name = input('Type your name:')
    
player = Player('Nate', 5)
player.set_player_name()