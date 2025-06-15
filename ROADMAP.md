# Yapay Zeka Destekli Kimlik Avı Tespit Sistemi

## Giriş
Siber güvenlik dünyasına hoş geldiniz! Bu yol haritası, e-postalarla gelen kötü niyetli saldırıları (kimlik avı) yakalayabilen akıllı bir sistemin nasıl oluşturulacağını adım adım açıklıyor. Bu proje, hem bilgisayar bilimleri bilginizi geliştirecek hem de siber dünyayı daha güvenli hale getirmeye yardımcı olacak. Hazır mısınız? Başlayalım!

## 1. Bilgisayarını Hazırla (Sistem Gereksinimleri ve Kurulum)
Bu projeye başlamadan önce bilgisayarınızın güçlü olması ve doğru yazılımların yüklü olması gerekiyor.

---

### İşletim Sistemi Seçimi
* **Öneri:** **Ubuntu (Linux)** kullanmanız şiddetle tavsiye edilir. Yapay zeka ve makine öğrenimi araçları genellikle Linux için daha iyi çalışır ve daha hızlıdır.
* **Alternatif:** Eğer Windows kullanıyorsanız, **Windows için Linux Alt Sistemi (WSL2)** kurabilirsiniz. Bu, Windows içinde bir Linux bilgisayar çalıştırmanıza olanak tanır, böylece hem Windows'un kolaylığını hem de Linux'un gücünü bir arada kullanabilirsiniz.

---

### Bilgisayar Donanımı (Gereksinimler)
* **Beyin (CPU):** Bilgisayarınızın ana işlemcisi. Verileri düzenlemek ve genel sistemin hızlı çalışması için önemlidir. En az **8 çekirdekli bir işlemci** (örneğin AMD Ryzen 7700X veya Intel Core i7-14700K) iyi olur.
* **Hızlandırıcı (GPU):** Yapay zeka modellerini eğitmek için çok önemlidir. **NVIDIA'nın RTX serisi** (örneğin RTX 4070 veya RTX 4090) gibi bir ekran kartı, büyük verileri hızlıca işlemenizi sağlar. Ekran kartının belleği (VRAM) ne kadar büyükse, o kadar iyi (**en az 12 GB, tercihen 24 GB veya daha fazla**).
* **Kısa Süreli Bellek (RAM):** Bilgisayarınızın aynı anda ne kadar bilgiyi aklında tutabildiğini gösterir. Büyük veri kümeleriyle çalışırken çok RAM'e ihtiyacınız olacak. **En az 32 GB RAM** önerilir, ancak 64 GB veya 128 GB daha büyük projeler için daha iyidir.
* **Depolama (SSD):** Verilerinizi hızlıca okuyup yazabilen bir depolama birimi. **NVMe SSD'ler** en hızlısıdır. **En az 500 GB NVMe SSD** önerilir, ancak 1 TB veya daha fazlası daha iyidir.

---

### Temel Yazılımları Kur
* **Python:** Yapay zeka projelerinin ana dilidir. Bilgisayarınıza Python'ı kurun.
* **pip:** Python paketlerini yüklemek için kullanılır. Python ile birlikte gelir.
* **Java (OpenJDK):** Bazı büyük veri araçları (Kafka, Flink, Spark) Java ile çalışır. OpenJDK'yı kurun.
* **Node.js ve npm:** Web arayüzü geliştirmek için gereklidir.

## 2. E-postaları Topla ve Düzenle (Veri Toplama ve Hazırlama)
Yapay zeka modeliniz, kimlik avı e-postalarını tanımayı öğrenmek için çok sayıda e-posta örneğine ihtiyaç duyar.

---

### Gerçek E-posta Veri Kümeleri Bul
* **"Seven Phishing Email Datasets" (Figshare):** Mart 2024'te yayınlanmış, 203.000'den fazla e-posta içeren büyük bir koleksiyon. Modelinizi eğitmek için harika bir başlangıç noktası.
* **University of Twente Veri Kümesi:** Ağustos 2024'ten yeni, 2.000 e-posta ile modelinizi test etmek için kullanabilirsiniz.

Bu veri kümelerini internetten indirin.

---

### Sentetik Veri Oluşturmayı Düşün
Gerçek e-postalar her zaman yeterli veya gizlilik açısından uygun olmayabilir. Yapay zeka (üretken YZ) kullanarak sahte ama gerçekçi kimlik avı e-postaları oluşturabilirsiniz. Bu, modelinizin yeni saldırı türlerini öğrenmesine yardımcı olur.

