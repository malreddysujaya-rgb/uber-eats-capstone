# Uber Eats Operational & Customer Intelligence System

## Project Overview

This project develops an end-to-end machine learning and analytics solution for a simulated food-delivery marketplace.

The objective is to analyze customer and restaurant behavior, understand customer feedback, predict delivery performance, and forecast hourly order demand.

The project combines data preprocessing, exploratory analysis, machine learning, natural language processing, and time-series forecasting to generate actionable business insights.

## Business Objectives

- Understand customer ordering and spending behavior.
- Segment customers and restaurants based on performance.
- Analyze customer feedback using sentiment analysis.
- Predict delivery time using regression models.
- Forecast hourly order demand using time-series models.
- Integrate analytical results into business insights and recommendations.

## Dataset

The project uses seven synthetic datasets:

| Dataset | Description |
|---|---|
| customers.csv | Customer information |
| restaurants.csv | Restaurant information |
| orders.csv | Order transaction details |
| deliveries.csv | Delivery information |
| drivers.csv | Delivery partner details |
| reviews.csv | Customer feedback |
| payments.csv | Payment transactions |

The datasets are generated using Python, Pandas, and NumPy. They are synthetic and do not represent actual Uber Eats customer records.

## Technologies

- Python
- Pandas and NumPy
- Matplotlib and Seaborn
- Scikit-learn
- NLTK
- TF-IDF
- Statsmodels
- ARIMA
- Prophet
- Joblib and Pickle
- Jupyter Notebook
- Git and GitHub

## Project Structure

```text
uber-eats-intelligence/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── docs/
│   ├── data_dictionary.csv
│   ├── data_dictionary.xlsx
│   ├── prompt_engineering.md
│   ├── project_overview.md
│   ├── methodology.md
│   ├── business_recommendations.md
│   └── limitations_and_future_scope.md
│
├── models/
│   ├── sentiment_nb_model.joblib
│   ├── sentiment_tfidf_vectorizer.joblib
│   ├── delivery_time_regression_model.joblib
│   ├── arima_demand_model.pkl
│   └── prophet_demand_model.joblib
│
├── notebooks/
│   ├── day2_segmentation.ipynb
│   ├── day3_sentiment_analysis.ipynb
│   ├── day4_regression_analysis.ipynb
│   ├── day5_demand_forecasting.ipynb
│   └── day6_business_insights.ipynb
│
├── src/
│   ├── generate_data.py
│   └── create_data_dictionary.py
│
├── reports/
│   ├── figures/
│   └── insights/
│
├── presentation/
│
├── README.md
├── requirements.txt
└── .gitignore
```

## Project Workflow

### Day 1 – Project Setup and Synthetic Data Generation

- Created the GitHub repository and project structure.
- Initialized Git and configured the Python environment.
- Generated seven synthetic datasets.
- Performed primary-key uniqueness and basic foreign-key checks.
- Created the data dictionary.
- Documented prompt engineering techniques.

### Day 2 – Customer and Restaurant Segmentation

- Inspected and prepared customer and restaurant datasets.
- Performed feature engineering.
- Applied K-Means clustering.
- Used the Elbow Method and Silhouette Score.
- Applied DBSCAN to identify dense groups and noise points.
- Used PCA for cluster visualization.
- Created cluster profiles and evaluation reports.

### Day 3 – Customer Sentiment Analysis

- Cleaned and preprocessed customer reviews.
- Applied TF-IDF vectorization.
- Implemented Multinomial Naive Bayes classification.
- Compared results with VADER sentiment analysis.
- Evaluated models using accuracy, precision, recall, F1-score, and confusion matrix.
- Identified negative review themes.

### Day 4 – Delivery Time Prediction

- Prepared and combined relevant datasets.
- Selected delivery time as the prediction target.
- Performed feature preprocessing.
- Implemented baseline, Random Forest, Ridge, and Lasso regression models.
- Evaluated models using MAE, RMSE, and R².
- Generated actual-versus-predicted visualizations and feature importance reports.

