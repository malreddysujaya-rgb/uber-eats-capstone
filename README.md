# Uber Eats Operational & Customer Intelligence System

## Project Overview

This project develops an end-to-end machine learning and analytics solution for a simulated food-delivery marketplace.

The objective is to analyze customer and restaurant behavior, understand customer feedback, predict delivery performance, and forecast hourly order demand.

## Dataset

The project uses seven synthetic datasets:

- Customers
- Restaurants
- Orders
- Deliveries
- Drivers
- Reviews
- Payments

The datasets are generated using Python, pandas, and NumPy. They are synthetic and do not represent actual Uber Eats customer records.

## Technologies

- Python
- Pandas and NumPy
- Matplotlib and Seaborn
- Scikit-learn
- NLTK
- Statsmodels
- Prophet
- Git

## Project Structure

- `data/raw/` — Generated CSV datasets
- `data/processed/` — Cleaned datasets and engineered features
- `notebooks/` — Exploratory analysis and model experiments
- `src/` — Python scripts and reusable pipelines
- `models/` — Saved machine learning models
- `reports/figures/` — Charts and plots
- `reports/insights/` — Findings and evaluation results
- `docs/` — Data dictionary and documentation
- `presentation/` — Final presentation

## Project Workflow

1. Project setup and synthetic data generation
2. Data preparation and customer/restaurant segmentation
3. NLP-based customer sentiment analysis
4. Delivery-time regression
5. Hourly demand forecasting
6. Integrated ML pipeline and business insights
7. Final documentation and presentation

## Current Progress

Day 1: Project structure created, Git initialized, Python environment configured, and seven synthetic datasets generated. Primary-key uniqueness and basic foreign-key checks passed.

## How to Run

Activate the project's virtual environment and install dependencies:

```bash
source .venv/bin/activate
python -m pip install -r requirements.txt
```

Generate the datasets:

```bash
python src/generate_data.py
```

Create the data dictionary:

```bash
python src/create_data_dictionary.py
```

## Limitations

The datasets are simulated. Findings and model performance must not be interpreted as actual Uber Eats business results.
