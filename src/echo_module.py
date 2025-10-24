# echo_module.py — Basit TCP echo server & client
import socket
import threading

def start_echo_server(host="127.0.0.1", port=5000):
    """Echo server: gelen veriyi aynen geri yollar."""
    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP soketi
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Port hızlı reuse
    srv.bind((host, port))
    srv.listen(1)
    print(f"[ECHO] Server listening on {host}:{port}")

    conn, addr = srv.accept()  # Bağlantıyı kabul et
    print("[ECHO] Connected:", addr)
    with conn:
        while True:
            data = conn.recv(4096)
            if not data:
                break
            conn.sendall(data)  # Aldığını geri gönder
    srv.close()
    print("[ECHO] Server closed")

def test_echo(host="127.0.0.1", port=5000, msg=b"hello123"):
    """Kısa test: server'ı ayrı thread'de başlatır, client olarak mesaj yollayıp geri dönüşü doğrular."""
    th = threading.Thread(target=start_echo_server, args=(host, port), daemon=True)
    th.start()

    # Client tarafı
    cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cli.connect((host, port))
    cli.sendall(msg)
    got = cli.recv(4096)
    cli.close()
    print("[ECHO-TEST] Client got:", got)
    return got

if __name__ == "__main__":
    test_echo()
