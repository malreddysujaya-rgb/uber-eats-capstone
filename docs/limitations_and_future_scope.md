# Uber Eats Capstone – Limitations and Future Scope

## 1. Introduction

This document describes the limitations of the Uber Eats Capstone Project and identifies opportunities for future improvements.

The project applies data analytics, machine learning, natural language processing, and time-series forecasting to understand food delivery operations.

## 2. Project Limitations

### 2.1 Synthetic Dataset

The project uses synthetically generated datasets instead of actual Uber Eats operational data.

**Limitation:**
- The generated records may not represent real customer behavior.
- Business patterns may differ from actual food delivery operations.
- Model performance on synthetic data may not generalize to real-world data.

### 2.2 Customer and Restaurant Segmentation

K-Means and DBSCAN were used for clustering.

**Limitations:**
- Cluster assignments depend on selected features and parameters.
- Different parameter choices may produce different groups.
- Cluster IDs do not represent fixed business categories.
- DBSCAN noise points require further investigation.

### 2.3 Sentiment Analysis

TF-IDF with Naive Bayes and VADER were used for sentiment analysis.

**Limitations:**
- Synthetic review text may contain predictable patterns.
- Synthetic sentiment labels may make classification easier than real-world reviews.
- Sarcasm, spelling variations, and complex language may affect predictions.
- The perfect Naive Bayes evaluation score does not guarantee real-world accuracy.

### 2.4 Delivery Time Prediction

Regression models were used to predict delivery time.

**Limitations:**
- Prediction quality depends on the available features and data quality.
- Synthetic delivery records may not capture all real-world delivery conditions.
- Traffic, weather, restaurant preparation, and other factors may change over time.
- Model performance requires validation using actual operational data.

### 2.5 Demand Forecasting

ARIMA and Prophet were used to forecast hourly order demand.

**Limitations:**
- Forecast accuracy depends on the historical time-series patterns.
- Synthetic demand may not represent actual seasonal or business trends.
- Sudden changes in demand may be difficult to predict.
- Model performance may vary across different forecasting periods.

## 3. Future Scope

### 3.1 Real-World Data Integration

Use actual operational data to improve the reliability and practical relevance of the analysis.

### 3.2 Advanced Customer Segmentation

Explore additional clustering algorithms and customer behavior features to identify more meaningful customer groups.

### 3.3 Advanced Sentiment Analysis

Experiment with advanced NLP models such as BERT and other transformer-based approaches to improve understanding of customer feedback.

### 3.4 Improved Delivery Time Prediction

Include real-time traffic, weather, restaurant preparation, and delivery partner location information to improve prediction quality.

### 3.5 Advanced Demand Forecasting

Explore additional forecasting approaches and incorporate holidays, promotions, seasonal trends, and external factors.

### 3.6 Dashboard Development

Develop an interactive dashboard using Power BI, Tableau, or Streamlit to help business teams monitor KPIs and model outputs.

### 3.7 Model Deployment

Deploy trained models through APIs and integrate them into an operational application for practical use.

## 4. Conclusion

The Uber Eats Capstone Project provides a foundation for applying data analytics and machine learning to food delivery operations.

Although the project uses synthetic datasets, it demonstrates an end-to-end analytical workflow. Future improvements using real-world data, advanced models, interactive dashboards, and deployment can increase its business value.