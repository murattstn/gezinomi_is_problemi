
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

####################################################
################# Değişkenler ######################
"""
SaleId: Satış id
SaleDate: Satış Tarihi
CheckInDate: Müşterininotelegirişitarihi
Price: Satış için ödenen fiyat
ConceptName: Otelkonseptbilgisi
SaleCityName: Otelin bulunduğu şehir bilgisi
CInDay: Müşterinin otele giriş günü
SaleCheckInDayDiff: Check in ile giriş tarihi gün farkı
Season: Otele giriş tarihindeki sezon bilgis
"""
####################################################
## Görev 1: Aşağıdaki Soruları Yanıtlayınız ##
# Soru1 : miuul_gezinomi.xlsx dosyasını okutunuz ve veri seti ile ilgili genel bilgileri gösteriniz..
pd.set_option('display.max_columns', None)
pd.set_option("display.float_format", "{:.2f}".format)
df = pd.read_excel("miuul_gezinomi.xlsx")
df.head()
df.info()
df.describe()
df.isnull().sum()

# Soru2:Kaçunique şehirvardır? Frekanslarınedir?
df["SaleCityName"].unique()
df["SaleCityName"].value_counts()

# Soru3:Kaç unique Concept vardır?
df["ConceptName"].value_counts()

# Soru5:Şehirlere göre satışlardan toplam ne kadar kazanılmış?
df.groupby("SaleCityName").agg({"Price":"sum"})

# Soru6:Concept türlerine göre ne kadar kazanılmış?
df.groupby("ConceptName").agg({"Price" : "sum"})

# Soru7:Şehirlere göre PRICE ortalamaları nedir?
df.groupby("SaleCityName").agg({"Price" : "mean"})

# Soru8:Conceptlere göre PRICE ortalamaları nedir?
df.groupby("ConceptName").agg({"Price" : "mean"})

# Soru9:Şehir-Concept kırılımında PRICE ortalamaları nedir ?
df.groupby(["SaleCityName", "ConceptName"]).agg({"Price" : "mean"})

# Görev 2: SaleCheckInDayDiff değişkenini kategorik bir değişkene çeviriniz.

# SaleCheckInDayDiff değişkeni müşterinin CheckIn tarihinden ne kadar önce satin alımını tamamladığını gösterir.
# Aralıkları ikna edici şekilde oluşturunuz. Örneğin: ‘0_7’, ‘7_30', ‘30_90', ‘90_max’ aralıklarını kullanabilirsiniz.
# Bu aralıklar için "Last Minuters", "Potential Planners", "Planners", "Early Bookers“ isimlerini kullanabilirsiniz

bins = [df["SaleCheckInDayDiff"].min()-1, 7, 30, 90, df["SaleCheckInDayDiff"].max()]
labels = ["Last Minuters", "Potential Planners", "Planners", "Early Bookers"]
df["EB_Score"] = pd.cut(df["SaleCheckInDayDiff"], bins, labels=labels)

# Bu çalışmada çeyrekliklere göre bölmenin daha anlamlı sonuçlar çıkaracağını
# düşünerek yukarıda verilen listeye göre değil çeyrekliklere bölüyoruz
df["EB_Score"] = pd.qcut(df["SaleCheckInDayDiff"], q= 4, labels=labels)
df.head()

# Görev 3:  Şehir-Concept-EB Score, Şehir-Concept-Sezon,Şehir-Concept-CInDay
# kırılımında ortalama ödenen ücret ve yapılan işlem sayısı cinsinden inceleyiniz ?
df.groupby(["SaleCityName", "ConceptName", "EB_Score"]).agg({"Price" : ["mean", "count"]})
df.groupby(["SaleCityName", "ConceptName", "CInDay"]).agg({"Price" : ["mean", "count"]})
df.groupby(["SaleCityName", "ConceptName", "Seasons"]).agg({"Price" : ["mean", "count"]})

# Görev 4:  City-Concept-Season kırılımının çıktısını PRICE'a göre sıralayınız
agg_df = df.groupby(["SaleCityName", "ConceptName", "Seasons"]).agg({"Price" : "mean"}).sort_values("Price",ascending=False)

# Görev 5: 4. görev çıktısında yer alan PRICE dışındaki tüm değişkenler index isimleridir. Bu isimleri değişken isimlerine çeviriniz.

agg_df.reset_index(inplace=True)
agg_df.head()

# Görev 6: Yeni seviye tabanlı satışları tanımlayınız(persona) ve veri setine değişken olarak ekleyiniz.
# Yeni eklenecek değişkenin adı: sales_level_based
# Önceki soruda elde edeceğiniz çıktıdaki gözlemleri bir araya getirerek sales_level_based değişkenini oluşturmanız gerekmektedir.

agg_df["sales_level_based"] = agg_df[["SaleCityName", "ConceptName", "Seasons"]].apply(lambda x: "_".join(x).upper(),axis=1)
agg_df["sales_level_based"].str.replace("İ","I", regex=False)
agg_df.head()

#Görev 7:  Yeni müşterileri (personaları) segmentlere ayırınız.
# Yeni personaları(sales_level_based) PRICE’a göre 4 segmente ayırınız(A,B,C,D) ve SEGMENT isimlendirmesi yapınız.
# Segmentleri betimleyiniz (Segmentlere göre group by yapıp price için mean, max, sum’larını alınız)

agg_df["SEGMENT"] = pd.qcut(agg_df["Price"], q=4, labels=["A","B","C","D"])
agg_df.head()

agg_df.groupby("SEGMENT", observed=True).agg({"Price" : ["mean", "max", "sum"]})

#Görev 8:  Yeni gelen müşterileri sınıflandırıp, ne kadar gelir getirebileceklerini  tahmin ediniz.
# Antalya’da herşey dahil ve yüksek sezonda tatil yapmak isteyen bir kişinin ortalama ne kadar gelir kazandırması beklenir?
# Girne’de yarım pansiyon bir otele düşük sezonda giden bir tatilci hangi segmentte yer alacaktır

new_users = ["GIRNE_YARIM PANSIYON_LOW", "ANTALYA_HERŞEY DAHIL_HIGH", "GIRNE_YARIM PANSIYON_HIGH"]
for user in new_users:
    print(agg_df[agg_df["sales_level_based"] == user])


