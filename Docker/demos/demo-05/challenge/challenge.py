key = 0x42

secret = b'Very secret string'

encrypted = ''.join(chr(b ^ key) for b in secret)

print(encrypted)
