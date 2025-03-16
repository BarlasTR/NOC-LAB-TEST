import requests

# Zabbix API bilgileri
ZABBIX_URL = "http://localhost/zabbix/api_jsonrpc.php" # APİ URL adresi
HEADERS = {
    "Content-Type": "application/json",
    "Authorization": "Bearer apitoken"  # API Token buraya girilmeli
}

def create_host():
    payload = {
        "jsonrpc": "2.0",
        "method": "host.create",
        "params": {
            "host": "Barlas_Test_Server",  # Host adı
            "interfaces": [
                {
                    "type": 1,
                    "main": 1,
                    "useip": 1,
                    "ip": "192.168.3.1",  # İzlenen makinenin IP adresi randomint kullanılabilir.
                    "dns": "",
                    "port": "10050"
                }
            ],
            "groups": [{"groupid": "2"}],  # Zabbix’te var olan bir grup ID’si
            "tags": [{"tag": "host-name", "value": "linux-selinuxrver"}],
            "templates": [{"templateid": "10001"}],  # İzleme şablonu (CPU, RAM, Disk)
            "macros": [
                {"macro": "{$USER_ID}", "value": "123321"},
                {"macro": "{$USER_LOCATION}", "value": "0:0:0"}
            ],
            "inventory_mode": 0,
            "inventory": {
                "macaddress_a": "01234",
                "macaddress_b": "56768"
            }
        },
        "id": 2
    }

    response = requests.post(ZABBIX_URL, json=payload, headers=HEADERS)
    return response.json()

# Host ekleme işlemini başlat
result = create_host()
print("Host Ekleme Sonucu:", result)

