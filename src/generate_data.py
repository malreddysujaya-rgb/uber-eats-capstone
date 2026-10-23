
from pathlib import Path
import numpy as np
import pandas as pd

# Use a fixed seed so the data can be reproduced
rng = np.random.default_rng(42)

# Project folders
PROJECT_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = PROJECT_DIR / "data" / "raw"
RAW_DIR.mkdir(parents=True, exist_ok=True)

# Number of records to generate
N_CUSTOMERS = 500
N_RESTAURANTS = 60
N_DRIVERS = 100
N_ORDERS = 5000

# -------------------------
# 1. Generate customers
# -------------------------
customers = pd.DataFrame({
    "customer_id": range(1, N_CUSTOMERS + 1),
    "age": rng.integers(18, 66, N_CUSTOMERS),
    "city": rng.choice(
        ["Hyderabad", "Bengaluru", "Chennai", "Mumbai", "Delhi"],
        N_CUSTOMERS
    ),
    "signup_date": pd.to_datetime(
        rng.choice(
            pd.date_range("2023-01-01", "2025-12-31"),
            N_CUSTOMERS
        )
    )
})

# -------------------------
# 2. Generate restaurants
# -------------------------
restaurants = pd.DataFrame({
    "restaurant_id": range(1, N_RESTAURANTS + 1),
    "restaurant_name": [
        f"Restaurant_{i}" for i in range(1, N_RESTAURANTS + 1)
    ],
    "category": rng.choice(
        ["Indian", "Chinese", "Italian", "Fast Food", "Healthy"],
        N_RESTAURANTS
    ),
    "city": rng.choice(
        ["Hyderabad", "Bengaluru", "Chennai", "Mumbai", "Delhi"],
        N_RESTAURANTS
    ),
    "restaurant_rating": np.round(
        rng.uniform(2.5, 5.0, N_RESTAURANTS), 1
    )
})

# -------------------------
# 3. Generate drivers
# -------------------------
drivers = pd.DataFrame({
    "driver_id": range(1, N_DRIVERS + 1),
    "experience_years": rng.integers(0, 11, N_DRIVERS),
    "vehicle_type": rng.choice(
        ["Bike", "Scooter", "Car"],
        N_DRIVERS,
        p=[0.45, 0.45, 0.10]
    )
})

# -------------------------
# 4. Generate orders
# -------------------------
order_customer_ids = rng.integers(1, N_CUSTOMERS + 1, N_ORDERS)
order_restaurant_ids = rng.integers(1, N_RESTAURANTS + 1, N_ORDERS)

order_timestamps = (
    pd.Timestamp("2026-01-01")
    + pd.to_timedelta(
        rng.integers(0, 90 * 24 * 60, N_ORDERS), unit="m"
    )
)

order_amounts = np.round(
    rng.gamma(shape=2.5, scale=250, size=N_ORDERS) + 100, 2
)

number_of_items = rng.integers(1, 9, N_ORDERS)

order_statuses = rng.choice(
    ["Completed", "Cancelled", "Preparing", "In Transit"],
    N_ORDERS,
    p=[0.82, 0.08, 0.04, 0.06]
)

orders = pd.DataFrame({
    "order_id": range(1, N_ORDERS + 1),
    "customer_id": order_customer_ids,
    "restaurant_id": order_restaurant_ids,
    "order_timestamp": order_timestamps,
    "order_amount": order_amounts,
    "number_of_items": number_of_items,
    "order_status": order_statuses
})

# -------------------------
# 5. Generate deliveries
# -------------------------
delivery_distances = np.round(
    rng.uniform(0.5, 15, N_ORDERS), 2
)
preparation_times = rng.integers(5, 46, N_ORDERS)
traffic_conditions = rng.choice(
    ["Low", "Medium", "High"], N_ORDERS, p=[0.3, 0.45, 0.25]
)
weather_conditions = rng.choice(
    ["Clear", "Rain", "Cloudy", "Hot"], N_ORDERS
)

delivery_times = np.maximum(
    10,
    12
    + delivery_distances * 2.2
    + preparation_times * 0.65
    + np.where(traffic_conditions == "High", 15, 0)
    + np.where(traffic_conditions == "Medium", 6, 0)
    + np.where(weather_conditions == "Rain", 8, 0)
    + rng.normal(0, 5, N_ORDERS)
).round(1)

