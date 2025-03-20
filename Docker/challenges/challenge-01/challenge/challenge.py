from pathlib import Path
import sys


class Challenge:
    def __init__(self):
        self.path = Path(__file__).parent
        self.open_flag()


    def main(self):
        print("You cleared the first stage! Follow the instructions below to connect to the next stage.")
        print(self.flag)
        

    def open_flag(self):
        with open(Path(self.path, "flag.txt")) as file:
            self.flag = file.read()


if __name__ == "__main__":
    challenge = Challenge()
    challenge.main()
