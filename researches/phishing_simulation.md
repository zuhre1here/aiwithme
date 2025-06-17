### Kontrollü Kimlik Avı Simülasyon Platformu Geliştirme

- **Ana Amaç:** Kullanıcıları kimlik avı saldırılarına karşı eğitmek ve davranışlarını analiz etmek.
- **Temel Özellikler:** Gerçekçi simülasyonlar, kullanıcı davranış takibi, eğitim modülleri ve raporlama.
- **Yaklaşım:** Web tabanlı bir platform, açık kaynak veya ticari çözümler kullanılabilir.
- **Teknolojiler:** Web sunucusu (Apache/Nginx), veritabanı (MySQL/PostgreSQL), e-posta servisleri (SMTP/SendGrid).
- **Mevcut Çözümler:** Açık kaynak projeler (ör. Phishing-Simulation) veya ticari platformlar (Keepnet, Mimecast).
- **Dikkat Edilmesi Gerekenler:** Gerçekçi senaryolar, kullanıcı dostu arayüz ve veri gizliliği.

#### Genel Bakış
Kimlik avı simülasyon platformları, kullanıcıların kimlik avı saldırılarını tanıma ve bunlara karşı savunma becerilerini geliştirmek için kontrollü bir ortamda sahte saldırılar oluşturur. Bu platformlar, özellikle şirket içi çalışanlar veya bireysel kullanıcılar için tasarlanabilir ve kullanıcı davranışlarını analiz ederek güvenlik farkındalığını artırır.

#### Geliştirme Süreci
Bir platform geliştirmek için web teknolojileri, veritabanı sistemleri ve e-posta servisleri kullanılabilir. Yönetim paneli, testlerin oluşturulmasını ve analizini sağlar; kullanıcı paneli ise eğitim ve test modülleri sunar. Açık kaynak projeler, geliştirme sürecini hızlandırabilir.

