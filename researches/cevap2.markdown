# Yapay Zeka Destekli Kimlik Avı Tespit Sistemi Geliştirme: Güncel Çözümler, Gereksinimler ve Etik Uygulamalar

## I. Yönetici Özeti

Bu rapor, yapay zeka (YZ) destekli kimlik avı saldırılarının giderek artan sofistikeliğine karşı YZ tabanlı bir kimlik avı tespit sistemi geliştirmenin temel unsurlarını ele almaktadır. Geleneksel tespit yöntemlerinin yetersiz kaldığı bu tehdit ortamında, proaktif ve uyarlanabilir YZ çözümleri kritik öneme sahiptir. Sistem mimarisi için gerçek zamanlı veri akışı ve ölçeklenebilirlik gereklidir. Açıklanabilir YZ (XAI) entegrasyonu, sentetik veri kullanımı ve MLOps güvenliği, sistemin şeffaflığını, veri kalitesini ve etik standartlara uyumu artırmaktadır. İnsan faktörü, hem saldırı hedefi hem de savunma mekanizmalarının önemli bir parçası olarak, sürekli eğitimle güçlendirilmelidir.

## II. YZ Destekli Kimlik Avı Tespitine Giriş

### A. YZ Destekli Kimlik Avı Saldırılarının Gelişen Tehdit Ortamı

Siber suçlular, YZ kullanarak meşru iletişimlerden neredeyse ayırt edilemeyen kimlik avı e-postaları oluşturmaktadır. Başlıca YZ odaklı yöntemler şunlardır:

- **Gelişmiş Dil Üretimi**: GPT modelleri gibi araçlar, dilbilgisi hatalarını ortadan kaldırarak otantik görünen metinler üretir.
- **Kişiselleştirilmiş Sosyal Mühendislik**: YZ, sosyal medya ve şirket verilerini tarayarak kişiselleştirilmiş e-postalar oluşturur.
- **Gerçek Zamanlı Adaptasyon ve A/B Testi**: YZ algoritmaları, e-posta kampanyalarını optimize etmek için A/B testi uygular.
- **Deepfake Ses ve Video Entegrasyonu**: YZ, yöneticileri taklit eden deepfake mesajlar üretir.
- **YZ Tarafından Oluşturulan Alan Adları ve Sahte E-postalar**: Sahte alan adları ve oturum açma portalları oluşturulur.

2024'te siber saldırıların %75'i kimlik avı ile başlamış ve %67,4'ü YZ kullanmıştır. Bu durum, "YZ'ye Karşı YZ" dinamiği yaratmakta ve sürekli öğrenen savunma sistemlerini zorunlu kılmaktadır.

### B. Geleneksel Yöntemlerin Yetersizliği

Kural tabanlı filtreleme ve kara listeleme, yeni tehditlere uyum sağlayamaz ve yüksek yanlış pozitif/negatif oranlarına sahiptir. Erken ML teknikleri, özellik mühendisliği gerektirir ve yeni tehditlere genelleşemez. "Kara kutu" modeller, şeffaflık eksikliği nedeniyle güven ve uyumluluk sorunlarına yol açar. Bu durum, açıklanabilir YZ (XAI) entegrasyonunu zorunlu kılar.

### C. Siber Güvenlikte YZ/ML'nin Dönüştürücü Potansiyeli

YZ/ML, otomasyon, kalıp tanıma, gerçek zamanlı yanıt ve sürekli öğrenme ile siber güvenliği dönüştürmektedir. Rutin görevleri otomatikleştirerek insan kaynaklarını serbest bırakır, gizli kalıpları tespit eder ve tahmine dayalı savunmalar sağlar. Bu, reaktif yaklaşımdan proaktif paradigmaya geçişi temsil eder.

## III. Kimlik Avı Tespiti için Temel YZ/ML Çözümleri

### A. Makine Öğrenimi ve Derin Öğrenme Modelleri

#### 1. Geleneksel ML'ye Genel Bakış ve Performansları

- **Random Forest**: %98 doğruluk, yüksek kesinlik ve geri çağırma.
- **Naive Bayes**: %95.86 doğruluk.
- **Karar Ağacı**: %97.02 doğruluk.
- **Destek Vektör Makineleri (SVM)**: %98.76 doğruluk.

**Sınırlamalar**: Özellik mühendisliği gereksinimi, yeni tehditlere genelleşememe, aşırı uyum.

#### 2. Derin Öğrenme Mimarileri

- **RNN ve LSTM**: Sıralı veriler için uygun, %91.36 doğruluk.
- **CNN**: Çok modlu verilerde etkili.
- **Transformer Modelleri (BERT, RoBERTa)**: %99 doğruluk, NLP görevlerinde üstün.

**Dezavantajlar**: Yüksek hesaplama maliyeti, aşırı uyum, yorumlanabilirlik eksikliği.

#### 3. Büyük Dil Modelleri (LLM'ler)

LLM'ler, metin analizi ve bağlamsal anlama için güçlüdür. Açık kaynaklı modeller (örn. Llama3.3_70b) %91.24 F1 puanı sunar. DeepSeek v3, insan tarafından okunabilir öngörüler sağlar.

