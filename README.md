# Gezinomi İş Problemi – Kural Tabanlı Sınıflandırma

Bu repo, Gezinomi firmasına ait müşteri verileri kullanılarak **kural tabanlı segmentasyon** yapılmasını amaçlayan bir iş probleminin Python ile çözümünü içerir.

Projede, müşterilerin demografik ve davranışsal özellikleri birleştirilerek yeni müşteri seviyeleri oluşturulmuş ve bu seviyelere göre segmentasyon yapılmıştır.

---

## İş Problemi

Gezinomi, müşterilerinin satın alma davranışlarını daha iyi analiz edebilmek için
müşteri özelliklerine dayalı bir segmentasyon modeli geliştirmek istemektedir.

Bu kapsamda amaç:
- Müşteri özelliklerini birleştirerek **yeni bir seviye bazlı müşteri tanımı** oluşturmak
- Bu tanımlara göre müşterileri **kural tabanlı segmentlere ayırmak**
- Yeni bir müşterinin hangi segmente ait olacağını tahmin edebilmektir

İş probleminin detaylı tanımı ve yönlendirici sorular **PDF dosyasında** yer almaktadır.

---

## Veri Seti

- `miuul_gezinomi.xlsx`
- Veri seti; şehir, konsept, sezon ve fiyat bilgilerini içermektedir.
- Analiz sürecinde bu değişkenler kullanılarak yeni türetilmiş değişkenler oluşturulmuştur.

---

## Proje İçeriği

- `gezinomi.py`  
  → İş probleminin Python ile çözümünü içeren ana kod dosyası

- `miuul_gezinomi.xlsx`  
  → Kullanılan ham veri seti

- `Gezinomi_Kural_Tabanlı_Sınıflandırma.pdf`  
  → İş probleminin tanımı ve yönlendirici sorular

- `environment.yml`  
  → Projenin çalıştırılması için gerekli Python paketlerini içeren ortam dosyası

---

## Kullanılan Teknolojiler

- Python
- pandas
- numpy

---

## Çalıştırma

1. Conda ortamı oluştur:
   ```bash
   conda env create -f environment.yml

2. Ortamı aktive et:
    conda activate <environment_name>

3. Python dosyasını çalıştır:
    python gezinomi.py
