from pwn import *

shell = ssh('bandit0', 'bandit.labs.overthewire.org', password='bandit0', port=2220)
print(shell['whoami'])