---

### Verileri Temizle ve Hazırla
* E-postalardaki HTML etiketlerini, sayıları, noktalama işaretlerini ve çok sık geçen kelimeleri (durak kelimeler) kaldırın.
* Tüm metni küçük harfe dönüştürün.
* Metni "belirteçlere" (kelimelere veya kelime parçalarına) ayırın (**tokenization**).

## 3. Akıllı Beyni Seç ve Eğit (Model Seçimi ve Eğitimi)
Şimdi sisteminizin "beynini" oluşturma zamanı. Bu beyin, e-postaların kimlik avı olup olmadığını anlayacak.

---

### Model Türünü Seç
* **Öneri:** **Dönüştürücü Modeller (Transformer Models)** kullanın. BERT, RoBERTa veya DistilBERT gibi modeller, e-postaların dilini çok iyi anlar ve kimlik avı tespitinde en yüksek doğruluğu sağlar (ortalama %99'a kadar).
* Bu modelleri "**ince ayar**" (fine-tuning) yaparak kendi kimlik avı veri kümenize göre eğitebilirsiniz.

---

### Modelini Eğit
* **Hugging Face Transformers** kütüphanesini kurun: `pip install transformers`.
* Bu kütüphaneyi kullanarak seçtiğiniz modeli (örneğin DistilBERT) yükleyin ve hazırladığınız veri kümesiyle eğitin.

---

### Modelinin Ne Kadar İyi Olduğunu Ölç
* **Doğruluk (Accuracy):** Modeliniz ne kadar doğru tahmin yapıyor?
* **Kesinlik (Precision):** Modelinizin "kimlik avı" dediği e-postaların ne kadarı gerçekten kimlik avı?
* **Duyarlılık (Recall):** Gerçek kimlik avı e-postalarının ne kadarını modeliniz yakalayabiliyor?
* **F1 Skoru:** Kesinlik ve duyarlılık arasında bir denge sağlar.

## 4. E-postaları Mercek Altına Al (E-posta İnceleme ve Özellik Çıkarma)
Sisteminiz, e-postaların farklı bölümlerini inceleyerek ipuçları bulacak.

---

### E-posta Başlıklarını İncele
* **Nasıl Yapılır:** Zoho Toolkit gibi çevrimiçi araçları kullanabilirsiniz. Şüpheli bir e-postanın "orijinal mesajını" kopyalayıp bu araca yapıştırın.
* **Nelere Bakılır:**
    * **Gönderen IP Adresi ve Rotası:** E-postanın nereden geldiğini ve hangi sunuculardan geçtiğini gösterir.
    * **Kimlik Doğrulama Sonuçları (SPF, DKIM, DMARC):** Gönderenin gerçekten iddia ettiği kişi olup olmadığını kontrol eder. Geçersiz veya eksik sonuçlar şüphelidir.
    * **Gönderen ve Yanıt Adresleri:** Gönderen adresi güvenilir görünse de, yanıt adresinin farklı veya şüpheli olup olmadığını kontrol edin.

---

### URL'leri Analiz Et
* **Nasıl Yapılır:** EasyDMARC'ın Kimlik Avı Bağlantı Denetleyicisi gibi araçları kullanabilirsiniz. Şüpheli bir bağlantıyı bu araca yapıştırın.
* **Nelere Bakılır:**
    * **Alan Adı Benzerliği:** URL'nin meşru bir siteye (örneğin Google, Facebook) çok benzeyip benzemediğini kontrol edin (örneğin "[https://www.google.com/search?q=Go0gle.com](https://www.google.com/search?q=Go0gle.com)" gibi).
    * **URL Yapısı:** Karmaşık alt alan adları veya "login", "bank" gibi kelimeler içerip içermediğini kontrol edin.
    * **HTTPS Kullanımı:** Kimlik avı siteleri de artık meşru görünmek için HTTPS kullanabilir, bu yüzden sadece HTTPS'ye güvenmeyin.

---

### E-posta İçeriğini Analiz Et (Doğal Dil İşleme - NLP)
Modeliniz, e-postanın metnini analiz ederek sosyal mühendislik taktiklerini (örneğin aciliyet, korku, otorite) tespit etmeye çalışacak. Büyük Dil Modelleri (LLM'ler) bu konuda çok iyidir, çünkü metnin tonunu, niyetini ve dilsel nüanslarını anlayabilirler.

## 5. E-postaları Anında Yakala (Gerçek Zamanlı Akış Mimarisi)
Kimlik avı saldırıları çok hızlı yayılır, bu yüzden sisteminizin e-postaları anında kontrol etmesi gerekir.

---

### Veri Taşıyıcı (Apache Kafka)
E-postaların sisteme sürekli ve hızlı bir şekilde akmasını sağlar. Yüksek hacimli verileri güvenilir bir şekilde taşır.
* **Kurulum (Ubuntu):** Sisteminizi güncelleyin, OpenJDK'yı kurun, Kafka'yı indirin ve çıkarın. Zookeeper ve Kafka hizmetlerini yapılandırın ve başlatın.
* **Kurulum (Windows/WSL2):** WSL2 ve Java'yı kurun. Zookeeper ve Kafka sunucusunu başlatın.

---

### Veri İşleyici (Apache Flink veya Spark Streaming)
Kafka'dan gelen e-postaları gerçek zamanlı olarak analiz eder ve kimlik avı olup olmadığını belirler.
* **Apache Flink:** Çok düşük gecikme süresiyle karmaşık analizler için iyidir.
    * **Kurulum:** Confluent Cloud Flink hızlı başlangıç eklentisini kullanabilir veya yerel olarak kurabilirsiniz.
* **Apache Spark Structured Streaming:** Büyük veri kümeleri üzerinde gerçek zamanlı analizler için güçlüdür.
    * **Kurulum (Ubuntu):** Spark ikili dosyalarını indirin ve çıkarın, ortam değişkenlerini ayarlayın.

## 6. Sonuçları Göster (Web Arayüzü ve Görselleştirme)
Güvenlik analistlerinin ve kullanıcıların sistemin ne yaptığını kolayca anlaması için görsel bir arayüze ihtiyacınız olacak.

---

### Arka Plan (Flask)
Python ile hafif web uygulamaları oluşturmak için kullanılır. Model sonuçlarını web arayüzüne sunmak için API'ler sağlayabilir.
* **Kurulum:** `pip install flask`.
* **Kullanım:** `app.py` gibi bir dosya oluşturun, rotaları tanımlayın (`@app.route("/")`), HTML şablonlarını kullanın (`render_template`).

---

### Ön Plan (React veya Angular)
Dinamik ve etkileşimli kontrol panelleri oluşturmak için kullanılır.
* **React:** Bileşen tabanlıdır, kullanıcı arayüzleri oluşturmak için popülerdir.
    * **Kurulum:** Node.js ve npm'i kurun. `npx create-react-app my-app` ile yeni bir proje oluşturun.
* **Angular:** Ölçeklenebilir web uygulamaları için tasarlanmıştır, güçlü özelliklere sahiptir.
    * **Kurulum:** Node.js ve npm'i kurun. `npm install -g @angular/cli` ile Angular CLI'yı kurun. `ng new my-app` ile yeni bir uygulama oluşturun.

---

### Grafikler ve Çizelgeler (Veri Görselleştirme Kütüphaneleri)
* **Plotly:** Etkileşimli grafikler oluşturmak için harikadır. Kullanıcıların yakınlaştırma, detaylara inme gibi özellikler sunar.
    * **Kurulum:** `pip install plotly`.
* **Matplotlib:** Python'ın temel çizim kütüphanesidir.
    * **Kurulum:** `pip install matplotlib`.
* **Seaborn:** Matplotlib üzerine kuruludur, daha güzel görünümlü istatistiksel grafikler oluşturmayı kolaylaştırır.
    * **Kurulum:** `pip install seaborn`.

---

### Siber Güvenlik Kontrol Paneli Tasarım İlkeleri
* **Önemli Bilgileri Öne Çıkar:** En kritik güvenlik uyarılarını (örneğin, risk skorları) en başta gösterin.
* **Hızlı Yanıt İçin Tasarla:** Analistlerin doğrudan arayüzden tehditlere yanıt vermesini sağlayın.
* **Net Görsel Hiyerarşi:** Renk, boyut ve yazı tipini stratejik olarak kullanarak en önemli verilerin öne çıkmasını sağlayın.
* **Gerçek Zamanlı Veri:** Kontrol panelinin canlı verileri anında işlemesini sağlayın (WebSockets gibi teknolojiler kullanabilirsiniz).

## 7. Nedenini Anla (Açıklanabilir Yapay Zeka - XAI)
Modelinizin bir e-postayı neden kimlik avı olarak işaretlediğini anlamak, sisteme güvenmek ve hataları düzeltmek için çok önemlidir.

---

### LIME ve SHAP Kullan
Bu kütüphaneler, modelin tahminlerinin arkasındaki nedenleri anlamana yardımcı olur.
* **LIME:** Belirli bir tahmin için hangi kelimelerin veya özelliklerin etkili olduğunu gösterir.
    * **Kurulum:** `pip install lime`.
* **SHAP:** Her bir özelliğin modelin tahminine ne kadar katkıda bulunduğunu sayısal olarak gösterir.
    * **Kurulum:** `pip install shap`.

---

### LLM'leri Açıklama İçin Kullan (DeepSeek API)
DeepSeek V3 gibi Büyük Dil Modelleri, LIME ve SHAP'tan gelen teknik açıklamaları, insanların anlayabileceği basit bir dile çevirebilir.
* **Erişim:** DeepSeek API Platformu'ndan bir API anahtarı alın.
* **Kullanım:** OpenAI SDK ile uyumludur. Python kütüphanesini kullanarak API anahtarını ve modelinizi ayarlayın, sonra mesajları gönderin.

## 8. Kullanıcıyı Tanı (Davranışsal Analiz ve Kullanıcı Profili Oluşturma)
Sisteminiz, bir kullanıcının normal davranışını öğrenerek, bir saldırganın o kullanıcının yerine geçmeye çalıştığını anlamasına yardımcı olabilir.

---

### Davranışsal Biyometri
Kullanıcıların klavye yazma ritmi, fare hareketleri, dokunmatik ekran kullanımı gibi benzersiz davranışsal özelliklerini analiz eder. Bu, şifreler çalınsa bile dolandırıcılığı tespit etmeye yardımcı olabilir.

---

### Anomali Tespiti
Yapay zeka, kullanıcının normal davranış kalıplarından sapmaları (örneğin, alışılmadık bir yerden giriş yapma) tespit edebilir.

## 9. Sistemi Güçlendir (MLOps Uygulamaları ve Etik Test)
Sisteminizin güvenli, güncel ve sürekli öğrenen bir şekilde çalışmasını sağlamak için bazı önemli adımlar var.

---

### MLOps (Makine Öğrenimi Operasyonları)
Bu, yapay zeka modelinin yaşam döngüsü boyunca (eğitim, dağıtım, izleme) güvenliğini ve verimliliğini yönetme pratiğidir.
* **Sürekli İzleme:** Modelinizin performansını, kullanımını ve hatalarını gerçek zamanlı olarak izleyin.
* **Sürekli Yeniden Eğitim:** Kimlik avı saldırıları sürekli değiştiği için, modelinizi düzenli olarak yeni verilerle yeniden eğitmeniz gerekir.

---

### Etik Kimlik Avı Simülasyonu ve Eğitimi
* **Neden Önemli:** İnsan hatası siber güvenlikteki en büyük zayıflıklardan biridir. Çalışanları kimlik avı saldırılarını tanımaları konusunda eğitmek çok önemlidir.
* **Simülasyon Platformları:**
    * **Gophish (Açık Kaynak):** Kendi kimlik avı simülasyonlarınızı oluşturmak ve yönetmek için kullanabilirsiniz. E-posta şablonlarını ve açılış sayfalarını özelleştirebilirsiniz.
    * **KnowBe4, Mimecast, Proofpoint:** Ticari platformlar olup, gerçekçi kimlik avı e-postaları göndererek çalışanların farkındalığını ölçer ve eğitim sağlar.
* **Etik Kurallar:**
    * Simülasyonları her zaman izin alarak ve kontrollü bir ortamda yapın.
    * Elde ettiğiniz sonuçları sadece eğitim ve savunmaları güçlendirmek için kullanın.
    * Veri Gizliliği: Hassas verileri koruyun, anonimleştirme teknikleri kullanın.
    * İnsan Denetimi: Yapay zekaya aşırı güvenmeyin. Kritik kararlar için her zaman insan denetimi (Human-in-the-Loop) olmalı.

## 10. Öğrenmeye Devam Et (Asla Durma)
Siber güvenlik ve yapay zeka alanları sürekli gelişiyor. Bu yüzden siz de sürekli öğrenmeye devam etmelisiniz. Yeni araştırma makalelerini okuyun, yeni araçları deneyin ve topluluklarla etkileşimde kalın.

Bu yol haritası, yapay zeka destekli kimlik avı tespit sistemi projenizi başarıyla tamamlamanız için size rehberlik edecektir. Her adımda bol şans ve başarılar dilerim!
