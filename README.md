<div align="center">
  <img src="https://img.shields.io/github/languages/count/zuhre1here/aiwithme?style=flat-square&color=blueviolet" alt="Language Count">
  <img src="https://img.shields.io/github/languages/top/zuhre1here/aiwithme?style=flat-square&color=1e90ff" alt="Top Language">
  <img src="https://img.shields.io/github/last-commit/zuhre1here/aiwithme?style=flat-square&color=ff69b4" alt="Last Commit">
  <img src="https://img.shields.io/github/license/zuhre1here/aiwithme?style=flat-square&color=yellow" alt="License">
  <img src="https://img.shields.io/badge/Status-Active-green?style=flat-square" alt="Status">
  <img src="https://img.shields.io/badge/Contributions-Welcome-brightgreen?style=flat-square" alt="Contributions">
</div>

# Yapay Zeka Destekli Kimlik Avı Tespit Sistemi

Yapay Zeka Destekli Kimlik Avı Tespit Sistemi projesi,
e-posta ve web tabanlı kimlik avı saldırılarını yapay zeka ve 
derin öğrenme (özellikle transformatör modelleri) kullanarak,
gerçek zamanlı ve akıllı bir şekilde belirlemeyi hedefler.
Bu sistem, sosyal mühendislik taktiklerini ve görsel aldatmacaları dahi
tespit ederek kullanıcıları en yeni ve sofistike tehditlerden korur.
Tüm sonuçlar, kolay anlaşılır etkileşimli bir web arayüzünde sunulur.

---

## Features / *Özellikler*

**Real-time Phishing Detection:**  
*Scans incoming emails and analyzed web pages in real-time to instantly identify and flag phishing attempts before they can cause harm.*  
**Gerçek Zamanlı Kimlik Avı Tespiti:** Gelen e-postaları ve analiz edilen web sayfalarını gerçek zamanlı olarak tarayarak, zarar vermeden önce kimlik avı girişimlerini anında tanımlar ve işaretler.

**Advanced AI-Powered Analysis:**  
*Leverages state-of-the-art deep learning models (e.g., Transformers like BERT/RoBERTa) and Large Language Models (LLMs) for a profound understanding of email content, headers, and URLs, catching even the most sophisticated, AI-generated phishing.*  
**Gelişmiş YZ Destekli Analiz:** E-posta içeriği, başlıkları ve URL'lerinin derinlemesine anlaşılması için son teknoloji derin öğrenme modelleri (örneğin, BERT/RoBERTa gibi Transformatörler) ve Büyük Dil Modelleri (LLM'ler) kullanır, böylece en sofistike, YZ tarafından oluşturulmuş kimlik avı saldırılarını bile yakalar.

**Social Engineering and Visual Deception Detection:**  
*Goes beyond text to identify psychological manipulation tactics (e.g., urgency, authority impersonation) and visual brand impersonation (e.g., fake logos, deceptive layouts) using multimodal AI.*  
**Sosyal Mühendislik ve Görsel Aldatma Tespiti:** Metnin ötesine geçerek, psikolojik manipülasyon taktiklerini (örneğin, aciliyet, otorite taklidi) ve görsel marka taklitlerini (örneğin, sahte logolar, yanıltıcı düzenler) çok modlu YZ kullanarak tespit eder.

**User-Friendly & Explainable Results:**  
*Presents complex threat analysis, risk scores, and the reasoning behind detections through an intuitive, interactive web dashboard (Flask), enhancing user understanding and trust.*  
**Kullanıcı Dostu ve Açıklanabilir Sonuçlar:** Karmaşık tehdit analizlerini, risk puanlarını ve tespitlerin arkasındaki nedenleri sezgisel, etkileşimli bir web panosu (Flask) aracılığıyla sunarak kullanıcı anlayışını ve güvenini artırır.

**Scalable Real-time Architecture:**  
*Built on robust streaming technologies like Apache Kafka and Apache Flink, ensuring high-throughput, low-latency processing for analyzing large volumes of email traffic efficiently.*  
**Ölçeklenebilir Gerçek Zamanlı Mimari:** Apache Kafka ve Apache Flink gibi sağlam akış teknolojileri üzerine inşa edilmiştir, bu da yüksek hacimli e-posta trafiğini verimli bir şekilde analiz etmek için yüksek verim ve düşük gecikmeli işlem sağlar.

