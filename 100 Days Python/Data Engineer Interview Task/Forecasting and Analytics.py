import pandas as pd
import numpy as np
import statsmodels.api
import xgboost as xgb
import datetime as dt
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import matplotlib
import statsmodels.api as sm

matplotlib.use("TkAgg")

pd.set_option("display.max_columns", None)

# Importing datasets
geolocation_data = pd.read_csv("geolocation.csv", header=0, index_col=0)
geolocation_data.dropna()

customers_data = pd.read_csv("customers.csv", header=0, index_col=0)
customers_data.dropna()

order_items_data = pd.read_csv("order_items.csv", header=0, index_col=0)
order_items_data.dropna()

order_payments_data = pd.read_csv("order_payments.csv", header=0, index_col=0)
order_payments_data.dropna()

order_reviews_data = pd.read_csv("order_reviews.csv", header=0, index_col=0)
order_reviews_data.dropna()

orders_data = pd.read_csv("orders.csv", header=0, index_col=None)
orders_data.dropna()

product_category_trans_data = pd.read_csv(
    "product_category_name_translation.csv", index_col=0
)
product_category_trans_data.dropna()

products_data = pd.read_csv("products.csv", header=0, index_col=0)
products_data.dropna()

sellers_data = pd.read_csv("sellers.csv", header=0, index_col=0)
sellers_data.dropna()
# ``````````````````````````````````````````````````` MERGING DATASETS ```````````````````````````````````````````````````````````
orders_customers = orders_data.merge(customers_data, on="customer_id", how="outer")

merged_orders = orders_customers.merge(order_payments_data, on="order_id", how="outer")

merged_items = merged_orders.merge(order_items_data, on="order_id", how="outer")

orders_products = merged_items.merge(products_data, on="product_id", how="outer")

orders_products_translated = orders_products.merge(
    product_category_trans_data,
    on="product_category_name",
    how="outer",
)
# ``````````````````````````````````````` DROPING UNNECESSARY COLUMNS `````````````````````````````````````````
orders_products_translated.drop(
    columns=[
        "product_length_cm",
        "product_width_cm",
        "product_height_cm",
        "product_photos_qty",
        "product_weight_g",
    ],
    axis=1,
    inplace=True,
)

orders_products_translated.sort_values(
    by="order_purchase_timestamp", inplace=True, ascending=False
)
# `````````````````````````````````````` SPLITTING DATA ``````````````````````````````
# Here I've split my data into train and test subsets. Train subset data consists of all data points up to one month before data capture
# Test data however will be the 2 weeks prediction as mention in the task
train = orders_products_translated.loc[
    orders_products_translated["order_purchase_timestamp"] < "2018-09-17"
]
test = orders_products_translated.loc[
    orders_products_translated["order_purchase_timestamp"] >= "2018-10-01"
]


order_counts = (
    train.groupby("order_purchase_timestamp")["order_item_id"].count().reset_index()
)
order_counts["date"] = pd.to_datetime(
    order_counts["order_purchase_timestamp"]
)  # Extract the date
order_counts = order_counts.rename(columns={"order_item_id": "order_quantity"})
training_data = train.merge(order_counts, how="left", on="order_purchase_timestamp")
training_data["product_category_name_english"] = training_data[
    "product_category_name_english"
].astype("string")

training_data["day_of_week"] = training_data["date"].dt.weekday
training_data["year"] = training_data["date"].dt.year
training_data["month"] = training_data["date"].dt.month
training_data.set_index("date", inplace=True)

train_target = training_data["order_quantity"].values
train_features = training_data[["day_of_week", "month", "year", "price"]]


# ``````````````````````````````````````````````````PREPARING TESTING FEATURES````````````````````````````````````````
# Creating Testing Features
test_order_count = (
    test.groupby("order_purchase_timestamp")["order_item_id"].count().reset_index()
)
test_order_count = test_order_count.rename(columns={"order_item_id": "order_quantity"})
testing_data = test.merge(test_order_count, how="left", on="order_purchase_timestamp")
testing_data["date"] = pd.to_datetime(
    test_order_count["order_purchase_timestamp"]
)  # Extract the date
testing_data["product_category_name_english"] = testing_data[
    "product_category_name_english"
].astype("string")

testing_data["day_of_week"] = pd.to_datetime(
    testing_data["order_purchase_timestamp"]
).dt.weekday
testing_data["year"] = pd.to_datetime(testing_data["order_purchase_timestamp"]).dt.year
testing_data["month"] = pd.to_datetime(
    testing_data["order_purchase_timestamp"]
).dt.month
testing_data.set_index("date", inplace=True)