**Zorluklar**: Tescilli model sınırlamaları, yeni güvenlik açıkları, yüksek hesaplama maliyeti.

#### 4. YZ/ML Modellerinin Karşılaştırmalı Analizi

| Model Kategorisi | Modeller | Doğruluk/F1 | Yorumlanabilirlik | Eğitim Maliyeti | Çıkarım Maliyeti | Veri Gereksinimleri | Genelleşme | Dezavantajlar |
|------------------|----------|-------------|-------------------|-----------------|-----------------|---------------------|-------------|---------------|
| Geleneksel ML    | Random Forest, SVM, Naive Bayes | %96-98 | Orta-Düşük | Düşük | Düşük | Özellik Mühendisliği | Sınırlı | Aşırı uyum, opaklık |
| Derin Öğrenme    | CNN, RNN, LSTM | %91-99 | Düşük | Yüksek | Orta-Yüksek | Büyük/Çeşitli Veri | İyi | Maliyet, yorumlanabilirlik eksikliği |
| LLM'ler          | BERT, RoBERTa, DeepSeek | %90-99 | Düşük (XAI ile artırılabilir) | Çok Yüksek | Yüksek | Çok Büyük Veri | Mükemmel | Maliyet, yeni güvenlik açıkları |

### B. Model Eğitimi için Veri Stratejileri

#### 1. Yüksek Kaliteli Veri Kümeleri

Eğitim verilerinin kalitesi ve çeşitliliği, model performansını doğrudan etkiler. Gürültülü veya önyargılı veriler, zayıf tahminlere yol açar.

#### 2. Sentetik Verilerden Yararlanma

**Avantajlar**:
- Özelleştirme ve verimlilik.
- Veri gizliliği sağlama.
- Daha zengin veri üretimi.

**Zorluklar**:
- Önyargı riski.
- Model çöküşü.
- Doğruluk ve gizlilik dengesi.

#### 3. Mevcut Kimlik Avı Veri Kümeleri

- **Yedi Kimlik Avı E-posta Veri Kümesi**: 203.000 e-posta, Figshare (Mart 2024).
- **Twente Üniversitesi Veri Kümesi**: 2.000 e-posta, doğrulama için ideal (Ağustos 2024).
- **Birleştirilmiş Veri Kümesi**: 206.057 e-posta, dengeli alt örnekleme.

### C. Gelişmiş YZ Kavramlarıyla Tespiti Geliştirme

#### 1. Açıklanabilir YZ (XAI)

XAI, model şeffaflığını artırır ve güven, uyumluluk ve hata ayıklama sağlar.

- **SHAP**: Özellik katkılarını nicelendirir. Kurulum: `pip install shap`.
- **LIME**: Yerel açıklamalar üretir. Kurulum: `pip install lime`.
- **LLM'ler**: DeepSeek v3 ile insan tarafından okunabilir öngörüler.

**Sınırlamalar**: LIME'da istikrarsızlık, doğruluk-yorumlanabilirlik ödünleşimi.

#### 2. Çok Modlu YZ

Metin, görüntü ve davranışsal verileri birleştirerek sağlam tespit sağlar. Sahte haber tespitinde kullanılan teknikler, kimlik avı için uyarlanabilir.

#### 3. Davranışsal Biyometri ve Kullanıcı Profili Oluşturma

- **Özellikler**: Tuş vuruşu dinamikleri, fare hareketleri, yürüyüş analizi, ses kalıpları.
- **Avantajlar**: Sürekli kimlik doğrulama, dinamik güvenlik.
- **Zorluklar**: Doğruluk sorunları, veri gizliliği, hesaplama maliyeti.

## IV. Sistem Gereksinimleri ve Mimarisi

### A. Donanım Gereksinimleri

- **CPU**: AMD Ryzen 9, Intel Xeon (16+ çekirdek).
- **GPU**: NVIDIA A100, H100, RTX 4090.
- **RAM**: 64-128 GB (ECC önerilir).
- **Depolama**: 1 TB+ NVMe SSD, RAID desteği.

### B. İşletim Sistemleri

- **Linux (Ubuntu)**: Yüksek uyumluluk, performans ve topluluk desteği.
- **Windows (WSL2)**: Linux araçlarıyla entegrasyon.
- **macOS**: Apple ekosistemi için uygun, sınırlı yükseltme seçenekleri.

### C. Gerçek Zamanlı Veri Akışı Mimarisi

#### 1. Apache Kafka

- **Avantajlar**: Yüksek verim, düşük gecikme, hata toleransı.
- **Dezavantajlar**: Karmaşık yapılandırma, ölçeklenebilirlik zorlukları.
- **Kurulum**: Ubuntu'da OpenJDK ve Kafka hizmetleri yapılandırılır.

#### 2. Apache Flink

- **Avantajlar**: Düşük gecikme, durum bilgili hesaplamalar.
- **Dezavantajlar**: Dik öğrenme eğrisi, yüksek kaynak tüketimi.
- **Kurulum**: Confluent Cloud veya yerel kurulum.

#### 3. Apache Spark Structured Streaming

