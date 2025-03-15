## Ping ve Traceroute ile Ağ Analizi
**Ping ve Traceroute, ağ bağlantılarını test etmek ve paketlerin geçtiği yolları incelemek için kullanılan en temel ağ analiz araçlarından biridir. Bu rehberde şunları öğreneceğiz:**

**Ping komutu ile ağ durumu nasıl kontrol edilir?**

**Traceroute kullanarak paketlerin geçtiği yönlendiriciler nasıl analiz edilir?**

***Paket kaybı, gecikme ve yönlendirme sorunları nasıl tespit edilir?**



## 📌 **1. Ping Komutu ve Kullanımı**  

Ping, bir hedef cihazın erişilebilir olup olmadığını kontrol etmek için kullanılan basit ama güçlü bir komuttur.

🟢 Basit Kullanımı:

```bash
ping 8.8.8.8
```

🟢 IP adresine veya alan adına Ping göndermek.

```bash
ping google.com
```

🟢 Belirli bir sayıda veya farklı parametreler ile ping göndermek. Örneğin google dns adresine 4 paket gönderelim:

```bash
ping -c 4 8.8.8.8
```

🔷 **Ping Komutunun Parametreleri ve Anlamları:**
🔹 -c <sayı> → Linux/macOS için belirli bir sayıda ping paketi göndermek için kullanılır.
🔹 -n <sayı> → Windows için, belirli bir sayıda ping paketi göndermek için kullanılır. 
🔹 -i <saniye> → Her ping arasında kaç saniye bekleyeceğini belirler.
🔹 -w <süre> → Ping süresi sınırını belirler (saniye cinsinden).
🔹 -s <bayt> → Gönderilecek paket boyutunu belirler.
🔹 -q Ping çıktısını daha sessiz hale getirir, sadece özet sonuçları gösterir.

📢 **Ping Çıktısının Açıklaması:**

✅ **Bytes: Ping testinde gönderilen paketlerin boyutu.**
✅ **Time: Ping testinin tamamlanma süresi.**
✅ **Packet Transmitted: Ping testinde gönderilen paketler.**
✅ **Received: Ping testinde kabul edilen paketler.**
✅ **Packet loss: Ping testinde kaybolan veya gönderilemeyen paketler.**

**📌 Ping Kullanım Senaryoları:**

✅ Ağ bağlantısının olup olmadığını test etmek
✅ Gecikme sürelerini (latency) ölçmek
✅ Paket kaybı olup olmadığını görmek


## 📌 **2. Traceroute Komutunu ve Kullanma**  

Traceroute, bir paketin kaynaktan hedefe giderken geçtiği tüm yönlendiricileri (hops) gösteren bir komuttur.

🟢 Basit Kullanımı:

```bash
traceroute 8.8.8.8  # Linux/macOS
tracert 8.8.8.8  # Windows
```

**📢  Traceroute Çıktısının Açıklaması:**

✅ **Hop: Paketin geçtiği her bir yönlendirici**
✅ **IP Adresi / Host Adı: Her yönlendiricinin adresi**
✅ **Gecikme Süreleri: Paketin her yönlendiriciye ulaşma süresi**


**📌 Traceroute Kullanım Senaryoları:**
**✅ Ağ trafiğinin nerede yavaşladığını görmek**
**✅ Hangi yönlendiricinin paket kaybına sebep olduğunu analiz etmek**
**✅ ISP tarafında mı yoksa dahili ağda mı bir problem olduğunu belirlemek**


❗️**Ping ve Traceroute ile Ağ Sorunlarını Çözme**
**💡 Senaryo 1: İnternet Bağlantısı Kesik**
**💡 Senaryo 2: Web Sitesi Açılmıyor Ama İnternet Çalışıyor**
**💡 Senaryo 3: Ağda Yavaşlık Var (Latency Sorunu)**

