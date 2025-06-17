# ai_phishing_detector/data_processor.py
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import os

# NLTK indirmelerinin kontrolü (sanal ortamda zaten indirilmiş olmalı)
# try:
#     stopwords.words('english')
# except LookupError:
#     nltk.download('stopwords')
# try:
#     word_tokenize("test")
# except LookupError:
#     nltk.download('punkt')

def clean_text(text):
    """
    Metni temizler: HTML etiketlerini, özel karakterleri kaldırır, küçük harfe çevirir
    ve durak kelimeleri çıkarır.
    """
    if not isinstance(text, str):
        return "" # Metin değilse boş döndür

    # HTML etiketlerini kaldır
    text = re.sub(r'<.*?>', '', text)
    # URL'leri kaldır (basit bir regex ile)
    text = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', text)
    # Sayıları ve noktalama işaretlerini kaldır
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    # Küçük harfe çevir
    text = text.lower()
    # Tokenize et ve durak kelimeleri kaldır
    words = word_tokenize(text)
    # İngilizce durak kelimeler listesi
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in words if word not in stop_words]
    return ' '.join(filtered_words)

def load_and_preprocess_all_csv_in_folder(data_folder, text_col, label_col):
    """
    Belirtilen klasördeki tüm CSV dosyalarını yükler, birleştirir ve ön işleme yapar.
    """
    all_dfs = []
    
    if not os.path.exists(data_folder):
        print(f"Hata: Klasör bulunamadı: {data_folder}. Lütfen yolunu kontrol edin.")
        return None

    print(f"'{data_folder}' klasöründeki tüm CSV dosyaları taranıyor ve okunuyor...")
    for filename in os.listdir(data_folder):
        # Yalnızca doğrudan klasördeki CSV dosyalarını işle, alt klasörlere girme
        if filename.endswith(".csv") and os.path.isfile(os.path.join(data_folder, filename)):
            file_path = os.path.join(data_folder, filename)
            try:
                df = pd.read_csv(file_path)
                # Gerekli sütunların varlığını kontrol et
                if text_col not in df.columns or label_col not in df.columns:
                    print(f"Uyarı: '{filename}' dosyasında '{text_col}' veya '{label_col}' sütunları bulunamadı. Bu dosya atlanıyor.")
                    continue
                
                # Etiket sütunundaki değerleri standartlaştır (phishing/legitimate)
                df[label_col] = df[label_col].astype(str).str.lower().replace({
                    'spam': 'phishing',
                    'ham': 'legitimate',
                    '1': 'phishing', # Eğer etiketler 1 ve 0 ise
                    '0': 'legitimate',
                    'phishing': 'phishing', 
                    'legitimate': 'legitimate'
                })
                
                # Sadece 'phishing' ve 'legitimate' etiketli satırları al (diğerlerini atla)
                df = df[df[label_col].isin(['phishing', 'legitimate'])]

                # Metni temizle
                df['cleaned_text'] = df[text_col].apply(clean_text)
                
                # Sadece temizlenmiş metin ve etiket sütunlarını al
                all_dfs.append(df[['cleaned_text', label_col]].rename(columns={label_col: 'label'}))
                print(f"'{filename}' dosyası yüklendi ve {len(df)} satır işlendi.")

            except Exception as e:
                print(f"Dosya okunurken veya işlenirken hata oluştu {file_path}: {e}")
                continue
    
    if not all_dfs:
        print(f"Hata: Belirtilen klasörde ('{data_folder}') geçerli CSV dosyası bulunamadı veya belirtilen sütun adları yanlış. Klasör boş olabilir.")
        return None
        
    return pd.concat(all_dfs, ignore_index=True)


if __name__ == "__main__":
    # CSV dosyalarınızın bulunduğu tam klasör yolu:
    data_folder_path = '/home/zuhre/ai_phishing_detector/data/25432108'

    # Sütun adları (daha önce tespit ettiğimiz):
    email_text_column_name = 'body'
    email_label_column_name = 'label'

    # Veri kümelerini yükle ve ön işleme yap
    combined_df = load_and_preprocess_all_csv_in_folder(
        data_folder_path, 
        email_text_column_name, 
        email_label_column_name
    )
    
    if combined_df is not None and not combined_df.empty:
        print("\n--- Birleştirilmiş ve İşlenmiş Veri Seti Özeti ---")
        print(f"Toplam işlenmiş e-posta sayısı: {len(combined_df)}")
        print("Etiket Dağılımı:")
        print(combined_df['label'].value_counts())

        # İşlenmiş verileri bir CSV dosyasına kaydetmek iyi bir uygulamadır.
        # Bu dosyayı 'data' klasörüne kaydediyoruz, doğrudan '25432108' içine değil.
        output_file_path = os.path.join('/home/zuhre/ai_phishing_detector/data', 'preprocessed_combined_emails.csv')
        combined_df.to_csv(output_file_path, index=False)
        print(f"\nİşlenmiş veriler '{output_file_path}' konumuna kaydedildi.")
    else:
        print("\nHiçbir e-posta verisi yüklenemedi veya işlenemedi. Sütun adları yanlış olabilir veya klasörde CSV dosyası bulunmuyor olabilir.")

    print("\nVeri ön işleme adımı tamamlandı!")
    print("İşlenmiş verileri daha sonra model eğitimi için kullanacaksınız.")
