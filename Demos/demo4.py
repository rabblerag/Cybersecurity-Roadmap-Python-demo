from pwn import *

# Helper functions to encode/decode with base64
print("Encrypting with base64:", b64e(b'Hello world'))
print("Decrypting with base64:", b64d(b'SGVsbG8gd29ybGQ='))
