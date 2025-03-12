## Zabbix Network Monitor Kurulumu
**Bu rehberde Zabbix nasıl kurulur onu anlatıyor olacağım.**

**Zabbix Güncel Versiyon:**

[Zabbix İndirme Linki](https://www.zabbix.com/download)

## 📌 **1. Sistem Dosyalarını Güncelleme**  

```bash
sudo apt update && sudo apt upgrade -y
```

## 📌 **2. Zabbix Depolarını Ekleme**  

```bash
wget https://repo.zabbix.com/zabbix/6.0/ubuntu/pool/main/z/zabbix-release/zabbix-release_6.0-4+ubuntu$(lsb_release -rs)_all.deb
sudo dpkg -i zabbix-release_6.0-4+ubuntu$(lsb_release -rs)_all.deb
sudo apt update
```

## 📌 **3. Zabbix Server ve İlgili Paketlerin Kurulumu**  

```bash
sudo apt install -y zabbix-server-mysql zabbix-frontend-php zabbix-apache-conf zabbix-agent
```

## 📌 **4. MySQL (MariaDB) Kurulumu**  

```bash
sudo apt install -y mariadb-server
```

**MariaDB’yi güvenli hale getirelim:**

```bash
sudo mysql_secure_installation
```

**Sonrasında Zabbix için bir veritabanı oluşturuyoruz:**

```bash
sudo mysql -uroot -p
```

**SQL komutlarıyla gerekli ayarları yapın:**

**Şifreniz kısmını databese şifrenizi belirleyebilirsiniz.**

```bash
CREATE DATABASE zabbix CHARACTER SET utf8mb4 COLLATE utf8mb4_bin;
CREATE USER 'zabbix'@'localhost' IDENTIFIED BY 'Şifreniz';
GRANT ALL PRIVILEGES ON zabbix.* TO 'zabbix'@'localhost';
FLUSH PRIVILEGES;
EXIT;
```

## 📌 **5. Zabbix İçin Veritabanı Şemasını Yükleme**  

```bash
zcat /usr/share/doc/zabbix-server-mysql*/create.sql.gz | mysql -u zabbix -p zabbix
```

## 📌 **6. Zabbix Server Ayarları**  

```bash
sudo nano /etc/zabbix/zabbix_server.conf
```

**Şu satırı bulun ve DBPassword ayarını yapın, güncel sürümde bu alanın başına '#' işareti var kaldırmalısınız.**

```bash
DBPassword=Şifreniz
```

**Dosyayı kaydedin (CTRL+X, CTRL+Y, ENTER).**

## 📌 **7. Zabbix Servislerini Başlatma**  

```bash
sudo systemctl restart zabbix-server zabbix-agent apache2
sudo systemctl enable zabbix-server zabbix-agent apache2
```

**Zabbix serverleri otomatik olarak başlayacaktır eğer otomatik olarak başlatılmasını istemiyorsanız her başlatma da manuel olarak başlatmak istiyorsanız systemctl ile yapabilirsiniz.**

## 📌 **8. Zabbix Web Arayüzüne Erişim**  

```bash
http://localhost/zabbix
```

**🎯 Varsayılan Giriş Bilgileri:**
**Username: Admin**
**Password: zabbix**

**Ben localhost üzerine kurduğum için localhost ip ile başladım, farklı server alanına kuranlar http://<IP>/zabbix kısmı ile giriş yapabilirler.**


🥳 **Zabbix Network Monitor başarıyla kuruldu, tebrik ederim.**
