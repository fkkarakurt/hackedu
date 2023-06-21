import socket

# Sunucu bilgilerini ayarla
server_ip = '127.0.0.1'  # Sunucu IP adresi
server_port = 12345  # Sunucu portu

# Soket oluştur ve sunucuya bağlan
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_ip, server_port))

while True:
    # Kullanıcıdan mesaj al
    message = input("Gönderilecek mesajı girin (Çıkmak için q/Q): ")

    if message.lower() == 'q':
        break

    # Mesajı sunucuya gönder
    client_socket.send(message.encode())

    # Sunucudan gelen yanıtı al
    response = client_socket.recv(1024).decode()
    print("Sunucudan gelen yanıt:", response)

# Bağlantıyı kapat
client_socket.close()