import string
import pandas as pd
from textblob import TextBlob
from scipy.stats import pearsonr
import matplotlib.pyplot as plt

user_reviews = pd.read_csv("order_reviews.csv", header=0)

order_items = pd.read_csv("order_items.csv", header=0)

reviews_orders = user_reviews.merge(order_items, on="order_id", how="inner")


def clean_text(text):
    text = str(text)  # Ensure text is a string
    text = text.lower()  # Convert to lowercase
    text = "".join(
        char for char in text if char not in string.punctuation
    )  # Remove punctuation
    return text


reviews_orders["review_comment_message"] = reviews_orders[
    "review_comment_message"
].apply(clean_text)
# Create a new column to store sentiment polarity scores
reviews_orders["sentiment_polarity"] = reviews_orders["review_comment_message"].apply(
    lambda text: TextBlob(text).sentiment.polarity
)

correlation, p_value = pearsonr(
    reviews_orders["review_score"], reviews_orders["sentiment_polarity"]
)
print("Correlation between rating and sentiment polarity:", correlation)

seller_groups = reviews_orders.groupby("seller_id")


# Define a function to analyze sentiment distribution per seller group
def analyze_seller_sentiment(seller_data):
    average_polarity = seller_data["sentiment_polarity"].mean()
    # Add additional logic here to identify problematic sellers based on sentiment
    low_sentiment_sellers = seller_data[
        seller_data["sentiment_polarity"] < -0.2
    ]  # Example threshold, adjust as needed
    # Print or store the results of problematic sellers (seller IDs or dataframes)
    if len(low_sentiment_sellers) != 0:
        print(
            f"Sellers with potentially low sentiment: {low_sentiment_sellers['seller_id'].unique()}"
        )
    return average_polarity


average_sentiment_per_seller = reviews_orders.groupby("seller_id")[
    "sentiment_polarity"
].mean()

plt.figure(figsize=(10, 6))  # Increase figure size for better readability
plt.bar(average_sentiment_per_seller.index, average_sentiment_per_seller.values)
plt.xlabel("Seller ID")
plt.ylabel("Average Sentiment Polarity")
plt.title("Average Sentiment Polarity of Sellers on Review Platform")
plt.xticks(
    rotation=45
)  # Rotate seller ID labels for better readability with many sellers
plt.grid(True)
plt.tight_layout()

# Apply the function to each seller group
seller_groups.apply(analyze_seller_sentiment)

plt.scatter(reviews_orders["review_score"], reviews_orders["sentiment_polarity"])
plt.xlabel("Review Score (1-5)")
plt.ylabel("Sentiment Polarity")
plt.title("Sentiment Polarity vs Review Score Distribution")
plt.grid(True)

# Visualize Results (Bar Chart - Average Sentiment per Seller)
plt.figure(figsize=(10, 6))  # Increase figure size for better readability
plt.bar(average_sentiment_per_seller.index, average_sentiment_per_seller.values)
plt.xlabel("Seller ID")
plt.ylabel("Average Sentiment Polarity")
plt.title("Average Sentiment Polarity of Sellers on Review Platform")
plt.xticks(
    rotation=45
)  # Rotate seller ID labels for better readability with many sellers
plt.grid(True)
plt.tight_layout()

plt.bar(average_sentiment_per_seller.index, average_sentiment_per_seller.values)
plt.xlabel("Seller ID")
plt.ylabel("Average Sentiment Polarity")
plt.title("Average Sentiment Polarity per Seller")
plt.xticks(
    rotation=45
)  # Rotate seller ID labels for better readability with many sellers
plt.grid(True)

bars = plt.bar(
    average_sentiment_per_seller.index,
    average_sentiment_per_seller.values,
    label=average_sentiment_per_seller.index,
)  # Store the bar container

for bar in bars:
    value = average_sentiment_per_seller[
        bar.get_label()
    ]  # Get corresponding sentiment value by label
    plt.text(
        bar.get_x() + bar.get_width() / 2, value + 0.01, f"{value:.2f}", ha="center"
    )  # Adjust y-offset for better positioning
plt.legend()
plt.tight_layout()
plt.show()
