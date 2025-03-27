from pwn import *
context.log_level = 'debug'

# Connect to a remote server
test = remote('localhost', 5000)

# Same as in demo1
test.recvline()
test.recvuntil(b': ')
test.sendline(b'something')
test.recvline()
