## 1️⃣ VMware Workstation Player Kurulumu
VMware Workstation Player'i aşağıdaki linklerden indirerek kurabilirsiniz:
- [VMware Workstation Player](https://www.vmware.com/products/workstation-player.html)

## 📌 **1. VMware Workstation 17 Player Açma**  
İlk olarak VMware Workstation Player'ı açın.

![VMware Ana Ekranı](/images/lab-setup-image0.png)

## 📌 **2. Yeni Bir Sanal Makine Oluşturma**  
VMware ana ekranında **"Create a New Virtual Machine"** seçeneğine tıklayın.

![Yeni Sanal Makine Oluşturma](images/Slab-setup-image1.png)

Burada:
- **Installer disc image file (ISO)** seçeneğini işaretleyin.
- Ubuntu 24.04 ISO dosyanızı seçin.
- **Next** butonuna tıklayın.

## 📌 **3. Kullanıcı Bilgilerini Girme (Easy Install Mode)**  
Bu adımda Ubuntu'nun otomatik kurulumu için kullanıcı bilgilerini girin:

- **Full Name:** test (Full isminizi belirleyin)  
- **User Name:** testuser (Kullanıcı adınızı belirleyin)  
- **Password:** (Güvenli bir parola belirleyin)  

![Kullanıcı Bilgileri](images/lab-setup-image2.png)

**Next** butonuna tıklayarak devam edin.

## 📌 **4. Sanal Makine İsmi ve Konumu Seçme**  
Sanal makineye bir isim verin ve kaydedileceği yeri seçin. Varsayılan olarak **"Ubuntu 64-bit"** olarak gelecektir. 

![Sanal Makine Adı](images/lab-setup-image3.png)

**Next** butonuna tıklayın.

## 📌 **5. Disk Boyutunu Ayarlama**  
Ubuntu'nun disk boyutunu belirleyin. **20 GB** önerilen boyuttur.  
İki seçenek vardır:
- **Store virtual disk as a single file:** Tek bir büyük disk dosyası oluşturur.
- **Split virtual disk into multiple files:** Daha küçük dosyalara böler (taşınabilirlik için önerilir).

![Disk Boyutu Ayarı](images/lab-setup-image4.png)

**Next** butonuna tıklayın.

## 📌 **6. Sanal Makineyi Başlatma**  
Son olarak, özet ekranında ayarları kontrol edip **"Finish"** butonuna tıklayın.  
Ubuntu sanal makineniz otomatik olarak kurulmaya başlayacaktır. 🎉  
