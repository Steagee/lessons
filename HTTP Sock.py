import socket

host=str(input("Enter URL: ", ))
host_e=(host.encode())

request = b"GET / HTTP/1.1\nHost:"+host_e+b"\n\n"
print(request)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, 80))
s.send(request)
result = s.recv(10000)

while (len(result) > 0):
    print(result)
    result = s.recv(10000)