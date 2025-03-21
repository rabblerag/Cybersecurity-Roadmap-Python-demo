from pathlib import Path
from base64 import b64encode as b64enc
from string import ascii_lowercase
import sys


class Challenge:
    def __init__(self):
        self.path = Path(__file__).parent
        self.open_flag()


    def main(self):
        print("-------Final stage-------")
        print("This time we applied 2 round of encryption on the flag. Can you decipher the flag?")
        
        self.challenge()


    def encrypt_flag(self):
        encrypted = ''
        for c in self.flag:
            if c in ascii_lowercase:
                encrypted += chr(((ord(c) - ord('a') + 13) % 26) + ord('a'))
            else:
                encrypted += c
                
        encrypted = b64enc(encrypted.encode())

        return encrypted.decode()
        

    def challenge(self):
        enc = self.encrypt_flag()
        print(enc)
        if input().strip() == self.flag:
            print("The flag is correct! You have completed the challenge!")
        else:
            print("Wrong! Are you sure you decyphered the flag correctly?")
        
         
                        
        


    def open_flag(self):
        with open(Path(self.path, "flag.txt")) as file:
            self.flag = file.read()


if __name__ == "__main__":
    challenge = Challenge()
    challenge.main()
