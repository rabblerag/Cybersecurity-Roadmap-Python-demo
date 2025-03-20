from pwn import *
context.log_level = 'debug'

chall = remote('localhost', 4012)

chall.recvline()
chall.recvline()

operation = chall.recvline().decode().split(' ')

for i, s in enumerate(operation):
    if s == '+':
        a = operation[i-1]
        op = s
        b = operation[i+1]
        break

chall.recvuntil(b': ')

print("TEST")
chall.sendline(str(eval(f"{a}{op}{b}")).encode())

while True:
    try:
        chall.recvline()
    except:
        break