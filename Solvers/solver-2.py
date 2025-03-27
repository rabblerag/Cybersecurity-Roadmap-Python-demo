from pwn import *
context.log_level = 'debug'

chall = remote('localhost', 4012)

chall.recvline()
chall.recvline()

# Get question from server
task = chall.recvline().decode().split(' ')

# Find a and b
for i, s in enumerate(task):
    if s == '+':
        a = task[i-1]
        b = task[i+1]
        break

# Wait until server requests input
chall.recvuntil(b': ')

# Send sum
chall.sendline(str(a+b).encode())

# Read all lines from the server
while True:
    try:
        chall.recvline()
    except:
        break