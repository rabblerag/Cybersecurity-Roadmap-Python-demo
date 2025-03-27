from pwn import *
context.log_level = 'debug'

# Execute program from inside python
test = process(['python', 'Demos/target1.py'])

test.recvline()             # Receive a line from the program being run
test.recvuntil(b': ')       # Receive data from the program until a specified delimiter
test.sendline(b'something') # Send data to the program
test.recvline()
