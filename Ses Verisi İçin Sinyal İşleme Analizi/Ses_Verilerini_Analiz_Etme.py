import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

# --- AYARLAR ---
DOSYA_OFKELI = "03-01-05-01-01-01-01.wav"  # 05 = Öfkeli
DOSYA_UZGUN = "03-01-04-01-01-01-01.wav"   # 04 = Üzgün

# Sesleri Yükle
y_ofkeli, sr_ofkeli = librosa.load(DOSYA_OFKELI, sr=None)
y_uzgun, sr_uzgun = librosa.load(DOSYA_UZGUN, sr=None)

# --- WAVEFORM (ZAMANSAL DALGA) KARŞILAŞTIRMASI ---
plt.figure(figsize=(14, 4))

plt.subplot(1, 2, 1) # 1 satır, 2 sütun, 1. grafik
librosa.display.waveshow(y_ofkeli, sr=sr_ofkeli, color="red", alpha=0.7)
plt.title("Öfkeli (Angry) Ses - Dalga Formu")
plt.xlabel("Zaman (sn)")
plt.ylabel("Genlik")

plt.subplot(1, 2, 2) # 1 satır, 2 sütun, 2. grafik
librosa.display.waveshow(y_uzgun, sr=sr_uzgun, color="blue", alpha=0.7)
plt.title("Üzgün (Sad) Ses - Dalga Formu")
plt.xlabel("Zaman (sn)")
plt.ylabel("Genlik")

plt.tight_layout()
plt.show()

# --- MEL-SPECTROGRAM KARŞILAŞTIRMASI ---
plt.figure(figsize=(14, 4))

# Öfkeli Spektrogram
plt.subplot(1, 2, 1)
S_ofkeli = librosa.feature.melspectrogram(y=y_ofkeli, sr=sr_ofkeli, n_mels=128, fmax=8000)
S_dB_ofkeli = librosa.power_to_db(S_ofkeli, ref=np.max)
librosa.display.specshow(S_dB_ofkeli, x_axis='time', y_axis='mel', sr=sr_ofkeli, fmax=8000)
plt.colorbar(format='%+2.0f dB')
plt.title("Öfkeli Ses - Mel-Spektrogram")

# Üzgün Spektrogram
plt.subplot(1, 2, 2)
S_uzgun = librosa.feature.melspectrogram(y=y_uzgun, sr=sr_uzgun, n_mels=128, fmax=8000)
S_dB_uzgun = librosa.power_to_db(S_uzgun, ref=np.max)
librosa.display.specshow(S_dB_uzgun, x_axis='time', y_axis='mel', sr=sr_uzgun, fmax=8000)
plt.colorbar(format='%+2.0f dB')
plt.title("Üzgün Ses - Mel-Spektrogram")

plt.tight_layout()
plt.show()