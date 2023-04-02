import socket

# 서버와 통신할 소켓 생성
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 서버 주소와 포트 번호 설정
server_address = ('localhost', 3334)

# 서버와 연결
client_socket.connect(server_address)

while True:
    # 사용자로부터 계산식 입력 받기
    expression = input("계산식을 입력하세요 (ex: 20+17, q입력시 종료): ")

    # q 입력 시 종료
    if expression == 'q':
        break

    # 입력한 계산식을 서버로 전송
    client_socket.send(expression.encode())

    # 서버로부터 결과 수신
    result = client_socket.recv(1024).decode()

    # 결과 출력
    print(f"결과: {result}")

# 소켓 연결 종료
client_socket.close()
