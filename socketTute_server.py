"""
ソケット通信
ウェルノウンポート（0-1023）
登録済みポート番号（1024-49151）
動的・プライベート　ポート番号（49152-65535）
"""
import socket

#接続方式TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('127.0.0.1',50007))
    #接続数
    s.listen(1)
    #接続があるまで待ち
    while True:
        conn, addr = s.accept()
        with conn:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                #クライアントから受け取ったdataとaddrを表示する
                print('data: {}, addr: {}'.format(data,addr))
                conn.sendall(b'Reveived: ' + data)