import socket

# Sunucu IP adresi ve port numarası
HOST = '127.0.0.1'
PORT = 12345

# TCP soketi oluşturma
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    # IP adresi ve port numarasıyla soketi bağlama
    server_socket.bind((HOST, PORT))
    
    # Bağlantıları dinleme
    server_socket.listen()

    print(f"Sunucu {HOST}:{PORT} üzerinde dinlemede...")

    # Bağlantıyı kabul etme
    client_socket, client_address = server_socket.accept()
    print(f"{client_address} adresinden bir istemci bağlandı.")

    # İstemciden gelen verileri almak ve işlemek için döngü
    while True:
        # İstemciden veri al
        data = client_socket.recv(1024)
        if not data:
            # Veri alınmadıysa bağlantıyı kapat
            break
        
        # Gelen veriyi işle
        received_data = data.decode()
        print(f"Gelen veri: {received_data}")
        
        # İstemciye yanıt gönder
        response = f"Sunucudan yanıt: {received_data}"
        client_socket.sendall(response.encode())
    
    # Bağlantıları kapat
    client_socket.close()