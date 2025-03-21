from pwn import *
context.log_level = 'debug'

test = process(['python', 'Demos/target1.py'])

test.recvline()
test.recvuntil(b': ')
test.sendline(b'something')
test.recvline()
