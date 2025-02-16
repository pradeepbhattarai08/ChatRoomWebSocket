import socket
import sys

try:
    S=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print('Socket successfully created');
except socket.error as err:
    print(f'Socket creation failded with error {err}')

port=80

try:
    host_ip=socket.gethostbyname('www.github.com');
except socket.gaierror:
        print(f'Error resolving the host {err}')
        sys.exit()

S.connect((host_ip,port))
print(f'Socket has successfully connected to github on port = {host_ip}')



## This code makes connection to the external github server on port 80 and prints the message that the connection is successful.