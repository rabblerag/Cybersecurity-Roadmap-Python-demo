from pwn import *
context.log_level = 'debug'

demo = remote('localhost', 5001)

encoded = demo.recvline().strip()

print("Secret is:", xor(encoded, 0x42).decode())