## Team / *Ekip*

- **242*****009** - Zührenaz Mısır: *Tüm proje sahibi.*
---

## Roadmap / *Yol Haritası*

*Yol haritasına göz atın: ROADMAP.md*

---

## Research / *Araştırmalar*

| Topic / *Başlık*                              | Link                                                      | Description / *Açıklama*                                                                                              |
|-----------------------------------------------|-----------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| Automated Phishing Simulation and Training Platform | [researchs/phishing_simulation.md](researchs/phishing_simulation.md) | Development of a controlled phishing simulation platform to educate and train users against phishing attacks, including user behavior analysis. / *Şirket içi veya bireysel kullanıcıları kimlik avı saldırılarına karşı eğitmek ve davranışlarını analiz etmek için kontrollü bir kimlik avı simülasyon platformunun geliştirilmesi.* |
| Phishing Email Generation and Delivery        | [researchs/phishing_email.md](researchs/phishing_email.md) | Techniques for creating realistic phishing emails using Python's smtplib library, mimicking common scenarios like bank notifications or package tracking, while bypassing spam filters. / *Python'ın smtplib kütüphanesi kullanılarak banka bildirimleri veya kargo takibi gibi yaygın senaryoları taklit eden gerçekçi kimlik avı e-postaları oluşturma teknikleri ve spam filtrelerini aşma yöntemleri.* |
| Web Page Cloning for Phishing Simulations     | [researchs/web_cloning.md](researchs/web_cloning.md)       | Methods to clone authentic-looking login pages using tools like wget or Python's requests and BeautifulSoup libraries, hosted on a Flask server to capture user inputs securely. / *Wget veya Python'ın requests ve BeautifulSoup kütüphaneleri kullanılarak gerçekçi görünen giriş sayfalarını kopyalama yöntemleri ve kullanıcı girişlerini güvenli bir şekilde yakalamak için Flask sunucusu kullanımı.* |
| User Behavior Tracking and Logging            | [researchs/behavior_tracking.md](researchs/behavior_tracking.md) | Implementation of a Python-based logging system to monitor user interactions with phishing emails and cloned web pages, such as email opens, link clicks, and data submissions. / *Kullanıcıların kimlik avı e-postaları ve kopyalanmış web sayfalarıyla etkileşimlerini (e-posta açma, linke tıklama, veri girişi) izlemek için Python tabanlı bir loglama sisteminin uygulanması.* |
| Training and Reporting System                 | [researchs/training_reporting.md](researchs/training_reporting.md) | Analysis of simulation results to identify at-risk users and provide tailored training materials, along with generating comprehensive reports for organizational awareness. / *Simülasyon sonuçlarının analizi ile risk altındaki kullanıcıların belirlenmesi, özelleştirilmiş eğitim materyalleri sunulması ve organizasyonel farkındalık için kapsamlı raporlar oluşturulması.* |
---

## Installation / *Kurulum*

1. **Clone the Repository / *Depoyu Klonlayın***:  
   ```bash
   git clone https://github.com/zuhre1here/ai_phishing_detector.git
   cd ai_phishing_detector
   ```

2. **Set Up Virtual Environment / *Sanal Ortam Kurulumu*** (Recommended):  
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies / *Bağımlılıkları Yükleyin***:  
   ```bash
   pip install -r requirements.txt
   ```
---


---
## Usage / *Kullanım*

To run your Phishing Email Detection System, follow the sequential steps below:
*Kimlik Avı Tespit Sistemi projenizi çalıştırmak için aşağıdaki sıralı adımları takip edin:*

**Prerequisites / *Ön Koşullar***:
Ensure your Python virtual environment is activated before running any scripts.
*Herhangi bir betiği çalıştırmadan önce Python sanal ortamınızın etkin olduğundan emin olun.*

```bash
cd /path/to/your/ai_phishing_detector # Projenizin ana dizinine gidin
source .venv/bin/activate             # Sanal ortamı etkinleştirin
```

**Steps / *Adımlar***:

