import socket
import time
import os
import struct
import telnetlib


def connect(ip, port):
    return socket.create_connection((ip, port))


def p(x):
    return struct.pack('<I', x)


def u(x):
    return struct.unpack('<I', x)[0]


def interact(s):
    print('---- interactive mode ----')
    t = telnetlib.Telnet()
    t.sock = s
    t.interact()


s = connect('110.10.212.130', 8888)

interact(s)
