key = 0x42 # Secret key to be used for XORing the secret

secret = b'Very secret string' # String that we want to keep secret

encrypted = ''.join(chr(b ^ key) for b in secret) # How we would normally xor each character with the key

print(encrypted)
