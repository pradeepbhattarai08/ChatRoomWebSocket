import socket
s=socket.socket()
print('Socket successfully created');
port=56789
s.bind(('',port))
print(f'socket binded to port {port}')
s.listen(5)
print('Socket is listening')

while True:
    c,addr=s.accept()
    print('Got connection from ', addr)
    message=('Thank you for connecting')
    c.send(message.encode())
    c.close()
    

    ## This code hosts a server on port 56789 and listens for incoming connections. When a connection is made, it sends a message to the client and closes the connection.