# socket_settings_module.py — timeout / buffer / non-blocking demo
import socket
import errno

def demo_settings():
    """Timeout, buffer boyutları ve non-blocking davranışını gösterir."""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Timeout ayarı
    s.settimeout(2.0)  # 2 sn timeout
    print("Timeout:", s.gettimeout(), "s")

    # Buffer ayarları (not: OS limitleri var, set edilen değer garanti değil)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 65536)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 65536)
    print("SO_RCVBUF:", s.getsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF))
    print("SO_SNDBUF:", s.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF))

    # Non-blocking accept demo
    s.bind(("127.0.0.1", 0))
    s.listen(1)
    s.setblocking(False)  # bloklama kapalı
    try:
        _ = s.accept()  # bekleyen bağlantı yoksa hata beklenir
    except OSError as e:
        if e.errno in (errno.EAGAIN, errno.EWOULDBLOCK):
            print("Non-blocking accept: pending connection yok (beklenen).")
        else:
            print("Non-blocking accept ERROR:", e)
    finally:
        s.close()

if __name__ == "__main__":
    demo_settings()
