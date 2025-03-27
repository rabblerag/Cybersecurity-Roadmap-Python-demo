from pathlib import Path


class Challenge:
    def __init__(self):
        self.path = Path(__file__).parent
        self.open_flag()


    def main(self):
        '''
        First challenge: Get the flag by connecting to the docker
        '''
        print("You cleared the first stage! Follow the instructions below to connect to the next stage.")
        print(self.flag)
        

    def open_flag(self):
        '''
        Helper function to read the flag
        '''
        with open(Path(self.path, "flag.txt")) as file:
            self.flag = file.read()


if __name__ == "__main__":
    challenge = Challenge()
    challenge.main()
