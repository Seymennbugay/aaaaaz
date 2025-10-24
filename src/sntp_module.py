import ntplib
from time import ctime

def get_ntp_time():
    """
    NTP sunucusundan zamanı alır ve yazdırır.
    """
    try:
        client = ntplib.NTPClient()
        response = client.request('pool.ntp.org')  # NTP sunucusuna istek atılır
        print("[SNTP] Sunucudan alınan zaman:", ctime(response.tx_time))
    except Exception as e:
        print("[SNTP] Hata:", e)


if __name__ == "__main__":
    get_ntp_time()
