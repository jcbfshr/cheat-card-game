from pwn import *

conn = remote('34.73.50.242',42121)
print(conn.recvline().decode())
conn.close()