
import socket
import threading

def start_chat_server():
    """
    Sunucu olarak çalışır. İstemciden gelen mesajları alır, yanıt gönderir.
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 7000))
    s.listen(1)
    print("[CHAT] Sunucu başlatıldı. Bağlantı bekleniyor...")

    conn, addr = s.accept()
    print(f"[CHAT] Bağlandı: {addr}")

    def receive():
        while True:
            try:
                data = conn.recv(1024).decode()
                if not data:
                    break
                print("[Client]", data)
            except:
                break

    threading.Thread(target=receive, daemon=True).start()

    while True:
        msg = input("You: ")
        if msg.lower() == 'exit':
            break
        conn.send(msg.encode())

    conn.close()
    print("[CHAT] Bağlantı sonlandı.")

def start_chat_client():
    """
    Client olarak çalışır. Server'a bağlanıp mesaj gönderir/alır.
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect(('127.0.0.1', 7000))
        print("[CHAT] Sunucuya bağlanıldı.")
    except Exception as e:
        print("[CHAT] Bağlantı hatası:", e)
        return

    def receive():
        while True:
            try:
                data = s.recv(1024).decode()
                if not data:
                    break
                print("[Server]", data)
            except:
                break

    threading.Thread(target=receive, daemon=True).start()

    while True:
        msg = input("You: ")
        if msg.lower() == 'exit':
            break
        s.send(msg.encode())

    s.close()
    print("[CHAT] Bağlantı kapandı.")