- **Avantajlar**: Basit operasyonel model, birleşik API'ler.
- **Dezavantajlar**: Daha yüksek gecikme, manuel ayarlama gereksinimi.
- **Kurulum**: Spark ikili dosyaları ve ortam değişkenleri ayarlanır.

#### 4. Karşılaştırmalı Analiz

| Özellik | Flink | Kafka Streams | Structured Streaming |
|---------|-------|---------------|---------------------|
| Gecikme | En düşük | Düşük | Daha yüksek |
| Verim | Yüksek | Kafka'ya bağlı | Daha düşük |
| Ölçeklenebilirlik | Dinamik | Bölüm bağımlı | Statik |
| Entegrasyon | Zengin konektörler | Kafka odaklı | Sınırlı |

## V. Temel Araçlar ve Kurulum

### A. Temel Araç Kurulumu

- **Python**: `pip` ile kütüphane yönetimi.
- **Node.js/npm**: React/Angular için.
- **Java (OpenJDK)**: Kafka, Flink, Spark için.

### B. Kontrol Paneli Arayüzü için Ön Uç Çerçeveler

- **Flask**: Hafif, esnek, ancak sınırlı güvenlik özellikleri. Kurulum: `pip install flask`.
- **React**: Bileşen tabanlı, performansı artıran sanal DOM. Kurulum: `npx create-react-app`.
- **Angular**: Ölçeklenebilir, iki yönlü veri bağlama. Kurulum: `npm install -g @angular/cli`.

### C. Veri Görselleştirme Kütüphaneleri

- **Matplotlib**: Esnek, ancak karmaşık çizimlerde yavaş. Kurulum: `pip install matplotlib`.
- **Seaborn**: İstatistiksel görselleştirme için optimize. Kurulum: `pip install seaborn`.
- **Plotly**: Etkileşimli, web tabanlı görselleştirmeler. Kurulum: `pip install plotly`.

### D. YZ/ML Model İnce Ayarı ve XAI Kütüphaneleri

- **Hugging Face Transformers**: BERT, RoBERTa için. Kurulum: `pip install transformers`.
- **LIME**: Yerel açıklamalar. Kurulum: `pip install lime`.
- **SHAP**: Özellik katkıları. Kurulum: `pip install shap`.
- **DeepSeek API**: İnsan tarafından okunabilir öngörüler. OpenAI SDK ile entegrasyon.

## VI. E-posta İnceleme Yöntemleri ve Etik Test Uygulamaları

### A. E-posta İçeriği ve Başlık Analizi

- **Otomatik Analiz**: YZ/ML modelleriyle metin, URL ve gönderen analizi.
- **Manuel/Destekli İnceleme**: Zoho Toolkit, EasyDMARC gibi araçlarla başlık ve URL kontrolü.
- **İnsan Dikkatliliği**: Çalışan eğitimi, şüpheli e-postaların doğrulanması.

### B. Etik Kimlik Avı Simülasyonu ve Eğitimi

#### 1. Sürekli Eğitim

İnsan hatasını azaltmak için düzenli eğitim, şüpheli e-postaların tanınmasını sağlar.

#### 2. Simülasyon Platformları

- **Gophish**: Açık kaynak, özelleştirilebilir, REST API desteği.
- **KnowBe4**: Entegre eğitim, otomatik testler, PCI uyumluluğu.
- **Mimecast**: Gerçekçi simülasyonlar, esnek eğitim sıklığı.
- **Proofpoint**: Hedefli kampanyalar, PhishAlarm ile hızlı bildirim.

#### 3. Etik Hususlar

- Kontrollü simülasyonlar, kullanıcı onayı, veri gizliliği.
- Algoritmik önyargı önleme, insan denetimi (HITL).
- Güvenli veri işleme, model provenansı, CI/CD güvenliği.

### C. YZ Sistem Güvenlik Açıkları ve Azaltılması

#### 1. YZ'ye Özgü Saldırılar

- **Zehirlenme**: Düşmanca eğitim, veri doğrulama.
- **Çıkarma**: API kısıtlamaları, diferansiyel gizlilik.
- **Kaçınma**: Sağlam özellik çıkarma.
- **İstem Enjeksiyonu**: Katı girdi doğrulaması.

#### 2. Genel Riskler

- Altyapı güvenliği, tedarik zinciri saldırıları, yanal hareket.

#### 3. MLOps Güvenliği

- Güvenli veri işleme, model filigranlama, ağ segmentasyonu.
- Sürekli izleme, güvenlik denetimleri.

#### 4. Mevcut Sistemlerle Entegrasyon Zorlukları

- **YZ Bozulmaları**: Doğrulama, insan denetimi.
- **Veri Gizliliği**: Anonimleştirme, erişim kontrolleri.

## VII. Sonuç

YZ destekli kimlik avı tespit sistemi, yüksek performanslı modeller, sentetik veri, gerçek zamanlı veri akışı ve etik uygulamalar gerektirir. XAI, güven ve uyumluluğu artırırken, davranışsal biyometri ve çok modlu YZ sağlamlık sağlar. Sürekli eğitim ve güvenli MLOps, sistem etkinliğini maksimize eder.