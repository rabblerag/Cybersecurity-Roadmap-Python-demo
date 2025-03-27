from pwn import *

# SSH functionality from within function
shell = ssh('bandit0', 'bandit.labs.overthewire.org', password='bandit0', port=2220)
print(shell['whoami']) # Syntax for interacting with the shell