test_target = testing_data["order_quantity"].values
test_features = testing_data[["day_of_week", "month", "year", "price"]]
# ``````````````````````````````````````````````````PUTTING DATA INTO MY MODEL ``````````````````````````````````````````
# Train Data
# objective="reg:squarederror",  # Set the objective function for regression (mean squared error)
# n_estimators = 1000,  # Number of decision trees to grow (can be tuned)
# learning_rate = 0.2  # Learning rate for updating weights during training (can be tuned)

model = xgb.XGBRegressor(
    objective="reg:squarederror", n_estimators=1000, learning_rate=0.2
)
# Train the model on the features and target
print(train_features.dtypes)
model.fit(train_features, train_target)

# Making predictions
prediction = model.predict(test_features)

# Plotting the model's performance
mse = mean_squared_error(test_target, prediction)
print("Mean Squared Error:", mse)
average_order_quantity = training_data["order_quantity"].mean()
relative_error = mse / (average_order_quantity**2)
print("Relative Error:", relative_error)

## Here I noticed that all previous data orders are cancelled. However I will keep those rows and try to optimise the algorythm

testing_data["prediction"] = model.predict(test_features)
orders_products_translated.merge(
    testing_data[["prediction"]], how="left", left_index=True, right_index=True
)
testing_data["error"] = np.abs(test_target - testing_data["prediction"])
testing_data["testing_date"] = testing_data.index.date
testing_data.groupby(["testing_date"])["error"].mean().sort_values()

# Here I am trying to train the model so that it will not show negative order demant which makes no sense.
# I will apply logarytmic function. This ensures non-negative values are mapped to a wider range on the number line.

# Transformation
train_features.loc[:, "log_quantity"] = np.log1p(training_data["order_quantity"]).copy()
test_features.loc[:, "log_quantity"] = np.log1p(testing_data["order_quantity"]).copy()

# Train the model with transformed target variable (log_quantity)
model = xgb.XGBRegressor(
    objective="reg:squarederror", n_estimators=1000, learning_rate=0.2
)
model.fit(
    train_features[["day_of_week", "month", "year", "log_quantity"]],
    train_features["log_quantity"],
)

# Predictions and Back-transformation
prediction_log = model.predict(
    test_features[["day_of_week", "month", "year", "log_quantity"]]
)
test.loc[:, "predicted_demand"] = np.exp(prediction_log)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# Plot on first axis (original scale)
ax1.scatter(
    testing_data.index,
    testing_data["order_quantity"].values,
    label="Actual Demand",
    color="red",
)
ax1.plot(
    testing_data.index, prediction, label="Actual Demand", color="red"
)  # Add line plot
ax1.set_xlabel("Date")
ax1.set_ylabel("Order Quantity")
ax1.set_title("Actual Demand (Original Scale)")
fig.autofmt_xdate()

# Plot on second axis (log scale)
ax2.scatter(
    testing_data.index,
    testing_data["order_quantity"].values,
    label="Actual Demand",
    color="blue",
)  # Back-transform predictions
ax2.plot(
    testing_data.index, np.exp(prediction_log), label="Predicted Demand", color="blue"
)  # Add line plot
ax2.set_xlabel("Date")
ax2.set_ylabel("Order Quantity (Log Scale)")
ax2.set_title("Predicted Demand (Log Scale)")

fig.autofmt_xdate()
plt.legend()
plt.tight_layout()
plt.show()


# ```````````````````````````````````````````````````````````````` Linear Regression


train_features_with_constant = sm.add_constant(train_features, has_constant="add")
test_features_with_constant = sm.add_constant(test_features, has_constant="add")
test_features_with_constant["price"] = test_features_with_constant["price"].fillna(0)
train_features_with_constant["price"] = train_features_with_constant["price"].fillna(0)

model_classic = sm.OLS(train_features_with_constant, train_target).fit()
prediction_classic = model_classic.predict(test_features_with_constant)

# Evaluating the linear regression model using Mean Squared Error
mse_linear = mean_squared_error(test_target, prediction_classic)
print("Mean Squared Error:", mse_linear)
average_order_quantity = training_data["order_quantity"].mean()
relative_error = mse / (average_order_quantity**2)
print("Relative Error:", relative_error)
summary = model_classic.summary()
print(summary)
