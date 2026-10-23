
from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = PROJECT_DIR / "data" / "raw"
DOCS_DIR = PROJECT_DIR / "docs"
DOCS_DIR.mkdir(parents=True, exist_ok=True)

# Business descriptions for each dataset
descriptions = {
    "customers": {
        "customer_id": "Unique identifier for each customer",
        "age": "Customer age in years",
        "city": "City where the customer is located",
        "signup_date": "Date when the customer registered"
    },
    "restaurants": {
        "restaurant_id": "Unique restaurant identifier",
        "restaurant_name": "Name assigned to the restaurant",
        "category": "Type of cuisine served",
        "city": "City where the restaurant operates",
        "restaurant_rating": "Restaurant rating on a 2.5 to 5 scale"
    },
    "orders": {
        "order_id": "Unique identifier for each order",
        "customer_id": "Customer who placed the order",
        "restaurant_id": "Restaurant receiving the order",
        "order_timestamp": "Date and time the order was placed",
        "order_amount": "Value of the ordered food before tip",
        "number_of_items": "Number of items in the order",
        "order_status": "Current or simulated order status"
    },
    "deliveries": {
        "delivery_id": "Unique delivery record identifier",
        "order_id": "Order associated with the delivery",
        "driver_id": "Driver assigned to the delivery",
        "delivery_distance_km": "Delivery distance in kilometers",
        "preparation_time_minutes": "Restaurant preparation time in minutes",
        "delivery_time_minutes": "Simulated delivery time in minutes",
        "weather": "Weather condition during the simulated delivery",
        "traffic_condition": "Traffic level during the simulated delivery"
    },
    "drivers": {
        "driver_id": "Unique identifier for each driver",
        "experience_years": "Driver experience in years",
        "vehicle_type": "Vehicle used by the driver"
    },
    "reviews": {
        "review_id": "Unique review identifier",
        "order_id": "Order being reviewed",
        "customer_id": "Customer who wrote the review",
        "restaurant_id": "Restaurant being reviewed",
        "review_text": "Synthetic customer feedback text",
        "sentiment_label": "Synthetic sentiment label assigned to the review"
    },
    "payments": {
        "payment_id": "Unique payment record identifier",
        "order_id": "Order associated with the payment",
        "payment_method": "Method used for payment",
        "tip_amount": "Simulated delivery tip amount",
        "total_amount": "Order amount plus tip"
    }
}

rows = []

for dataset_name, column_descriptions in descriptions.items():
    file_path = RAW_DIR / f"{dataset_name}.csv"
    dataframe = pd.read_csv(file_path)

    for column in dataframe.columns:
        if column in ["customer_id", "restaurant_id", "driver_id",
                      "order_id", "delivery_id", "review_id", "payment_id"]:
            if column in ["customer_id", "restaurant_id", "driver_id",
                          "order_id", "delivery_id", "review_id", "payment_id"]:
                key_type = "Primary key" if column.endswith("_id") and column not in [
                    "customer_id", "restaurant_id", "driver_id", "order_id"
                ] else "Identifier / Foreign key"
        else:
            key_type = "Neither"

        if dataset_name == "customers" and column == "customer_id":
            key_type = "Primary key"
        elif dataset_name == "restaurants" and column == "restaurant_id":
            key_type = "Primary key"
        elif dataset_name == "drivers" and column == "driver_id":
            key_type = "Primary key"
        elif dataset_name == "orders" and column == "order_id":
            key_type = "Primary key"
        elif dataset_name == "deliveries" and column == "delivery_id":
            key_type = "Primary key"
        elif dataset_name == "reviews" and column == "review_id":
            key_type = "Primary key"
        elif dataset_name == "payments" and column == "payment_id":
            key_type = "Primary key"
        elif column in ["customer_id", "restaurant_id", "driver_id", "order_id"]:
            key_type = "Foreign key"

        sample = dataframe[column].dropna()
        example = str(sample.iloc[0]) if not sample.empty else ""

        rows.append({
            "Dataset": f"{dataset_name}.csv",
            "Column": column,
            "Data Type": str(dataframe[column].dtype),
            "Description": column_descriptions.get(
                column, "Description to be reviewed"
            ),
            "Example": example,
            "Key / Relationship": key_type
        })

dictionary = pd.DataFrame(rows)

csv_path = DOCS_DIR / "data_dictionary.csv"
dictionary.to_csv(csv_path, index=False)

# Excel output is optional; requires openpyxl
try:
    excel_path = DOCS_DIR / "data_dictionary.xlsx"
    dictionary.to_excel(excel_path, index=False)
    print(f"Excel dictionary saved: {excel_path}")
except ImportError:
    print("openpyxl is not installed. CSV dictionary was created.")

print(f"CSV dictionary saved: {csv_path}")
print(f"Total documented columns: {len(dictionary)}")
