from pwn import *
from base64 import b64decode as b64dec
context.log_level = 'debug'

chall = remote('localhost', 4034)
chall.recvline()
chall.recvline()


dec = b64dec(chall.recvline().strip())

print(dec)
chall.sendline(dec)

print(chall.recvline())