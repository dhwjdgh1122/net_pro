from socket import *

s = socket()
s.bind(('', 80))
s.listen(10)

while True:
    c, addr = s.accept()

    data = c.recv(1024)
    msg = data.decode()
    req = msg.split('\r\n')

# 웹 서버 코드 작성
# 각 객체(파일 또는 문자열) 전송 후, 소켓 닫기(c.close())
    path = req[0].split(" ")
    path = path[1]
    filename = path[1:]

    if filename == "index.html":
        f = open(filename, 'r', encoding='utf-8')
        mimeType = 'text/html'
        response = 'Content-Type: ' + mimeType + '\r\n'
        c.send(b'HTTP/1.1 200 OK\r\n')
        c.send(response.encode())
        c.send(b'\r\n')
        data = f.read()
        c.send(data.encode('euc-kr'))
        c.close()
        
    elif filename == "iot.png":
        f = open(filename, 'rb')
        mimeType = 'image/png'
        response = 'Content-Type: ' + mimeType + '\r\n'
        c.send(b'HTTP/1.1 200 OK\r\n')
        c.send(response.encode())
        c.send(b'\r\n')
        data = f.read()
        c.send(data)
        c.close()

    elif filename == "favicon.ico":
        f = open(filename, 'rb')
        mimeType = 'image/x-icon'
        response = 'Content-Type: ' + mimeType + '\r\n'
        c.send(b'HTTP/1.1 200 OK\r\n')
        c.send(response.encode())
        c.send(b'\r\n')
        data = f.read()
        c.send(data)
        c.close()

    else:
        content = '<HTML><HEAD><TITLE>Not Found</TITLE></HEAD><BODY>Not Found</BODY></HTML>'
        response = 'HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n{}'.format(content)
        c.send(response.encode())

        c.close()

s.close()
