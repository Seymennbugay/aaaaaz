# machine_info.py — Basit makine/network bilgisi toplayıcı
import socket

def show_machine_info():
    """Hostname ve temel IP bilgilerini yazdırır."""
    hostname = socket.gethostname()  # Makine adı
    try:
        ip = socket.gethostbyname(hostname)  # Basit IP çözümü (her zaman tüm arayüzleri vermez)
    except socket.gaierror:
        ip = "Çözümlenemedi"

    print(f"[MACHINE] Hostname: {hostname}")
    print(f"[MACHINE] IP: {ip}")

if __name__ == "__main__":
    show_machine_info()
