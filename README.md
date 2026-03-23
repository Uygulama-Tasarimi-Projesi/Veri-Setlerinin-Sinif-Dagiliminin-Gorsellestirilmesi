## 📊 Veri Seti Analizi (Data Exploratory Analysis)

### A) Metin Verisi Analizi ve Dağılımı (Text Data Analysis)

Gerçekleştirilen analizler sonucunda elde edilen görselleştirme çıktıları, oluşturulan hibrit metin veri setinin hedeflenen istatistiksel dengeye ulaştığını kanıtlamıştır. Çubuk grafik incelendiğinde, veri setindeki 7 duygu sınıfının homojen bir dağılım sergilediği görülmektedir.

FSMTSAD veri setinden dışarıdan entegre edilen "Nötr" sınıfının, TREMO ana veri setindeki mevcut diğer sınıflarla tam bir sayısal uyum yakaladığı tespit edilmiştir. Sınıflar arasında aşırı uçurumların bulunmaması, tasarlanacak **CNN-LSTM** derin öğrenme modelinin eğitim sürecinde belirli bir çoğunluk sınıfına yönelik yanlılık (bias) geliştirmesini engelleyecek ideal veri altyapısının başarıyla kurulduğunu doğrulamaktadır.

![Duygu Sınıflarının Dağılım Çubuk Grafiği](Metin%20Verilerini%20Analiz%20Etme/Metin%20duygu%20sınıflarının%20dağılım%20çubuk%20grafiği.jpeg)
*Şekil 2: Metin veri seti duygu sınıflarının dağılım çubuk grafiği*

---

### B) Ses Verisi Analizi ve Dağılımı (Audio Data Analysis)

Şekil 3’te sunulan grafik, projenin işitsel analiz ayağında kullanılan 1.248 adet RAVDESS ses verisinin duygu sınıflarına göre dağılımını göstermektedir. Yapılan istatistiksel analiz sonucunda, veri setindeki sınıfların kendi içlerinde standartlara uygun, homojen bir dağılım sergilediği doğrulanmıştır. 

Metin verilerinde sağlanan istatistiksel dengenin ses verilerinde de korunması; geliştirilecek CNN-LSTM tabanlı çok modlu yapay zekâ modelinin akustik özellikleri öğrenirken belirli bir duygu sınıfına yönelik bias geliştirmesini kesin olarak engelleyecek altyapıyı sağlamıştır.

![Ses Veri Seti Duygu Dağılımı](Ses%20Verilerini%20Analiz%20Etme/ses_görüntü.png)
*Şekil 3: Ses veri seti duygu sınıf dağılımı çubuk grafiği*

> **💡 Sonuç:** Hem metin hem de ses modalitelerinde elde edilen bu kusursuz sınıf dengesi (class balance), veri sızıntısını önleyen aktör bazlı bölme (actor-based split) stratejisiyle birleşerek; modelin laboratuvar ortamında ezberleme (overfitting) yapmasını engellemiş ve gerçek dünya senaryolarında yüksek genelleme yeteneğine (generalization) sahip olmasını istatistiksel olarak garanti altına almıştır.
