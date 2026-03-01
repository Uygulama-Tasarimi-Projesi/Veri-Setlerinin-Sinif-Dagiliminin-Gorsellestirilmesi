## 📊 Veri Seti Analizi (Data Exploratory Analysis)

### A) Metin Verilerini Analiz Etme (Text Data Analysis)

Gerçekleştirilen analizler sonucunda elde edilen görselleştirme çıktıları, oluşturulan hibrit metin veri setinin hedeflenen istatistiksel dengeye ulaştığını kanıtlamıştır. Çubuk grafik ve terminal çıktıları incelendiğinde duyguların homojen bir dağılım sergilediği görülmektedir.

FSMTSAD veri setinden dışarıdan entegre edilen "Nötr" sınıfının, TREMO ana veri setindeki diğer yoğun sınıflarla tam bir sayısal uyum yakaladığı tespit edilmiştir. Sınıflar arasında aşırı uçurumların bulunmaması, tasarlanacak **CNN-LSTM** derin öğrenme modelinin eğitim sürecinde belirli bir çoğunluk sınıfına yönelik yanlılık (bias) geliştirmesini engelleyecek ideal veri altyapısının başarıyla kurulduğunu doğrulamaktadır.

![Duygu Sınıflarının Dağılım Çubuk Grafiği](Metin%20Verilerini%20Analiz%20Etme/Metin%20duygu%20sınıflarının%20dağılım%20çubuk%20grafiği.jpeg)
*Şekil 2: Duygu sınıflarının dağılım çubuk grafiği*

---

### B) Ses Verisi İçin Sinyal İşleme Analizi (Audio Signal Processing)

Projede kullanılacak derin öğrenme modelinin (CNN) ses verilerini nasıl ayırt edeceğini teknik olarak doğrulamak amacıyla, RAVDESS veri setinden seçilen "Öfkeli" ve "Üzgün" duygu sınıflarına ait örnek kayıtlar üzerinde `librosa` kütüphanesi ile sinyal analizi gerçekleştirilmiştir.

* **Dalga Formu (Waveform) Analizi:** Çizdirilen zamansal dalga grafikleri incelendiğinde, öfkeli duygu durumuna ait ses sinyalinin genliğinin çok daha yüksek, ani ve enerjik dalgalanmalara sahip olduğu görülmektedir. Buna karşın üzgün ses sinyali belirgin ölçüde daha düşük genlikli, düşük enerjili ve daha yavaş salınımlı bir yapı sergilemektedir.

![Ses Dalga Formu Zamansal Dalga Grafiği](Ses%20Verisi%20İçin%20Sinyal%20İşleme%20Analizi/Öfkeli%20ve%20üzgün%20duygularının%20Ses%20Dalga%20Formu%20zamansal%20dalga%20grafiği.jpeg)
*Şekil 3: Öfkeli ve üzgün duygularının Ses Dalga Formu zamansal dalga grafiği*

* **Mel-Spektrogram Analizi:** İnsan işitme sistemine uygun olarak ölçeklendirilen Mel-Spektrogram haritaları karşılaştırıldığında ise akustik farklar daha boyutlu bir şekilde ortaya çıkmaktadır. Öfkeli seste enerjinin (parlak/sıcak renklerin) yüksek frekans bantlarına (4096 Hz ve üzeri) kadar yoğun bir şekilde yayıldığı tespit edilirken; üzgün seste enerjinin daha çok düşük frekanslarda toplandığı ve genel matriste düşük bir akustik şiddetin hakim olduğu saptanmıştır.

![Mel-Spektrogram Analizi](Ses%20Verisi%20İçin%20Sinyal%20İşleme%20Analizi/Öfkeli%20ve%20üzgün%20duygularının%20Mel-Spektrogram%20Analizi.jpeg)
*Şekil 4: Öfkeli ve üzgün duygularının Mel-Spektrogram Analizi*

> **💡 Sonuç:** Bu görsel analizler, farklı duygu durumlarının birbirinden tamamen farklı iki boyutlu akustik örüntülere sahip olduğunu kanıtlamaktadır. Geliştirilecek çok modlu sistemin ses işleme katmanında yer alacak olan Evrişimsel Sinir Ağı (CNN) modelinin, bu Mel-Spektrogram haritalarını birer görüntü matrisi olarak kabul edip duygu sınıflarını yüksek doğrulukla ayırt edebileceği istatistiksel ve görsel olarak doğrulanmıştır.
