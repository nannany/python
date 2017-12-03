from pwn import *

l = listen()
s = ssh(host='ctfq.sweetduet.info',
        user='q4',
        password='q60SIMpLlej9eq49')
a = s.connect_remote(s.host, l.lport)
b = l.wait_for_connection()
a.sendline('ls -l')
b.recvline()
