# Uber Eats Capstone – Business Recommendations

## 1. Introduction

This document presents business insights and recommendations based on the Uber Eats Capstone Project.

The analysis covers customer segmentation, restaurant performance, customer sentiment, delivery time prediction, and hourly demand forecasting.

## 2. Customer Segmentation Insights

Customer segmentation was performed using K-Means and DBSCAN clustering.

The K-Means analysis identified three customer groups.

| Cluster | Customers | Average Orders | Average Order Value | Average Spending |
|---|---:|---:|---:|---:|
| Cluster 0 | 259 | 6.39 | 700.79 | 4,462.77 |
| Cluster 1 | 163 | 11.15 | 759.67 | 8,432.26 |
| Cluster 2 | 78 | 8.28 | 719.70 | 5,925.82 |

### Business Interpretation

- Cluster 0 represents a larger group with comparatively lower order frequency and spending.
- Cluster 1 represents frequent customers with the highest average order value and spending.
- Cluster 2 represents a smaller group with moderate ordering activity and spending.

### Recommendations

1. Provide loyalty rewards and personalized offers to frequent customers.
2. Encourage customers with lower order frequency through targeted promotions.
3. Use personalized recommendations to increase repeat purchases.
4. Monitor customer ordering patterns to identify changes in engagement.

## 3. Restaurant Segmentation Insights

The restaurant segmentation analysis identified three groups.

| Cluster | Restaurants | Average Orders | Average Revenue | Average Delivery Time | Cancellation Rate |
|---|---:|---:|---:|---:|---:|
| Cluster 0 | 25 | 91.60 | 56,305.16 | 54.07 | 8% |
| Cluster 1 | 17 | 76.82 | 46,555.92 | 55.63 | 7% |
| Cluster 2 | 18 | 78.00 | 44,080.53 | 52.24 | 9% |

### Business Interpretation

- Cluster 0 has the highest average order volume and revenue.
- Cluster 1 has the lowest cancellation rate among the three groups.
- Cluster 2 has the shortest average delivery time but the highest cancellation rate.

### Recommendations

1. Study the operational practices of high-revenue restaurants.
2. Identify ways to improve delivery efficiency across restaurant groups.
3. Investigate the reasons for higher cancellations in Cluster 2.
4. Support restaurants with operational improvements and performance monitoring.

## 4. Customer Sentiment Insights

Customer reviews were analyzed using TF-IDF with a Multinomial Naive Bayes classifier and compared with VADER.

### Model Comparison

| Metric | Naive Bayes | VADER |
|---|---:|---:|
| Accuracy | 1.0000 | 0.6867 |
| Weighted Precision | 1.0000 | 0.7227 |
| Weighted Recall | 1.0000 | 0.6867 |
| Weighted F1-score | 1.0000 | 0.7009 |

### Business Interpretation

- Naive Bayes achieved higher evaluation scores than VADER on the generated review dataset.
- VADER provided a lower-performing baseline for comparison.
- Negative review themes can help identify areas requiring service improvements.

### Recommendations

1. Monitor customer reviews regularly.
2. Investigate recurring complaints.
3. Improve restaurant preparation and delivery coordination where complaints indicate delays.
4. Use sentiment trends to monitor customer satisfaction.

**Note:** The datasets and sentiment labels are synthetic. Perfect Naive Bayes scores should not be interpreted as proof of real-world performance.

## 5. Delivery Time Prediction

Regression models were developed to predict delivery time.

The project compared:

- Baseline Regression
- Random Forest Regression
- Ridge Regression
- Lasso Regression

### Business Recommendations

1. Use delivery-time predictions to support operational planning.
2. Examine important model features to identify potential delivery delays.
3. Improve coordination between restaurants and delivery partners.
4. Compare predicted and actual delivery times to monitor model performance.

The final model-selection decision should be based on the actual MAE, RMSE, and R² results in the regression evaluation report.

## 6. Hourly Demand Forecasting

Hourly order demand was analyzed using time-series techniques.

The project compared:

- Hour-of-day baseline
- ARIMA
- Prophet

### Business Recommendations

1. Use hourly demand patterns to support delivery partner scheduling.
2. Plan operational capacity around periods of higher demand.
3. Coordinate restaurant preparation capacity with expected order volumes.
4. Compare forecasted and actual demand to improve future planning.

The final forecasting model should be selected based on the actual MAE, RMSE, and MAPE evaluation results.

## 7. Overall Business Recommendations

Based on the combined project analysis:

1. **Customer Retention:** Introduce loyalty programs and personalized promotions.
2. **Restaurant Performance:** Monitor restaurant revenue, order volume, delivery time, and cancellations.
3. **Customer Experience:** Analyze negative feedback and address recurring complaints.
4. **Delivery Operations:** Use delivery-time predictions to support better operational planning.
5. **Demand Planning:** Use hourly forecasts to plan delivery partner availability.
6. **Continuous Monitoring:** Track KPIs and model performance regularly.

## 8. Conclusion

The project demonstrates how customer segmentation, sentiment analysis, regression, and demand forecasting can support food delivery business decisions.

The recommendations provide opportunities to improve customer engagement, restaurant operations, delivery efficiency, and demand planning.