deliveries = pd.DataFrame({
    "delivery_id": range(1, N_ORDERS + 1),
    "order_id": orders["order_id"],
    "driver_id": rng.integers(1, N_DRIVERS + 1, N_ORDERS),
    "delivery_distance_km": delivery_distances,
    "preparation_time_minutes": preparation_times,
    "delivery_time_minutes": delivery_times,
    "weather": weather_conditions,
    "traffic_condition": traffic_conditions
})

# -------------------------
# 6. Generate customer reviews
# -------------------------
positive_reviews = [
    "Great food and fast delivery",
    "Excellent service and tasty food",
    "The order arrived on time",
    "Very good experience",
    "Fresh food and friendly service"
]

negative_reviews = [
    "Food arrived cold and late",
    "Delivery was very slow",
    "Order was missing items",
    "Poor packaging and bad service",
    "Very disappointing experience"
]

neutral_reviews = [
    "The food was okay",
    "Average delivery experience",
    "Nothing special about the order",
    "Service was acceptable",
    "The order was as expected"
]

review_rows = []

# Create reviews for a subset of orders
review_order_indices = rng.choice(
    N_ORDERS, size=round(N_ORDERS * 0.75), replace=False
)

for idx in review_order_indices:
    sentiment = rng.choice(
        ["Positive", "Negative", "Neutral"],
        p=[0.55, 0.25, 0.20]
    )

    if sentiment == "Positive":
        review_text = rng.choice(positive_reviews)
    elif sentiment == "Negative":
        review_text = rng.choice(negative_reviews)
    else:
        review_text = rng.choice(neutral_reviews)

    review_rows.append({
        "review_id": len(review_rows) + 1,
        "order_id": int(orders.iloc[idx]["order_id"]),
        "customer_id": int(orders.iloc[idx]["customer_id"]),
        "restaurant_id": int(orders.iloc[idx]["restaurant_id"]),
        "review_text": review_text,
        "sentiment_label": sentiment
    })

reviews = pd.DataFrame(review_rows)

# -------------------------
# 7. Generate payments
# -------------------------
tips = np.round(
    np.maximum(0, rng.normal(35, 25, N_ORDERS)), 2
)

payments = pd.DataFrame({
    "payment_id": range(1, N_ORDERS + 1),
    "order_id": orders["order_id"],
    "payment_method": rng.choice(
        ["UPI", "Card", "Cash", "Wallet"],
        N_ORDERS,
        p=[0.45, 0.25, 0.15, 0.15]
    ),
    "tip_amount": tips,
    "total_amount": np.round(order_amounts + tips, 2)
})

# -------------------------
# 8. Save all datasets
# -------------------------
datasets = {
    "customers.csv": customers,
    "restaurants.csv": restaurants,
    "orders.csv": orders,
    "deliveries.csv": deliveries,
    "drivers.csv": drivers,
    "reviews.csv": reviews,
    "payments.csv": payments
}

print("Synthetic data generation started.")

for filename, dataframe in datasets.items():
    output_path = RAW_DIR / filename
    dataframe.to_csv(output_path, index=False)
    print(f"Created {filename}: {len(dataframe)} rows, "
          f"{len(dataframe.columns)} columns")

# -------------------------
# 9. Basic validation
# -------------------------
assert customers["customer_id"].is_unique
assert restaurants["restaurant_id"].is_unique
assert drivers["driver_id"].is_unique
assert orders["order_id"].is_unique

assert orders["customer_id"].isin(
    customers["customer_id"]
).all()

assert orders["restaurant_id"].isin(
    restaurants["restaurant_id"]
).all()

assert deliveries["order_id"].isin(orders["order_id"]).all()
assert deliveries["driver_id"].isin(drivers["driver_id"]).all()
assert reviews["order_id"].isin(orders["order_id"]).all()
assert payments["order_id"].isin(orders["order_id"]).all()

print("\nAll seven datasets generated successfully.")
print("Primary key and foreign key checks passed.")
print(f"Files saved in: {RAW_DIR}")
