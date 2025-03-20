from pathlib import Path
from random import randrange
from signal import signal, SIGALRM, alarm
import sys


class TimeoutException(Exception):
    '''
    Custom Exception for when user takes too long to respond
    '''
    def __init__(self):
        super().__init__("You weren't fast enough :(\nTry making a script instead of manually computing the answer")


class Challenge:
    def __init__(self):
        self.path = Path(__file__).parent
        self.open_flag()


    def main(self):
        print("-------Stage 2-------")
        print("Can you solve this math question fast enough?")
        
        self.challenge()


    def challenge(self):
        a = randrange(1e5, 1e6)
        b = randrange(1e5, 1e6)
        print("What is the result of", a, '+', b, "?")
        ans = self.timedInput(3)
        if int(ans.strip()) == a+b:
            print("That's the correct answer! Follow these instructions to move to stage 3")
            print(self.flag)
        elif ans != '-1':
            print("Wrong answer")
    

    def timedInput(self, timelimit):
        '''
        Source: https://stackoverflow.com/questions/76406020/python-user-input-to-wait-for-a-few-seconds-if-the-user-does-not-give-any-input
        '''
        def handler(*_):
            raise TimeoutException
        old_handler = signal(SIGALRM, handler)
        alarm(timelimit)
        try:
            return input(f'You have {timelimit} seconds to respond: ')
        except TimeoutException as e:
            print(e)
            return '-1'
        finally:
            signal(SIGALRM, old_handler)


    def open_flag(self):
        with open(Path(self.path, "flag.txt")) as file:
            self.flag = file.read()


if __name__ == "__main__":
    challenge = Challenge()
    challenge.main()
