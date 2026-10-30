# Uber Eats Capstone – Project Methodology

## 1. Introduction

This document explains the methodology followed during the Uber Eats Capstone Project. The project uses Python-based data analysis, machine learning, NLP, and time-series forecasting techniques.

## 2. Data Generation and Preparation

### 2.1 Data Generation

Seven synthetic datasets were generated:

- Customers
- Restaurants
- Orders
- Deliveries
- Drivers
- Reviews
- Payments

### 2.2 Data Inspection and Cleaning

The datasets were inspected to understand their structure and data types.

The preparation process included:

- Checking dataset dimensions.
- Inspecting column names and data types.
- Identifying missing values.
- Checking duplicate records.
- Converting columns into appropriate data types.
- Preparing datasets for analysis.

### 2.3 Feature Engineering

Relevant features were created from customer, restaurant, order, and delivery information to support analytical tasks and machine learning models.

## 3. Customer and Restaurant Segmentation

### Objective

Identify groups of customers and restaurants with similar characteristics.

### Techniques Used

**K-Means Clustering**

- Applied K-Means clustering to customer and restaurant features.
- Used the Elbow Method to examine suitable cluster counts.
- Used Silhouette Scores to evaluate cluster separation.
- Used PCA to visualize clusters.

**DBSCAN Clustering**

- Applied DBSCAN to identify dense groups.
- Examined noise points and potential outliers.

### Evaluation

Cluster profiles were created using average values and group sizes to understand the characteristics of each segment.

## 4. Customer Sentiment Analysis

### Objective

Understand customer opinions from review text.

### Methodology

1. Loaded and inspected customer reviews.
2. Cleaned and preprocessed review text.
3. Converted text into numerical features using TF-IDF.
4. Trained a Multinomial Naive Bayes classifier.
5. Evaluated predictions using classification metrics.
6. Compared the model with VADER sentiment analysis.
7. Examined negative reviews to identify common complaint themes.

### Evaluation Metrics

- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix

## 5. Delivery Time Prediction

### Objective

Predict delivery time using available order and delivery information.

### Methodology

1. Combined relevant order, delivery, and restaurant information.
2. Selected delivery time as the prediction target.
3. Prepared numerical and categorical features.
4. Split the data into training and testing sets.
5. Trained and evaluated regression models.

### Models Used

- Baseline Regression
- Random Forest Regressor
- Ridge Regression
- Lasso Regression

### Evaluation Metrics

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R-squared (R²)

Feature importance and actual-versus-predicted visualizations were used to interpret model results.

## 6. Hourly Demand Forecasting

### Objective

Analyze and forecast hourly order demand.

### Methodology

1. Converted order timestamps into datetime format.
2. Aggregated orders into hourly demand.
3. Identified missing time intervals.
4. Visualized hourly demand patterns.
5. Performed time-series decomposition.
6. Checked stationarity using the Augmented Dickey-Fuller (ADF) test.
7. Applied differencing when required.
8. Divided the data chronologically into training and testing periods.
9. Trained forecasting models.

### Models Used

- ARIMA
- Prophet
- Hour-of-day baseline

### Evaluation Metrics

- MAE
- RMSE
- MAPE

Forecast visualizations were used to compare actual and predicted demand.

## 7. Business Insights and Integration

The outputs from segmentation, sentiment analysis, regression, and forecasting were combined to prepare an overall business view.

The integration included:

- Business KPI summaries.
- Customer sentiment summaries.
- Clustering profiles.
- Regression model comparisons.
- Forecast model comparisons.
- Business insights and recommendations.

## 8. Model and Output Storage

Processed datasets were stored in `data/processed/`.

Trained models were stored in `models/`.

Visualizations were stored in `reports/figures/`.

Evaluation metrics and business insights were stored in `reports/insights/`.

## 9. Conclusion

The methodology combines descriptive analytics, machine learning, NLP, and forecasting to examine different aspects of food delivery operations and support data-driven business decisions.