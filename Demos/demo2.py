from pwn import *
context.log_level = 'debug'

test = remote('localhost', 5000)

test.recvline()
test.recvuntil(b': ')
test.sendline(b'something')
test.recvline()
