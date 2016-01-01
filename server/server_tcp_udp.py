#!/usr/bin/python

import sys
import socket

DATA_FILE_NAME = "data.txt"


# UDP SERVER
def UDP_SERVER():
    print "Starting local UDP server..."
    port = 5000
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(("", port))
    print "Started on port:", port
    while 1:
        data, addr = s.recvfrom(1024)
        print "[", addr, "] : ", data
        printf("[UPD] " + data)


# /UDP SERVER


# TCP SERVER
def TCP_SERVER():
    print "Starting local TCP server..."
    port = 10000
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('127.0.0.1', port)  # Bind the socket to the port
    print >> sys.stderr, 'starting up on %s port %s' % server_address
    sock.bind(server_address)
    print "Started on port:", port
    # Listen for incoming connections
    sock.listen(1)

    while True:
        # Wait for a connection
        print >> sys.stderr, 'Waiting for a connection'
        connection, client_address = sock.accept()

        try:
            print >> sys.stderr, 'connection from', client_address

            # Receive the data in small chunks and retransmit it
            while True:
                data = connection.recv(16)
                print >> sys.stderr, 'received "%s"' % data
                if data:
                    print >> sys.stderr, 'sending data back to the client'
                    connection.sendall(data)
                    printf("[TCP] " + data)
                else:
                    print >> sys.stderr, 'no more data from', client_address
                    break
        finally:  # Clean up the connection
            connection.close()

            # /TCP SERVER

            # Printf Data To File (./web/DATA_FULE_NAME)


def printf(message):
    target = open('./web/' + DATA_FILE_NAME, 'w')
    target.truncate()
    target.write(message)
    target.close()


# /Printf

# MAIN
if (len(sys.argv) != 2):
    print "Pass 0 or 1 as argument to define server type\n0:\tUDP\n1:\tTCP"
    quit(1);
else:
    if (sys.argv[1] == '0'):
        UDP_SERVER()
    else:
        TCP_SERVER()


# /MAIN
