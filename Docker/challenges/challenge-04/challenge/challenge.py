from pathlib import Path
from base64 import b64encode as b64enc


class Challenge:
    def __init__(self):
        self.path = Path(__file__).parent
        self.open_flag()

    def main(self):
        print("-------Stage 4-------")
        print("Can you decode the instructions for the next stage?")

        self.challenge()

    def challenge(self):
        '''
        Fourth challenge: decode the instructions encoded with base64
        '''
        print(b64enc(self.flag.encode()).decode())
        if input().strip() == self.flag:
            print("Correct! Move to stage 5")
        else:
            print("Wrong! Are you sure you decoded the instructions correctly?")

    def open_flag(self):
        '''
        Helper function to read the flag
        '''
        with open(Path(self.path, "flag.txt")) as file:
            self.flag = file.read()


if __name__ == "__main__":
    challenge = Challenge()
    challenge.main()
