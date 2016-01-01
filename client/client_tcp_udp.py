#!/usr/bin/python

import sys
import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5000


# UDP Client
def UDP_Client(message):
    print "Starting UDP Client..."
    print "UDP target", UDP_IP, ":", UDP_PORT
    print "Content: ", message

    sock = socket.socket(socket.AF_INET,  # Internet
                         socket.SOCK_DGRAM)  # UDP
    sock.sendto(message, (UDP_IP, UDP_PORT))
    sock.close()
    print "Closing UDP Client..."


# / UDP Client


# TCP Client
def TCP_Client(message):
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = 10000
    # Connect the socket to the port where the server is listening
    server_address = ('127.0.0.1', port)
    print >> sys.stderr, 'connecting to %s port %s' % server_address
    sock.connect(server_address)
    try:
        # Send data
        print >> sys.stderr, 'sending "%s"' % message
        sock.sendall(message)

        # Look for the response
        amount_received = 0
        amount_expected = len(message)

        while amount_received < amount_expected:
            data = sock.recv(16)
            amount_received += len(data)
            print >> sys.stderr, 'received "%s"' % data

    finally:
        print >> sys.stderr, 'closing socket'
        sock.close()  # / TCP Client


if (len(sys.argv) != 3):
    print "Pass 0 or 1 as argument to define client type\n0:\tUDP\n1:\tTCP"
    print "Follow that with the message"
    quit(1);
else:
    if (sys.argv[1] == '0'):
        UDP_Client(sys.argv[2])
    else:
        TCP_Client(sys.argv[2])
