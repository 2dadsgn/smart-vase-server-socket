import socket
import mongoconn as CONN
import json
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip='192.168.1.103'
s.bind((ip,1238))
s.listen(2)
while True:
    clientsocket, address = s.accept()
    clientsocket.send(bytes("connection established","utf-8"))
    cliente = clientsocket.getsockname()
    print(f"benvenuto {cliente}")
    msg= clientsocket.recv(1024)
    print(msg.decode("utf-8"))

    #riceve oggetto da client vase
    ogg_json = clientsocket.recv(1024)
    print(ogg_json.decode("utf-8"))

    clientsocket.close()

    dati = json.loads(ogg_json)
    try:
        CONN.insert_dati(dati)
    except:
        print("errore chiamata a funzione CONN")
