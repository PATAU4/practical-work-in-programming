import socket
import threading
b = 30


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 8088)) 
sock.listen(5)  # максимальное количество клиентов 

    
def decrypt_with_step(K, data): 
    print(f"Зашифрованный текст: {data}")
    decrypted = ''.join(map(chr, [x - K for x in map(ord, data)]))
    print('Дешифрованный вид исходного текста:')
    return decrypted

def find_step(b, A, p):
    #b = 15   # секретный ключ, объявленный у сервера 
    s_A = (A**b) % p
    return s_A

def find_b_to_client(b, g, p): # высчитывание ключа, необходимого для нахождения шага для дешифрования у клиента 
    B = (g ** b) % p 
    return B
    
#encrypt(find_step(15, A), data_to_encrypt)





def connect(sock):
    # Функция принятия подключения клиента
    while True:
        conn, addr = sock.accept()
        print(f'Client joined. Addres {addr}')
        p, g, A = list(map(int, conn.recv(1024).decode().split()))
        B = find_b_to_client(b, g, p)
        conn.send(str(B).encode())
        global K
        K = find_step(b, A, p)
        print(K)
        if conn is not None:
            output_and_echo(conn) 
    
        
def sending(conn, mess):
    conn.send(mess.encode())

def output_and_echo(conn):
    while True:
        data = conn.recv(1024)   
        data = data.decode()
        print(K)
        data = decrypt_with_step(K, data)   
        print(data)
        sending(conn, 'Echo from server')
    


while True:
    threads = [threading.Thread(target=connect, args=[sock]) for _ in range(3)]
    [thread.start() for thread in threads]
    [thread.join() for thread in threads]
