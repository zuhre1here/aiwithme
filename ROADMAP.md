# Yapay Zeka Destekli Kimlik Avı Tespit Sistemi

Bu proje, e-posta metinlerini analiz ederek gelen bir e-postanın kimlik avı (phishing) olup olmadığını tespit eden bir yapay zeka sistemi geliştirmeyi amaçlamaktadır. Projenin geliştirilme süreci adım adım aşağıda açıklanmıştır.

---

## 🚀 Yol Haritası (ROADMAP)

### Adım 1: Bilgisayarı Hazırlama (Sistem Gereksinimleri ve Kurulum)

**Amaç:**
- Proje için gerekli temel donanım ve yazılım altyapısını kurmak.

**Yapılanlar:**
1. Ubuntu (veya WSL2) işletim sistemi seçimi.
2. Python, pip, Java, Node.js gibi temel yazılımların kurulumu.
```
sudo apt update
sudo apt install -y python3 python3-pip openjdk-11-jdk nodejs npm
```
3. Python sanal ortamının oluşturulması.
```
mkdir ai_phishing_detector
cd ai_phishing_detector
python3 -m venv .venv
source .venv/bin/activate
```
4. Gerekli Python kütüphanelerinin (`pandas`, `scikit-learn`, `nltk`, `joblib`) kurulumu.
```
#Önce requirements.txt dosyanızı projenizin ana dizinine (ai_phishing_detector/) oluşturun. İçeriği şu şekildedir:
pandas
scikit-learn
nltk
joblib
#Ardından komutu çalıştırın:
pip install -r requirements.txt

```
5. NLTK dil kaynaklarının (`stopwords`, `punkt`) indirilmesi.
```
python -c "import nltk; nltk.download('stopwords'); nltk.download('punkt'); nltk.download('punkt_tab')"
```
---

### Adım 2: E-postaları Toplama ve Düzenleme (Veri Hazırlama)

**Amaç:**
- Yapay zeka modelini eğitmek için kimlik avı ve meşru e-posta veri kümelerini toplamak, temizlemek ve işlemek.

**Yapılanlar:**
1. "Seven Phishing Email Datasets" veri kümesinin indirilmesi.
2. Veri dosyalarının birleştirilmesi ve temizlenmesi (`HTML etiketleri`, `URL'ler`, `durak kelimeler` kaldırıldı).
3. İşlenmiş verilerin `preprocessed_combined_emails.csv` dosyasına kaydedilmesi.

---

### Adım 3: Model Eğitimi (Basit Makine Öğrenimi Modeli)

**Amaç:**
- Temizlenmiş verileri kullanarak kimlik avı tespiti yapabilen bir makine öğrenimi modeli eğitmek.
```
python model_trainer.py
```

**Yapılanlar:**
1. TF-IDF vektörizerı ile e-posta metinlerinden sayısal özellikler çıkarıldı.
2. Lojistik Regresyon modeli eğitildi.
3. Modelin doğruluğu ve diğer performans metrikleri hesaplandı (yaklaşık %98 doğruluk).
4. Model (`phishing_detection_simple_model.joblib`) ve TF-IDF vektörizer (`tfidf_vectorizer.joblib`) kaydedildi.

---

### Adım 4: E-postaları Tahmin Etme (Model Kullanımı)

**Amaç:**
- Eğitilmiş modeli kullanarak yeni e-posta metinlerinin kimlik avı olup olmadığını tahmin etmek.

**Yapılanlar:**
1. Model ve vektörizer dosyaları yüklendi.
2. Kullanıcıdan alınan e-posta metinleri işlenip tahminler yapıldı.
3. Tahmin sonuçları ve güven olasılığı kullanıcıya sunuldu.

---

### Adım 5: Model Kararlarını Açıklama (XAI)

**Amaç:**
- Modelin kararlarının arkasındaki mantığı anlamak ve hangi kelimelerin belirli tahminlere katkıda bulunduğunu açıklamak.

**Yapılanlar:**
1. Modelin en etkili pozitif/negatif kelimeleri analiz edildi.
2. Kararların şeffaflığı artırıldı.

---

## 📋 Sistem Gereksinimleri

- **İşletim Sistemi:** Ubuntu veya WSL2
- **RAM:** En az 8 GB (16 GB önerilir)
- **Depolama:** 10 GB boş alan
- **CPU:** Modern çok çekirdekli işlemci
- **GPU:** Zorunlu değil

---

## 📂 Proje Yapısı

```
ai_phishing_detector/
├── .venv/                         # Sanal ortam klasörü
├── data/                          # Veri kümelerinin bulunduğu klasör
│   ├── 25432108/                  # İndirilen CSV dosyalarını içeren klasör
│   └── preprocessed_combined_emails.csv  # İşlenmiş veri dosyası
├── models/                        # Eğitilmiş model ve vektörizerın bulunduğu klasör
│   ├── phishing_detection_simple_model.joblib
│   └── tfidf_vectorizer.joblib
├── src/                           # Python betiklerinin bulunduğu klasör
│   ├── data_processor.py
│   ├── model_trainer.py
│   ├── predict_phishing.py
│   └── explain_model.py
├── requirements.txt               # Python bağımlılıkları listesi
└── README.md                      # Proje açıklaması
```

Bu yol haritası, projenin başından sonuna kadar tüm süreçleri kapsamaktadır. Her adımı izleyerek kolayca projeyi tamamlayabilirsiniz.
