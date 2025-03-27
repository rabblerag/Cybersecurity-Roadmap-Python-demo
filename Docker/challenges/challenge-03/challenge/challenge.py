from pathlib import Path
from random import choice


class Challenge:
    def __init__(self):
        self.path = Path(__file__).parent
        self.open_flag()

    def main(self):
        print("-------Stage 3-------")
        print("Can you find the password by brute-force?")

        self.challenge(4)

    def challenge(self, pass_len):
        '''
        Third challenge: brute-force the password made up of known characters
        '''
        
        alphabet = "0123456789abcdef"
        password = "".join([choice(alphabet) for _ in range(pass_len)])

        while True:
            if input().strip() == password:
                print(
                    "The password is correct! Follow these instructions to move to stage 4"
                )
                print(self.flag)
                break
            else:
                print("Wrong password!")

    def open_flag(self):
        '''
        Helper function to read the flag
        '''
        with open(Path(self.path, "flag.txt")) as file:
            self.flag = file.read()


if __name__ == "__main__":
    challenge = Challenge()
    challenge.main()
