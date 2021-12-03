
import socket
import threading
        


def receiving():
    # Функция получения echo от сервера
    while True:   
        try:   
            data = sock.recv(1024)
            print(data.decode())
        except:
             print('Отключение')
             break





def encrypt(K, data_to_encrypt):
    global encrypted
    encrypted=''.join(map(chr, [x + K for x in map(ord, data_to_encrypt)]))
    print('Зашифрованный вид исходного текста:')
    print(encrypted)
    return encrypted


    
def find_step(a, B): # нахождение шага для дешифрования
    #a = 6   # секретный ключ, объявлено у клиента 
    s_A = (B**a)%p
    return s_A

def find_a_to_server(a): # высчитывание ключа, необходимого для нахождения шага для шифрования на сервере
    A = (g**a)%p 
    return A

def sending():
    # Функция передачи data к серверу
    sock.send(f'client {nickname} joined'.encode())
    while True:
        mes = (input())
        mes = encrypt(K, mes)
        sock.send(mes.encode())
        
        if mes=='exit':
            sock.close()   
            break     


global p,g
p = 23 # первое секретное число, о котором знает и клиент и сервер
g = 5  # второе секретное число, о котором знает и клиент и сервер
a = 7
A = find_a_to_server(a)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
public_k = str(p) + " " + str(g) + ' ' + str(A)
sock.connect(('localhost', 8087)) 
sock.send(public_k.encode())
B = int(sock.recv(1024).decode())
global K
K = find_step(a, B)
print(f"K = {K}")

while True:
    nickname = input ('Enter your nickname: ')
    if 1<len(nickname)<20:
        break





t1 = threading.Thread(target=sending, name='sending')
t2 = threading.Thread(target=receiving, name='receiving')

t1.start()
t2.start()

t2.join()


sock.close()
