import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# DOSYA YOLU
ravdess_path = "C:\\Users\\asus\\Desktop\\3_sinif_bahar\\Uygulama_tasarim\\7.hafta\\archive_ravdess"

# RAVDESS dosya isimlendirme standartlarına göre duygu kodları
emotion_dict = {
    '01': 'Neutral (Nötr)',
    '02': 'Calm (Sakin)',
    '03': 'Happy (Mutlu)',
    '04': 'Sad (Üzgün)',
    '05': 'Angry (Kızgın)',
    '06': 'Fearful (Korkulu)',
    '07': 'Disgust (İğrenme)',
    '08': 'Surprised (Şaşkın)'
}

emotions_list = []

# KLASÖRLERİ VE DOSYALARI OKUMA
if not os.path.exists(ravdess_path):
    print(f"Klasör bulunamadı: {ravdess_path}")
else:
    for actor_folder in os.listdir(ravdess_path):
        actor_path = os.path.join(ravdess_path, actor_folder)
        
        # Sadece klasörleri işle
        if os.path.isdir(actor_path):
            for file in os.listdir(actor_path):
                if file.endswith(".wav"):
                    # Dosya ismini '-' işaretine göre böl ve 3. elemanı (duygu kodunu) al
                    part = file.split('-')
                    if len(part) >= 3:
                        emotion_code = part[2]
                        # Kodu sözlükten bul, listeye ekle
                        emotions_list.append(emotion_dict.get(emotion_code, 'Bilinmeyen'))

    # VERİYİ DATAFRAME'E ÇEVİR VE SAY
    df_audio = pd.DataFrame(emotions_list, columns=['Emotion'])
    duygu_sayilari = df_audio['Emotion'].value_counts()

    print(f"Toplam İşlenen Ses Dosyası: {len(df_audio)}")
    print("\n--- SES DUYGU DAĞILIMI ---")
    print(duygu_sayilari)

    # GÖRSELLEŞTİRME (BAR PLOT)
    plt.figure(figsize=(10,6))
    sns.barplot(x=duygu_sayilari.values, y=duygu_sayilari.index, palette="viridis")
    plt.title("RAVDESS Ses Veri Seti Duygu Sınıf Dağılımı")
    plt.xlabel("Örneklem Sayısı")
    plt.ylabel("Duygu Sınıfları")
    plt.tight_layout()
    plt.show()
