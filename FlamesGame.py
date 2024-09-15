from json import load, dump
from termcolor import colored

FlamesData = {
    "F": "Friend", "L": "Lover", "A": "Affectionate",
    "M": "Marriage", "E": "Enemies", "S": "Siblings"
}

class FlamesGame:
    def __init__(self) -> None:
        with open("data.json", 'r+') as file:
            self.data = load(file)

        self.Results = {"Player1": '', "Player2": ''}

    def Calculate(self, matched: list) -> str:
        ''' This function will calculate the given list of elements and return the match case '''
        GameName = list('FLAMES')
        while len(GameName) != 1:
            count = len(matched) % len(GameName)
            index = (count - 1) % len(GameName)
            GameName.pop(index)
            GameName = GameName[index:] + GameName[:index]
        return FlamesData[GameName[0]]

    def Flames(self) -> str:
        '''taking two players name and then calculate their FLAMES'''
        self.Results["Player1"] = Player1 = input(f'Enter your Name: ')
        Player1 = list(Player1.replace(' ', '').lower())

        self.Results["Player2"] = Player2 = input(f'Enter your Partner\'s Name: ')
        Player2 = list(Player2.replace(' ', '').lower())

        CommonLetters = []

        for letter in Player1[:]:
            if letter in Player2:
                CommonLetters.append(letter)
                Player1.remove(letter)
                Player2.remove(letter)

        Matched = Player1 + Player2
        result = self.Calculate(Matched)

        if result in ["Friend", "Lover", "Affectionate", "Marriage", "Siblings"]:
            result_color = 'green'
        else:
            result_color = 'red'

        print(colored(f"{self.Results['Player1']} and {self.Results['Player2']} Are Becomde : {result}", result_color, attrs=['bold']), "\n")
        return result


if __name__ == "__main__":
    inputs = input(f'Enter any key to start the game, or Enter Q to quit')
    tag = True
    while tag:
        if 'q' != inputs.lower():
            Game = FlamesGame().Flames()
            new = input("Do you want to continue..? Yes/No : ").lower()
            if new in ["yes", "y", "n", "no"]:
                if new in ["n", "no"]:
                    tag = False
                else:
                    tag = True
            else:
                print(f" Please check your Input")
