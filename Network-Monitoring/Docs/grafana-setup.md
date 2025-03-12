## **Grafana Monitor Kurulumu**
**Bu rehberde Grafana nasıl kurulur onu anlatıyor olacağım.**

**Grafana Güncel Versiyon:** [İndirme Linki](https://grafana.com/grafana/download)

## 📌 **1. Sistem Dosyalarını Güncelleme**  

```bash
sudo apt update && sudo apt upgrade -y
```

## 📌 **2. Grafana Depolarını Ekleme**  

```bash
sudo apt install -y software-properties-common
wget -q -O - https://packages.grafana.com/gpg.key | sudo apt-key add -
sudo add-apt-repository "deb https://packages.grafana.com/oss/deb stable main"
```

## 📌 **3. Grafana Kurulumu**  

```bash
sudo apt update
sudo apt install -y grafana
```

## 📌 **4. Grafana Servisini Başlat ve Etkinleştir**  

```bash
sudo systemctl start grafana-server
sudo systemctl enable grafana-server
```

## 📌 **5. Grafana Web Arayüzüne Erişim**  

```bash
http://localhost:3000/grafana
```

**🎯 Varsayılan Giriş Bilgileri:**
**Username: admin**
**Password: admin**

**Ben localhost üzerine kurduğum için localhost:3000 ip ile başladım, farklı server alanına kuranlar http://<IP:3000>/grafana kısmı ile giriş yapabilirler.**


🥳 **Grafana Monitor başarıyla kuruldu, tebrik ederim.**
🥳 **Grafana Monitor üzerinden Zabbix veya farklı bağlantıları bağlayabilirsiniz.**
