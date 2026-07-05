# telco-churn-analytics

[![Open In Colab](https://colab.research.google.com/github/didemkastan/telco-churn-analytics/blob/main/Telco_Churn_Analysis.ipynb#scrollTo=cell-10)



Bu projede açık kaynak IBM Telco Customer Churn veri seti kullanılarak müşteri kaybı analizi yapılmıştır. Veri setinde 7.043 müşteri kaydı bulunmaktadır.

Amaç, hangi müşteri gruplarında churn riskinin daha yüksek olduğunu görmek ve iki temel modelin tahmin performansını karşılaştırmaktır.



## Proje Özeti

Bu çalışma, IBM Telco Customer Churn veri seti kullanılarak uçtan uca müşteri kaybı analizi gerçekleştirmek amacıyla hazırlanmıştır. Amaç yalnızca model geliştirmek değil, elde edilen bulguları iş kararlarını destekleyecek analitik içgörülere dönüştürmektir.

## İş Problemi

Müşteri kaybı telekom sektörünün en önemli operasyonel problemlerinden biridir. Analiz, müşteri elde tutma stratejilerine katkı sağlayabilecek risk göstergelerini ortaya çıkarmayı hedeflemektedir.

## İş Perspektifi

Analiz sonuçları özellikle aşağıdaki müşteri gruplarına odaklanılmasının faydalı olabileceğini göstermektedir:

* Aylık kontratlı müşteriler
* Abonelik süresi düşük müşteriler
* Electronic Check kullanan müşteriler

## Kazanılan Yetkinlikler

* Veri Temizleme
* Keşifsel Veri Analizi
* Lojistik Regresyon
* Gradient Boosting
* ROC/AUC Analizi
* İş Odaklı Yorumlama
* Veri Görselleştirme

## Analiz Kapsamı

Bu çalışma aşağıdaki adımları içerir:

* `TotalCharges` ve churn etiketi için veri temizliği
* Kontrat tipi, abonelik süresi ve internet hizmeti için keşifsel analiz
* Churn riskini yorumlamak için lojistik regresyon
* Riski artıran ve azaltan faktörler için odds oranı analizi
* Logistic Regression ve Gradient Boosting model karşılaştırması
* Ayrılmış test kümesinde ROC/AUC değerlendirmesi

## Temel Bulgular

|Faktör|Sonuç|Yorum|
|-|-:|-|
|İki yıllık kontrat|Odds oranı: 0.26|Aylık kontrata göre churn riski belirgin şekilde daha düşük|
|Abonelik süresi|Odds oranı: 0.24|Müşteri firmada kaldıkça churn riski azalıyor|
|Electronic check ödeme|Odds oranı: 1.35|Daha yüksek riskli bir ödeme segmenti|
|Online security hizmeti|Odds oranı: 0.66|Ek hizmet kullanımı churn riskini azaltan bir sinyal olabilir|

**Model performansı:** Logistic Regression ve Gradient Boosting ayrılmış test kümesinde birbirine çok yakın sonuçlar üretmiş, iki model de **0.847** test AUC değerine ulaşmıştır. Daha basit model aynı seviyede performans verdiği için Logistic Regression yorumlanabilirlik açısından ana model olarak kullanılabilir.

## Çıktılar

![Keşifsel veri analizi](outputs/eda\_overview.png)



![ROC eğrileri](outputs/roc\_curves.png)



Yeniden Üretme

Colab üzerinden çalıştırmak için yukarıdaki rozete tıklayabilirsiniz. Notebook hem analist hem de yönetici düzeyinde yorumlar içerir.

Lokal ortamda çalıştırmak için:

```bash
pip install -r requirements.txt
python run\_analysis.py
```

Veri seti: [IBM Telco Customer Churn](https://github.com/IBM/telco-customer-churn-on-icp4d)

## Proje Yapısı

```text
telco-churn-analytics/
├── Telco\_Churn\_Analysis.ipynb
├── run_analysis.py
├── data/
│   └── Telco-Customer-Churn.csv
├── outputs/
│   ├── eda_overview.png
│   ├── roc_curves.png
│   ├── odds_ratios.csv
│   └── model_comparison.csv
├── README.md
├── README.tr.md
├── requirements.txt
└── LICENSE
```

## Notlar

Bu çalışma doğrudan üretim ortamında kullanılacak bir churn sistemi değildir. Müşteri kaybını anlamak, riskli segmentleri belirlemek ve churn tahmini için temel bir analiz akışı sunar.

Gerçek bir telekom senaryosunda şikayet kayıtları, arıza geçmişi, fatura itirazları, bölge bilgisi, kampanya geçmişi ve müşteri yaşam boyu değeri gibi ek verilerle analiz genişletilebilir.

## Geliştirme Fikirleri

* İlk dönem churn analizi
* Risk segmentasyonu
* Gelir riski / ARPU analizi
* Kampanya maliyetine göre eşik optimizasyonu
* Uplift modelleme ile kampanya hedefleme

## Geliştirici

Didem Kaştan

[LinkedIn](https://www.linkedin.com/in/didemkastan)

Principal Specialist | Business Analysis

Ölçme ve Veri Analitiği Yüksek Lisans

Telekom Operasyonları • Veri Analitiği • Python • SQL • Makine Öğrenmesi

## Lisans

MIT

