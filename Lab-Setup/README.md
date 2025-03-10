# 🖥️ Sanal Lab Ortamı Kurulumu

Bu kılavuz, NOC mühendisliği için sanal test ortamının nasıl oluşturulacağını anlatır.

## 1️⃣ VMware Workstation Player / VirtualBox Kurulumu
VMware veya VirtualBox'u aşağıdaki linklerden indirerek kurabilirsiniz:
- [VMware Workstation Player](https://www.vmware.com/products/workstation-player.html)
- [VirtualBox](https://www.virtualbox.org/)

## 📌 **1. VMware Workstation 17 Player Açma**  
İlk olarak VMware Workstation Player'ı açın. Eğer kurulu değilse [buradan](https://www.vmware.com/products/workstation-player.html) indirebilirsiniz.

![VMware Ana Ekranı](images/Screenshot_1.png)

## 📌 **2. Yeni Bir Sanal Makine Oluşturma**  
VMware ana ekranında **"Create a New Virtual Machine"** seçeneğine tıklayın.

![Yeni Sanal Makine Oluşturma](images/Screenshot_2.png)

Burada:
- **Installer disc image file (ISO)** seçeneğini işaretleyin.
- Ubuntu 24.04 ISO dosyanızı seçin.
- **Next** butonuna tıklayın.

## 📌 **3. Kullanıcı Bilgilerini Girme (Easy Install Mode)**  
Bu adımda Ubuntu'nun otomatik kurulumu için kullanıcı bilgilerini girin:

- **Full Name:** test  
- **User Name:** testuser  
- **Password:** (Güvenli bir parola belirleyin)  

![Kullanıcı Bilgileri](images/Screenshot_3.png)

**Next** butonuna tıklayarak devam edin.

## 📌 **4. Sanal Makine İsmi ve Konumu Seçme**  
Sanal makineye bir isim verin ve kaydedileceği yeri seçin. Varsayılan olarak **"Ubuntu 64-bit"** olarak gelecektir. 

![Sanal Makine Adı](images/Screenshot_4.png)

**Next** butonuna tıklayın.

## 📌 **5. Disk Boyutunu Ayarlama**  
Ubuntu'nun disk boyutunu belirleyin. **20 GB** önerilen boyuttur.  
İki seçenek vardır:
- **Store virtual disk as a single file:** Tek bir büyük disk dosyası oluşturur.
- **Split virtual disk into multiple files:** Daha küçük dosyalara böler (taşınabilirlik için önerilir).

![Disk Boyutu Ayarı](images/Screenshot_5.png)

**Next** butonuna tıklayın.

## 📌 **6. Sanal Makineyi Başlatma**  
Son olarak, özet ekranında ayarları kontrol edip **"Finish"** butonuna tıklayın.  
Ubuntu sanal makineniz otomatik olarak kurulmaya başlayacaktır. 🎉  



Kurulum tamamlandıktan sonra ayarlarınızı aşağıdaki gibi yapılandırın, minimum olması gereken ayarlar:

| Ayar | Değer |
|------|-------|
| RAM  | 4 GB |
| CPU  | 2 Çekirdek |
| Disk | 20 GB |

## 2️⃣ Linux Sanal Makine Kurulumu
- Ubuntu 22.04 ISO dosyasını indirin: [Ubuntu Download](https://ubuntu.com/download)
- VMware veya VirtualBox’ta yeni bir sanal makine oluşturun.
- ISO dosyasını bağlayarak işletim sistemini kurun.

## 3️⃣ Ağ Yapılandırması (NAT & Bridge)
Komut satırında ağ arayüzlerini kontrol edin:
```bash
ip a
```
![Sanal Lab Ortamı](images/lab-setup-image1.png)
![Sanal Lab Ortamı](images/lab-setup-image1.png)

