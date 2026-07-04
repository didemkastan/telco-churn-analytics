# telco-churn-analytics

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/didemkastan/telco-churn-analytics/blob/main/Telco_Churn_Analysis.ipynb)



This project analyzes customer churn using the open IBM Telco Customer Churn dataset with 7,043 customer records.

The goal is to understand which customer groups have higher churn risk and to compare two baseline models for churn prediction.



## Project Overview

This repository demonstrates an end-to-end customer churn analytics workflow using the IBM Telco Customer Churn dataset. The focus is not only on predictive performance but also on producing business-oriented insights that can support customer retention strategies.

## Business Problem

Customer churn is one of the most significant challenges for telecommunication providers. Understanding the drivers of churn helps organizations prioritize retention efforts and make data-driven decisions.

## Business Insights

The analysis indicates that retention initiatives should primarily focus on:

* Month-to-month subscribers
* Customers with low tenure
* Customers using electronic check payments

These findings may help optimize retention campaigns by focusing on higher-risk customer segments.

## Skills Demonstrated

* Data Cleaning
* Exploratory Data Analysis
* Logistic Regression
* Gradient Boosting
* ROC/AUC Evaluation
* Business Interpretation
* Data Visualization

## Analysis Scope

This project includes:

* Data cleaning for `TotalCharges` and churn labels
* Exploratory analysis of contract type, tenure and internet service
* Logistic regression for interpretable churn drivers
* Odds ratio analysis for risk-increasing and risk-reducing factors
* Logistic Regression vs. Gradient Boosting model comparison
* ROC/AUC evaluation on a held-out test set

## Key Findings

|Factor|Result|Interpretation|
|-|-:|-|
|Two-year contract|Odds ratio: 0.26|Lower churn risk compared with month-to-month contracts|
|Tenure|Odds ratio: 0.24|Customers become more stable as tenure increases|
|Electronic check payment|Odds ratio: 1.35|Higher-risk payment segment|
|Online security add-on|Odds ratio: 0.66|Add-on service usage may reduce churn risk|

**Model performance:** Logistic Regression and Gradient Boosting produced very similar results on the held-out test set, with both models reaching a **0.847** test AUC. Since the simpler model achieved the same level of performance, Logistic Regression can be used as the main model for interpretation.

## Outputs

![EDA overview](outputs/eda\_overview.png)

![ROC curves](outputs/roc\_curves.png)

## Reproduce

You can run the notebook in Colab by clicking the badge above. The notebook includes both analyst-level and executive-level commentary.

To run locally:

```bash
pip install -r requirements.txt
python run\_analysis.py
```

Dataset: [IBM Telco Customer Churn](https://github.com/IBM/telco-customer-churn-on-icp4d)

## Project Structure

```text
telco-churn-analytics/
├── Telco\\\_Churn\\\_Analysis.ipynb
├── run\\\\\\\_analysis.py
├── data/
│   └── Telco-Customer-Churn.csv
├── outputs/
│   ├── eda\\\_overview.png
│   ├── roc\\\_curves.png
│   ├── odds\\\_ratios.csv
│   └── model\\\_comparison.csv
├── README.md
├── README.tr.md
├── requirements.txt
└── LICENSE
```

## Notes

This is not a production churn system. It is a compact churn analysis project that shows how customer loss can be explored, modeled and interpreted with a reproducible Python workflow.

In a real telecom scenario, the analysis could be improved with additional operational data such as complaint records, fault history, billing disputes, region, campaign history and customer lifetime value.

## Possible Improvements

* Early-tenure churn analysis
* Risk segmentation
* Revenue risk / ARPU analysis
* Campaign threshold optimization
* Uplift modeling for retention targeting

## About the Author

Didem Kaştan
[LinkedIn](https://www.linkedin.com/in/didemkastan)

Principal Specialist | Business Analysis

MSc Measurement \& Data Analytics

Telecom Operations • Data Analytics • Python • SQL • Machine Learning



## License

MIT

