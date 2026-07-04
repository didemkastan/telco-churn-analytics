# telco-churn-analytics

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/didemkastan/telco-churn-analytics/blob/main/Telco_Churn_Analysis.ipynb)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-success)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-ML-orange)
![License: MIT](https://img.shields.io/badge/License-MIT-green)

# 📊 Telco Customer Churn Analytics

An end-to-end exploratory data analysis and baseline machine learning project using the IBM Telco Customer Churn dataset (7,043 customers).

Rather than focusing only on model performance, this project emphasizes **business interpretation**, helping identify customer segments with higher churn risk and translating analytical findings into actionable business insights.

## 🎯 Why this project?

Customer churn is one of the most critical business challenges in the telecommunications industry. This project demonstrates a reproducible analytics workflow from raw customer data to business-oriented recommendations using Python.

## 🔍 Analysis Scope

- Data cleaning (`TotalCharges`, churn labels)
- Exploratory Data Analysis (EDA)
- Contract, tenure and internet service analysis
- Logistic Regression
- Odds Ratio interpretation
- Logistic Regression vs Gradient Boosting
- ROC / AUC evaluation

## 💼 Business Insights

The analysis suggests that retention efforts should primarily focus on:
- Month-to-month customers
- Customers paying by Electronic Check
- Customers with low tenure

These findings can support customer retention strategies and data-driven decision making.

## 📊 Key Findings

| Factor | Result | Interpretation |
|---|---:|---|
| Two-year contract | OR: 0.26 | Significantly lower churn risk |
| Tenure | OR: 0.24 | Longer relationships reduce churn |
| Electronic check | OR: 1.35 | Higher-risk payment segment |
| Online security | OR: 0.66 | May reduce churn risk |

Both Logistic Regression and Gradient Boosting achieved **0.847 Test AUC**, making Logistic Regression the preferred model due to its interpretability.

## 🧠 Skills Demonstrated

- Data Cleaning
- Exploratory Data Analysis
- Data Visualization
- Logistic Regression
- Gradient Boosting
- ROC/AUC Evaluation
- Business Interpretation

## 📂 Project Structure

See repository structure and notebook for details.

## 🚀 Future Improvements

- Early-tenure churn analysis
- Revenue risk / ARPU analysis
- Customer segmentation
- Uplift modeling
- Explainable AI (SHAP)

## 👩‍💻 Author

**Didem Kaştan**

Principal Specialist | Business Analysis | Telecom Operations

MSc Measurement & Data Analytics

Python • SQL • Machine Learning • Business Analytics

Dataset: https://github.com/IBM/telco-customer-churn-on-icp4d

Licensed under MIT.
