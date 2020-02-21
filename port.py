import socket

remoteServer = input('Enter a remote host to scan: ')

for port in range(78,85):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    result = sock.connect_ex((remoteServer,port))

    if result == 0:
        print(f'Port {port} open')

    else:
        print(f'Port {port} close')

    sock.close()