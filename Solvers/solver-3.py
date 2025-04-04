from pwn import *
from time import sleep
from string import digits # '0123456789'
from itertools import product


alphabet = digits + "abcdef"

chall = remote("localhost", 4075)
print(chall.recvline().decode())
print(chall.recvline().decode())

# Use product() instead of 4 nested for-loops
for candidate in product(alphabet, repeat=4):
    chall.sendline("".join(candidate).encode())
    response = chall.recvline()
    if b"correct" in response:
        print(response)
        print(chall.recvline())
        chall.close()
        break
    elif b"Wrong" in response:
        continue
    elif b"Time" in response:
        print("".join(candidate))
        print(response)
        break
    sleep(1e-3)  # Don't overload the server
