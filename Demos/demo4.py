from pwn import *

print("Encrypting with base64:", b64e(b'Hello world'))
print("Decrypting with base64:", b64d(b'SGVsbG8gd29ybGQ='))
