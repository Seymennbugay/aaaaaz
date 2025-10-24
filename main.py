# main.py — Entegre menü
from machine_info import show_machine_info
from echo_module import test_echo
from sntp_module import get_ntp_time
from chat_module import start_chat_server, start_chat_client
from socket_settings_module import demo_settings

def menu():
    """Kullanıcıya modül seçtiren basit menü."""
    print("\n=== Network Diagnostic Tool ===")
    print("1) Machine Information")
    print("2) Echo Test")
    print("3) SNTP Time Check")
    print("4) Socket Settings Demo")
    print("5) Chat (Server)")
    print("6) Chat (Client)")
    print("0) Exit")

if __name__ == "__main__":
    while True:
        menu()
        choice = input("Seçim: ").strip()
        if choice == "1":
            show_machine_info()
        elif choice == "2":
            _ = test_echo()
        elif choice == "3":
            get_ntp_time()
        elif choice == "4":
            demo_settings()
        elif choice == "5":
            start_chat_server()
        elif choice == "6":
            start_chat_client()
        elif choice == "0":
            break
        else:
            print("Geçersiz seçim.")