### 1. Data Processing and Preparation / *1. Veri İşleme ve Hazırlama*
This step cleans and prepares your raw email data, saving it as a single processed CSV file.
*Bu adım, ham e-posta verilerinizi temizler ve hazırlar, tek bir işlenmiş CSV dosyası olarak kaydeder.*

```bash
python src/data_processor.py
```

* **Output / *Çıktı***: `data/preprocessed_combined_emails.csv` will be generated.
* *`data/preprocessed_combined_emails.csv` dosyası oluşturulacaktır.*

### 2. Model Training / *2. Model Eğitimi*
This step trains the Logistic Regression model using your processed data and saves the trained model and TF-IDF vectorizer.
*Bu adım, işlenmiş verilerinizi kullanarak Lojistik Regresyon modelini eğitir ve eğitilmiş modeli ile TF-IDF vektörizerını kaydeder.*

```bash
python src/model_trainer.py
```

* **Output / *Çıktı***: `models/phishing_detection_simple_model.joblib` (trained model) and `models/tfidf_vectorizer.joblib` (TF-IDF vectorizer) will be saved. You will also see model performance metrics.
* *`models/phishing_detection_simple_model.joblib` (eğitilmiş model) ve `models/tfidf_vectorizer.joblib` (TF-IDF vektörizerı) kaydedilecektir. Ayrıca model performans metriklerini de göreceksiniz.*

### 3. Phishing Prediction / *3. Kimlik Avı Tahmini*
Use this script to test the trained model by inputting new email texts.
*Bu betiği, eğitilmiş modeli kullanarak yeni e-posta metinlerini girerek test etmek için kullanın.*

```bash
python src/predict_phishing.py
```

* **Usage / *Kullanım***: The program will prompt you to enter an email text. Paste your text and press Enter. It will provide the prediction result and its confidence. Type `q` and press Enter to quit.
* *Program sizden e-posta metni girmenizi isteyecektir. Metni yapıştırın ve Enter'a basın. Tahmin sonucunu ve güven olasılığını göreceksiniz. Çıkmak için `q` yazıp Enter'a basın.*

### 4. Model Explanation (XAI) / *4. Model Açıklaması (XAI)*
This step helps understand the model's decision-making by showing the most influential words/phrases for classifying emails as phishing or legitimate.
*Bu adım, e-postaları kimlik avı veya meşru olarak sınıflandırmada en etkili olan kelime/ifadeleri göstererek modelin karar verme mekanizmasını anlamanıza yardımcı olur.*

```bash
python src/explain_model.py
```

* **Output / *Çıktı***: You will see lists of words that contribute most to "phishing" and "legitimate" predictions.
* *Modelin "phishing" ve "legitimate" tahminlerine en çok katkıda bulunan kelime listelerini göreceksiniz.*

---

## Contributing / *Katkıda Bulunma*

We welcome contributions! To help:  
1. Fork the repository.  
2. Clone your fork (`git clone git@github.com:YOUR_USERNAME/ai_phishing_detector.git`).  
3. Create a branch (`git checkout -b feature/your-feature`).  
4. Commit changes with clear, descriptive messages.  
5. Push to your fork (`git push origin feature/your-feature`).  
6. Open a Pull Request.  

*Topluluk katkılarını memnuniyetle karşılıyoruz! Katkıda bulunmak için yukarıdaki adımları izleyin ve kodlama standartlarımıza uyun.*
-->
---

## License / *Lisans*

Licensed under the [MIT License](LICENSE).  
*MIT Lisansı altında lisanslanmıştır.*

---
Thanks to:
- Keyvan Arasteh Abbasabad

*Teşekkürler: İstinye Üniversitesi’ne yenilikçi akademik ortamı için, Scapy ve Psutil kütüphanelerine güçlü ve güvenilir destekleri için, açık kaynak topluluğuna ilham ve iş birliği için.*

---

## Contact / *İletişim* (Optional)

Project Maintainer: Zührenaz Mısır - [zuhrenazmisir@gmail.com] 
Found a bug? Open an issue.  

*Proje Sorumlusu: Zührenaz Mısır - [zuhrenazmisir@gmail.com]. Hata bulursanız bir sorun bildirin.*
### -->
