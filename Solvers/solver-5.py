from pwn import *
from string import ascii_lowercase
from base64 import b64decode as b64dec
context.log_level = 'debug'

chall = remote('localhost', 4093)

chall.recvline()
chall.recvline()

dec = b64dec(chall.recvline().strip()).decode()
print(dec)

flag = ''

for c in dec:
    if c in ascii_lowercase:
        flag += chr( ((ord(c) - ord('a') + 13) % 26) + ord('a'))
    else:
        flag += c
        
chall.sendline(flag.encode())

chall.recvline()


