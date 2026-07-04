# telco-churn-analytics

[!\[Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/didemkastan/telco-churn-analytics/blob/main/Telco_Churn_Analysis.ipynb)
!\[Python](https://img.shields.io/badge/Python-3.x-blue)
!\[Pandas](https://img.shields.io/badge/Pandas-Veri%20Analizi-success)
!\[Scikit-Learn](https://img.shields.io/badge/scikit--learn-Makine%20%C3%96%C4%9Frenmesi-orange)
!\[License: MIT](https://img.shields.io/badge/License-MIT-green)

# 

# Telco Customer Churn Analytics📊

IBM Telco Customer Churn veri seti (7.043 müşteri) kullanılarak hazırlanan uçtan uca veri analizi ve temel makine öğrenmesi projesidir.

Bu çalışma yalnızca model başarısını değil, **iş açısından anlamlı içgörüler üretmeyi** hedeflemektedir.

## 

## Neden bu proje?

Müşteri kaybı, telekom sektörünün en önemli iş problemlerinden biridir. Bu proje, ham veriden iş kararlarını destekleyecek analitik çıktılara kadar tekrarlanabilir bir Python analiz süreci sunmaktadır.

## 

## Analiz Kapsamı

* Veri temizleme
* Keşifsel Veri Analizi (EDA)
* Kontrat, abonelik süresi ve internet hizmeti analizi
* Lojistik Regresyon
* Odds Oranı analizi
* Logistic Regression ve Gradient Boosting karşılaştırması
* ROC / AUC değerlendirmesi

## 

## İş Perspektifi

Analiz, özellikle aşağıdaki müşteri gruplarında elde tutma çalışmalarının önceliklendirilmesinin faydalı olabileceğini göstermektedir:

* Aylık kontratlı müşteriler
* Electronic Check kullanan müşteriler
* Abonelik süresi düşük müşteriler

## 

## Temel Bulgular

|Faktör|Sonuç|Yorum|
|-|-:|-|
|İki yıllık kontrat|OR: 0.26|Churn riski belirgin şekilde düşük|
|Abonelik süresi|OR: 0.24|Süre arttıkça churn azalıyor|
|Electronic Check|OR: 1.35|Daha yüksek risk|
|Online Security|OR: 0.66|Riski azaltabilecek bir gösterge|

Her iki model de **0.847 Test AUC** elde etmiş, yorumlanabilirliği nedeniyle Logistic Regression öne çıkmıştır.

## 

## Kazanılan Yetkinlikler

* Veri Temizleme
* Keşifsel Veri Analizi
* Veri Görselleştirme
* Lojistik Regresyon
* Gradient Boosting
* ROC/AUC Analizi
* İş Odaklı Yorumlama

## 

## Gelecek Çalışmalar

* İlk dönem churn analizi
* ARPU ve gelir riski analizi
* Risk segmentasyonu
* Uplift modelleme
* SHAP ile açıklanabilir yapay zekâ

## 

## Geliştirici

**Didem Kaştan**

Principal Specialist | Business Analysis | Telecom Operations

Ölçme ve Veri Analitiği Yüksek Lisans

Python • SQL • Machine Learning • Business Analytics

Veri seti: https://github.com/IBM/telco-customer-churn-on-icp4d

MIT Lisansı.

