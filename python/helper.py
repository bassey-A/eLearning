import os

class Helper():
    """
    Helper functions to handle IO stuff
    """
    def get_number(self, low, high, message):
        num = -1
        while not(num >= low and num <= high):
            try:
                num = (int)(input(message))
                os.system("cls")
            except ValueError as _:
                os.system("cls")
                print(f'The number should be from {low} to {high}')
        return num