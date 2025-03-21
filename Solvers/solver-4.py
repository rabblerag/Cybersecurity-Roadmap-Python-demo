from pwn import *
context.log_level = 'debug'

chall = remote('localhost', 4034)
chall.recvline()
chall.recvline()


dec = b64d(chall.recvline().strip())

print(dec)
chall.sendline(dec)

print(chall.recvline())