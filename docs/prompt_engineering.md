# Prompt Engineering for Synthetic Data Generation

## 1. Objective

The objective of prompt engineering was to generate a Python script that creates realistic synthetic datasets for the Uber Eats Operational & Customer Intelligence System capstone.

The generated datasets support customer and restaurant segmentation, customer sentiment analysis, delivery-time prediction, and hourly demand forecasting.

## 2. P.T.C.F. Prompting

P.T.C.F. stands for **Persona, Task, Context, and Format**.

### Prompt

**Persona:** Act as an experienced data engineer and food-delivery marketplace analytics expert.

**Task:** Develop a Python script to generate seven related synthetic datasets for an Uber Eats analytics project.

**Context:** The data will be used for customer and restaurant segmentation, NLP-based sentiment analysis, delivery-time prediction, and hourly order-demand forecasting. The datasets must contain realistic business attributes and consistent relationships.

**Format:** Provide a complete Python script using pandas and NumPy. Save the generated datasets as CSV files in `data/raw/`. Include comments, a fixed random seed, and validation checks.

### Application

The P.T.C.F. framework helped organize the request into a clear role, objective, business context, and expected output. This made the requirements for the Python script easier to communicate.

## 3. Role-Based Prompting

### Prompt

Act as a data engineer working on a food-delivery analytics platform. Design related customer, restaurant, order, delivery, driver, review, and payment datasets. Ensure that identifiers and relationships are consistent across the datasets.

### Application

Role-based prompting established the perspective of a data engineer. It helped focus the script on dataset design, identifier consistency, reproducibility, and validation.

## 4. Few-Shot Prompting

Few-shot prompting provides examples of the expected output so the model can follow the required structure.

### Example

Example customer record:

- customer_id: 101
- age: 28
- city: Hyderabad
- signup_date: 2025-03-12

Example order record:

- order_id: 5001
- customer_id: 101
- restaurant_id: 12
- order_amount: 650.00
- number_of_items: 3
- order_status: Completed

### Prompt

Use the example records to understand the expected columns and value formats. Generate additional synthetic records that follow the same structure, use valid identifiers, and maintain relationships between customers, restaurants, and orders.

### Application

The examples illustrate the expected schema and data formats. They help guide the generation of consistent records instead of leaving the output structure ambiguous.

Note: These are illustrative prompt examples, not a record of a previously executed prompt unless they were actually used.

## 5. Structured Output Prompting

### Prompt

Generate exactly seven CSV files with these filenames:

1. customers.csv
2. restaurants.csv
3. orders.csv
4. deliveries.csv
5. drivers.csv
6. reviews.csv
7. payments.csv

Use consistent column names, appropriate data types, unique primary keys, and valid foreign-key references. Save all files in `data/raw/`. Print the row count and column count of each file. Validate the primary keys and foreign-key relationships after generation.

### Application

Structured-output prompting specified the expected filenames, output format, and validation requirements. This made the results easier to inspect, document, and reuse in later machine learning tasks.

## 6. Synthetic Data Generation

The Python script `src/generate_data.py` uses pandas and NumPy to generate the seven datasets.

A fixed random seed is used to make the generated data reproducible. The script also checks primary-key uniqueness and selected foreign-key relationships before completing.

## 7. Results

The script generated the following datasets:

| Dataset | Rows |
|---|---:|
| Customers | 500 |
| Restaurants | 60 |
| Orders | 5,000 |
| Deliveries | 5,000 |
| Drivers | 100 |
| Reviews | 3,750 |
| Payments | 5,000 |

The script reported that all seven datasets were generated successfully and that the primary-key and foreign-key checks passed.

## 8. Conclusion

Prompt engineering helped define the requirements, structure, and expected outputs of the synthetic data-generation process. The resulting Python script created seven related CSV datasets that form the foundation for the remaining stages of the capstone.

The datasets are synthetic and should not be interpreted as actual Uber Eats operational data.