#### Mevcut Çözümler
Açık kaynak bir çözüm olarak [GitHub Phishing-Simulation](https://github.com/jenyraval/Phishing-Simulation) projesi, sahte alan adları ve web siteleri oluşturarak kullanıcıları test eder. Ticari çözümler arasında [Keepnet](https://keepnetlabs.com/products/phishing-simulator) ve [Mimecast](https://www.mimecast.com/content/phishing-simulation/) gibi platformlar öne çıkar.

#### Öneriler
Kendi platformunuzu geliştirmek için açık kaynak projelerden faydalanabilir veya ticari çözümleri değerlendirebilirsiniz. Kullanıcı davranışlarını analiz etmek için ayrıntılı raporlama ve gerçekçi senaryolar kritik öneme sahiptir.

---

### Kimlik Avı Simülasyon Platformu Geliştirme: Detaylı Rapor

Kimlik avı (phishing) saldırıları, siber suçluların kullanıcıları kandırarak hassas bilgileri ele geçirmeye çalıştığı yaygın bir tehdittir. Kontrollü bir kimlik avı simülasyon platformu, kullanıcıları bu tür saldırılara karşı eğitmek ve davranışlarını analiz etmek için etkili bir araçtır. Bu rapor, böyle bir platformun geliştirilmesi için gerekli bileşenleri, adımları ve mevcut çözümleri detaylı bir şekilde ele almaktadır.

#### Platformun Amacı ve Önemi
Kimlik avı simülasyon platformları, kullanıcıların gerçek dünya saldırılarını taklit eden kontrollü senaryolar aracılığıyla siber güvenlik farkındalığını artırmayı amaçlar. Araştırmalar, başarılı siber saldırıların %91’inin kimlik avı ile başladığını göstermektedir ([Riot Blog](https://tryriot.com/blog/phishing-simulation/)). Bu platformlar, kullanıcıların sahte e-postaları, web sitelerini veya diğer sosyal mühendislik tekniklerini tanımasını sağlar ve davranışlarını analiz ederek zayıf noktaları belirler. Şirket içi veya bireysel kullanıcılar için tasarlanan bu platformlar, güvenlik kültürünü güçlendirir ve veri ihlallerini önler.

#### Platformun Temel Bileşenleri
Bir kimlik avı simülasyon platformu, aşağıdaki temel bileşenleri içermelidir:

1. **Yönetim Paneli (Admin Module):**
   - Test senaryolarını oluşturma ve yönetme.
   - Kullanıcı davranışlarını izleme ve analiz etme.
   - Departmanlara özel test konfigürasyonları oluşturma.
   - Raporlama ve performans analizi.

2. **Kullanıcı Paneli (Client Module):**
   - Kimlik avı teknikleri hakkında eğitici içerikler (tutorial’ler).
   - Gerçekçi simülasyonlar (sahte e-postalar, web siteleri, SMS’ler).
   - Kullanıcıların tepkilerini değerlendiren testler.

3. **E-posta ve Web Altyapısı:**
   - Simüle edilmiş kimlik avı e-postaları göndermek için e-posta servisleri.
   - Gerçekçi sahte web siteleri oluşturmak için web sunucuları.

4. **Veri Analizi ve Raporlama:**
   - Kullanıcıların tıklamalarını, form gönderimlerini ve diğer etkileşimlerini izleme.
   - Güvenlik farkındalığı seviyesini ölçen ayrıntılı raporlar.

| **Bileşen**                | **Açıklama**                                                                 | **Örnek Teknolojiler**                     |
|----------------------------|------------------------------------------------------------------------------|--------------------------------------------|
| Yönetim Paneli             | Test oluşturma, analiz ve raporlama                                          | PHP, Python (Django/Flask), Node.js        |
| Kullanıcı Paneli           | Eğitim modülleri ve test senaryoları                                         | HTML, CSS, JavaScript, React               |
| E-posta Servisi            | Simüle edilmiş e-postalar gönderme                                           | SMTP, SendGrid, Mailgun                    |
| Veritabanı                 | Kullanıcı verileri ve test sonuçlarını saklama                               | MySQL, PostgreSQL                          |
| Web Sunucusu               | Sahte web siteleri barındırma                                                | Apache, Nginx                              |
| Analiz ve Raporlama        | Kullanıcı davranışlarını analiz etme ve raporlama                            | Grafana, Power BI, özel dashboard’lar      |

#### Geliştirme Adımları
Bir kimlik avı simülasyon platformu geliştirmek için aşağıdaki adımlar izlenebilir:

1. **Altyapı Kurulumu:**
   - **Web Sunucusu:** Apache veya Nginx gibi bir web sunucusu, sahte web sitelerini barındırmak için kullanılır.
   - **Veritabanı:** Kullanıcı verileri, test sonuçları ve analizler için MySQL veya PostgreSQL gibi bir veritabanı kurulmalıdır.
   - **E-posta Servisi:** Simüle edilmiş e-postalar göndermek için SMTP sunucuları veya [SendGrid](https://sendgrid.com/) gibi bulut tabanlı servisler kullanılabilir.

2. **Uygulama Geliştirme:**
   - **Yönetim Paneli:** Test senaryolarını oluşturmak ve analizleri görüntülemek için kullanıcı dostu bir arayüz geliştirilmelidir. Örneğin, PHP tabanlı bir yönetim paneli, [GitHub Phishing-Simulation](https://github.com/jenyraval/Phishing-Simulation) projesinde olduğu gibi kullanılabilir.
   - **Kullanıcı Paneli:** Eğitim modülleri ve test senaryoları için HTML, CSS ve JavaScript tabanlı bir arayüz oluşturulmalıdır.
   - **Simülasyonlar:** Gerçekçi sahte web siteleri ve e-postalar oluşturmak için “typosquatting” (benzer alan adları oluşturma) gibi teknikler kullanılabilir.

3. **Kullanıcı Etkileşimlerini İzleme:**
   - Kullanıcıların sahte e-postalardaki bağlantılara tıklama veya form gönderimlerini izlemek için sunucu tarafında loglama veya istemci tarafında JavaScript kullanılabilir.
   - Veriler, veritabanında saklanarak analiz edilir.

4. **Eğitim ve Geri Bildirim:**
   - Testlerde başarısız olan kullanıcılara anında geri bildirim sağlanmalı ve eğitim modülleri sunulmalıdır.
   - Örneğin, [Keepnet](https://keepnetlabs.com/products/phishing-simulator) platformu, kullanıcılara hata yaptıklarında hangi kimlik avı göstergelerini kaçırdıklarını açıklayan geri bildirimler sunar.

5. **Raporlama ve Analiz:**
   - Kullanıcı davranışlarını analiz eden raporlar, hangi çalışanların veya departmanların daha fazla eğitime ihtiyaç duyduğunu belirler.
   - [Mimecast](https://www.mimecast.com/content/phishing-simulation/) gibi platformlar, bireysel ve departman bazında risk puanları sunar.

#### Mevcut Çözümler
Piyasada hem açık kaynak hem de ticari çözümler mevcuttur:

- **Açık Kaynak Çözümler:**
  - [GitHub Phishing-Simulation](https://github.com/jenyraval/Phishing-Simulation): Bu proje, sahte alan adları ve web siteleri oluşturarak kullanıcıları test eden bir platform sunar. XAMPP ile kolayca kurulabilir ve hem yönetim hem de kullanıcı panellerini içerir. Özellikleri arasında farklı departmanlar için özelleştirilmiş testler, gerçekçi senaryolar ve analiz grafikleri yer alır.
  - **GoPhish**: Ücretsiz ve açık kaynak bir çözüm olup, mevcut e-postaları kopyalayarak simülasyonlar oluşturur. Ancak teknik bilgi gerektirir ve eğitim modülü sunmaz.

- **Ticari Çözümler:**
  - [Keepnet Phishing Simulator](https://keepnetlabs.com/products/phishing-simulator): Hızlı kampanya oluşturma, çoklu saldırı vektörleri (e-posta, SMS, QR kod) ve ayrıntılı raporlama sunar.
  - [Mimecast](https://www.mimecast.com/content/phishing-simulation/): Güvenlik farkındalığı eğitimiyle entegre, özelleştirilebilir simülasyonlar sağlar.
  - [Microsoft Attack Simulation Training](https://learn.microsoft.com/en-us/defender-office-365/attack-simulation-training-simulations): Microsoft 365 ekosistemiyle entegre, çoklu teknikler (ör. kimlik bilgisi toplama, kötü amaçlı yazılım) ve ayrıntılı raporlama sunar.
  - [PhishingBox](https://www.phishingbox.com/): Geniş şablon kütüphanesi ve özelleştirme seçenekleriyle dikkat çeker.

#### Teknoloji Yığını Önerileri
Platformu sıfırdan geliştirmek için aşağıdaki teknoloji yığını kullanılabilir:

- **Web Framework’leri:** PHP, Python (Django/Flask) veya Node.js ile yönetim ve kullanıcı panelleri geliştirilebilir.
- **Veritabanı:** MySQL veya PostgreSQL, kullanıcı verileri ve test sonuçlarını saklamak için uygundur.
- **E-posta Servisleri:** [SendGrid](https://sendgrid.com/) veya [Mailgun](https://www.mailgun.com/) gibi bulut tabanlı servisler, simüle edilmiş e-postalar göndermek için kullanılabilir.
- **İzleme ve Analiz:** Kullanıcı etkileşimlerini izlemek için sunucu tarafı loglama veya JavaScript tabanlı istemci izleme kullanılabilir. Grafana veya Power BI gibi araçlar, analiz için görselleştirme sağlayabilir.

#### Örnek Kod: Basit Bir Kimlik Avı Simülasyonu
Aşağıda, basit bir kimlik avı simülasyonu için PHP tabanlı bir yönetim paneli örneği verilmiştir. Bu kod, sahte bir giriş sayfası oluşturur ve kullanıcı girişlerini kaydeder.

```php
<?php
// Veritabanı bağlantısı
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "phishadmin";

$conn = new mysqli($servername, $username, $password, $dbname);
if ($conn->connect_error) {
    die("Bağlantı hatası: " . $conn->connect_error);
}

// Kullanıcı girişlerini kaydetme
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $email = $_POST['email'];
    $password = $_POST['password'];
    $sql = "INSERT INTO user_attempts (email, password, timestamp) VALUES ('$email', '$password', NOW())";
    $conn->query($sql);
}
?>

<!DOCTYPE html>
<html>
<head>
    <title>Sahte Giriş Sayfası</title>
</head>
<body>
    <h2>Giriş Yap</h2>
    <form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>">
        E-posta: <input type="email" name="email"><br><br>
        Şifre: <input type="password" name="password"><br><br>
        <input type="submit" value="Giriş Yap">
    </form>
</body>
</html>

<?php
$conn->close();
?>
```

Bu kod, kullanıcıların sahte bir giriş sayfasına girdiği bilgileri bir MySQL veritabanına kaydeder. Gerçek bir platformda, bu tür bir sayfa, kullanıcıları eğitmek için güvenli bir şekilde kullanılmalı ve etik kurallara uygun olmalıdır.

#### Dikkat Edilmesi Gerekenler
- **Etik ve Yasal Hususlar:** Simülasyonlar, kullanıcıların izniyle ve etik kurallara uygun şekilde yapılmalıdır.
- **Gerçekçilik:** Senaryolar, gerçek dünya saldırılarını taklit etmeli ve kullanıcıların ilgisini çekmelidir.
- **Veri Gizliliği:** Kullanıcı verileri, GDPR gibi veri koruma yasalarına uygun şekilde saklanmalıdır.
- **Kullanıcı Deneyimi:** Eğitim modülleri ve testler, kullanıcı dostu ve etkileşimli olmalıdır.

#### Sonuç
Kontrollü bir kimlik avı simülasyon platformu geliştirmek, kullanıcıların siber güvenlik farkındalığını artırmak için etkili bir yöntemdir. Açık kaynak projeler, geliştirme sürecini hızlandırabilirken, ticari çözümler daha kapsamlı özellikler sunar. Yukarıdaki adımlar ve teknolojiler, sıfırdan bir platform geliştirmek için temel bir yol haritası sağlar. Mevcut çözümleri değerlendirmek, zaman ve kaynak tasarrufu sağlayabilir.

**Key Citations:**
- [GitHub Phishing Simulation Project](https://github.com/jenyraval/Phishing-Simulation)
- [Microsoft Attack Simulation Training Documentation](https://learn.microsoft.com/en-us/defender-office-365/attack-simulation-training-simulations)
- [Keepnet Phishing Simulator Product Page](https://keepnetlabs.com/products/phishing-simulator)
- [Mimecast Phishing Simulation Overview](https://www.mimecast.com/content/phishing-simulation/)
- [Riot Blog: How to Run a Phishing Simulation](https://tryriot.com/blog/phishing-simulation/)
