import joblib
import os
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Temizleme fonksiyonunu tekrar tanımlıyoruz
def clean_text(text):
    """
    Metni temizler: HTML etiketlerini, özel karakterleri kaldırır, küçük harfe çevirir
    ve durak kelimeleri çıkarır.
    """
    if not isinstance(text, str):
        return "" 

    text = re.sub(r'<.*?>', '', text)
    text = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', text)
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    text = text.lower()
    words = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in words if word not in stop_words]
    return ' '.join(filtered_words)

# Kaydedilmiş model ve vektörizer yolları
model_path = os.path.join(os.path.dirname(__file__), 'phishing_detection_simple_model.joblib')
vectorizer_path = os.path.join(os.path.dirname(__file__), 'tfidf_vectorizer.joblib')

try:
    model = joblib.load(model_path)
    vectorizer = joblib.load(vectorizer_path)
    print("Model ve TF-IDF vektörizer başarıyla yüklendi.")
except FileNotFoundError:
    print(f"Hata: Model veya vektörizer dosyaları bulunamadı. Lütfen '{os.path.dirname(__file__)}' klasöründe 'phishing_detection_simple_model.joblib' ve 'tfidf_vectorizer.joblib' dosyalarının olduğundan emin olun.")
    exit()
except Exception as e:
    print(f"Model veya vektörizer yüklenirken bir hata oluştu: {e}")
    exit()

# Modelin "phishing" olarak kabul etmesi için gereken minimum olasılık eşiği
# Bu değeri 0.5 ile 1.0 arasında değiştirebilirsiniz. Daha yüksek bir değer,
# modelin "phishing" demeden önce daha emin olmasını sağlar, yanlış pozitifleri azaltır
# ancak gerçek phishing'leri kaçırma riskini artırabilir.
# Genellikle varsayılan 0.5 kullanılır, ancak kısa metinler için daha yüksek bir eşik deneyebilirsiniz.
PHISHING_THRESHOLD = 0.7

def predict_email_phishing(email_text):
    """
    Verilen e-posta metninin kimlik avı olup olmadığını tahmin eder.
    Temizlenmiş metin boşsa özel bir mesaj döner.
    """
    cleaned_email = clean_text(email_text)
    
    if not cleaned_email.strip():
        return "Giriş metni boş veya anlamsız kelimeler içeriyor. Tahmin yapılamadı.", 0.0 # Olasılığı da 0 döndür
    
    email_tfidf = vectorizer.transform([cleaned_email])
    
    # Modelin her sınıf için olasılıklarını al
    # predict_proba metodu, sınıflandırıcının her sınıf için olasılık tahmini döndürür.
    probabilities = model.predict_proba(email_tfidf)[0]
    
    # 'phishing' sınıfının olasılığı (genellikle 1. index)
    phishing_probability = probabilities[1] 
    
    # Olasılık eşiğine göre tahmin yap
    if phishing_probability >= PHISHING_THRESHOLD:
        prediction_label = "Kimlik Avı (Phishing)"
    else:
        prediction_label = "Meşru (Legitimate)"
        
    return prediction_label, phishing_probability

if __name__ == "__main__":
    print("\nKimlik Avı Tespit Sistemi - Tahmin Modu")
    print("--------------------------------------")
    print(f"Kimlik Avı Tespit Eşiği (PHISHING_THRESHOLD): {PHISHING_THRESHOLD}")
    print("Çıkmak için 'q' yazıp Enter'a basın.")

    while True:
        email_input = input("\nTest etmek istediğiniz e-posta metnini girin (veya 'q' ile çıkın): \n")
        
        if email_input.lower() == 'q':
            break
        
        if not email_input.strip(): 
            print("Lütfen boş olmayan veya anlamlı kelimeler içeren bir metin girin.")
            continue

        result_label, result_prob = predict_email_phishing(email_input)
        print(f"\nTahmin Sonucu: {result_label} (Olasılık: {result_prob:.4f})")

    print("\nProgramdan çıkılıyor.")