### Day 5 – Hourly Demand Forecasting

- Aggregated orders into hourly demand.
- Analyzed hourly order patterns.
- Performed time-series decomposition.
- Checked stationarity using the ADF test.
- Implemented baseline, ARIMA, and Prophet forecasting models.
- Evaluated forecasts using MAE, RMSE, and MAPE.

### Day 6 – Integrated Business Insights

- Combined outputs from the analytical stages.
- Calculated business KPIs.
- Summarized customer sentiment.
- Integrated clustering, regression, and forecasting results.
- Prepared business insights and recommendations.

### Day 7 – Final Documentation and Presentation

- Prepared project documentation.
- Updated the README.
- Organized project deliverables.
- Prepared the final capstone presentation.

## Machine Learning and Analytical Techniques

| Analysis | Techniques |
|---|---|
| Customer Segmentation | K-Means, DBSCAN, PCA |
| Restaurant Segmentation | K-Means, DBSCAN, PCA |
| Sentiment Analysis | TF-IDF, Multinomial Naive Bayes, VADER |
| Delivery Time Prediction | Baseline, Random Forest, Ridge, Lasso |
| Demand Forecasting | Baseline, ARIMA, Prophet |

## Evaluation Metrics

**Classification**
- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix

**Regression**
- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R-squared (R²)

**Forecasting**
- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- Mean Absolute Percentage Error (MAPE)

## Key Business Insights

- Customer segmentation identified three distinct customer groups.
- Customer Cluster 1 showed the highest average order frequency and spending.
- Restaurant Cluster 0 showed the highest average order volume and revenue.
- Naive Bayes achieved higher sentiment evaluation scores than VADER on the synthetic review dataset.
- Regression models were developed to estimate delivery time.
- ARIMA and Prophet were implemented to forecast hourly order demand.

Detailed evaluation results, visualizations, and business findings are available in `reports/insights/` and `reports/figures/`.

## How to Run the Project

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
cd uber-eats-intelligence
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
```

### 3. Activate the virtual environment

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Generate synthetic datasets

```bash
python src/generate_data.py
```

### 6. Create the data dictionary

```bash
python src/create_data_dictionary.py
```

### 7. Run the notebooks

```bash
jupyter notebook
```

Open the notebooks in the `notebooks/` directory and execute them in sequence.

**Note:** The notebooks depend on the generated datasets and the outputs of earlier analytical stages. Run the relevant stages in order.

## Project Deliverables

- Seven synthetic raw datasets.
- Processed datasets and engineered features.
- Data dictionary in CSV and Excel formats.
- Five analytical Jupyter notebooks.
- Saved machine learning and forecasting models.
- Model evaluation reports.
- Business KPI summaries.
- Analytical visualizations.
- Business recommendations.
- Project documentation.
- Final presentation.

## Limitations

- The datasets are simulated and do not represent actual Uber Eats operational data.
- Findings and model performance must not be interpreted as actual business results.
- Synthetic review labels may make sentiment classification easier than real-world classification.
- Model performance requires validation using real operational data.
- Forecasting models may not capture unexpected changes in demand.

## Future Scope

- Integrate real-world food delivery datasets.
- Explore advanced NLP models such as BERT.
- Include real-time traffic and weather information.
- Develop interactive dashboards using Power BI or Streamlit.
- Deploy trained models through APIs.
- Monitor model performance using real-time operational data.

## Conclusion

The Uber Eats Operational & Customer Intelligence System demonstrates an end-to-end analytical workflow using Python, machine learning, NLP, and time-series forecasting.

The project provides insights into customer behavior, restaurant performance, customer sentiment, delivery-time prediction, and hourly demand forecasting.

It demonstrates how data-driven analysis can support operational planning, customer experience improvements, and business decision-making.

---

**Project:** Uber Eats Operational & Customer Intelligence System  
**Role:** Trainee Data Analyst  
**Duration:** 7 Days  
**Project Type:** Data Analytics and Machine Learning Capstone
