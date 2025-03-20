from pwn import *
context.log_level = 'debug'

chall = remote("localhost", 4000)

chall.recvline()
chall.recvline()
chall.close()