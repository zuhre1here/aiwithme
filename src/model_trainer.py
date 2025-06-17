import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_recall_fscore_support
import joblib # Modeli ve vektörizerı kaydetmek için
import os

# 1. Veri Yükleme
# Ön işlenmiş verilerinizin bulunduğu yol
data_path = os.path.join(os.path.dirname(__file__), 'data', 'preprocessed_combined_emails.csv')

try:
    df = pd.read_csv(data_path)
    print(f"Veri başarıyla yüklendi. Toplam satır: {len(df)}")
    print("Veri başlığı:")
    print(df.head())
    print("\nEtiket dağılımı:")
    print(df['label'].value_counts())

except FileNotFoundError:
    print(f"Hata: {data_path} dosyası bulunamadı. Lütfen veri işleme adımını tamamladığınızdan emin olun.")
    exit()
except Exception as e:
    print(f"Veri yüklenirken bir hata oluştu: {e}")
    exit()

# 'cleaned_text' sütununda boş veya NaN değerler varsa dolduralım
df['cleaned_text'] = df['cleaned_text'].fillna('')


# 2. Veri Hazırlığı ve Etiketleme
# Etiketleri sayısal hale dönüştürelim: 'phishing' -> 1, 'legitimate' -> 0
label_map = {'legitimate': 0, 'phishing': 1}
df['labels'] = df['label'].map(label_map)

# Eğitim ve test setlerine ayırma
# %80 eğitim, %20 test verisi
X_train, X_test, y_train, y_test = train_test_split(
    df['cleaned_text'],
    df['labels'],
    test_size=0.2,
    random_state=42,
    stratify=df['labels'] # Etiket dağılımını korur
)

print(f"\nEğitim veri boyutu: {len(X_train)}")
print(f"Test veri boyutu: {len(X_test)}")

# 3. Özellik Çıkarma (TF-IDF)
# TF-IDF vektörizerı oluşturma
# min_df: minimum belge sıklığı (çok nadir kelimeleri atlar)
# max_df: maksimum belge sıklığı (çok sık geçen kelimeleri atlar)
# ngram_range: kelime gruplarını (örn: "yapay zeka") dikkate alır
vectorizer = TfidfVectorizer(min_df=5, max_df=0.8, ngram_range=(1, 2))

# Eğitim verileri üzerinde TF-IDF vektörizerını eğit ve uygula
X_train_tfidf = vectorizer.fit_transform(X_train)

# Test verileri üzerinde TF-IDF vektörizerını uygula (eğitme!)
X_test_tfidf = vectorizer.transform(X_test)

print(f"\nTF-IDF vektör boyutu (özellik sayısı): {X_train_tfidf.shape[1]}")

# 4. Modeli Seçme ve Eğitme (Lojistik Regresyon)
# Lojistik Regresyon modelini oluşturma
# max_iter: modelin yakınsaması için maksimum iterasyon sayısı
model = LogisticRegression(max_iter=1000, random_state=42, n_jobs=-1) # n_jobs=-1 tüm CPU çekirdeklerini kullanır

print("\nModel eğitimi başlıyor...")
model.fit(X_train_tfidf, y_train)

print("\nModel değerlendirmesi başlıyor...")
y_pred = model.predict(X_test_tfidf)

# 5. Metrikleri Hesaplama
precision, recall, f1, _ = precision_recall_fscore_support(y_test, y_pred, average='binary', zero_division=0)
acc = accuracy_score(y_test, y_pred)

print(f"\nDoğruluk (Accuracy): {acc:.4f}")
print(f"Kesinlik (Precision): {precision:.4f}")
print(f"Duyarlılık (Recall): {recall:.4f}")
print(f"F1 Skoru: {f1:.4f}")

# 6. Eğitilmiş Model ve Vektörizerı Kaydetme
model_save_path = os.path.join(os.path.dirname(__file__), 'phishing_detection_simple_model.joblib')
vectorizer_save_path = os.path.join(os.path.dirname(__file__), 'tfidf_vectorizer.joblib')

joblib.dump(model, model_save_path)
joblib.dump(vectorizer, vectorizer_save_path)

print(f"\nEğitilmiş model '{model_save_path}' konumuna kaydedildi.")
print(f"TF-IDF vektörizerı '{vectorizer_save_path}' konumuna kaydedildi.")

print("\nBasit model eğitim adımı tamamlandı!")
print("Eğitilmiş modelinizi ve vektörizerınızı artık kullanıma hazırsınız.")
