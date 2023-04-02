from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 3334))
s.listen(5)
print('waiting...')

while True:
    client, addr = s.accept()
    print('connection from ', addr)

    while True:
        data = client.recv(1024)
        if not data:
            break
        expression = data.decode()
        if expression == 'q':
            break
        try:
            result = eval(expression)
            response = str(round(result, 1))
        except:
            response = 'Error'
        client.send(response.encode())

    client.close()
