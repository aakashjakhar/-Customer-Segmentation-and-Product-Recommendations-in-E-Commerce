# -Customer-Segmentation-and-Product-Recommendations-in-E-Commerce
This project explores e-commerce transaction data to uncover customer behavior patterns. By leveraging machine learning, I’ve built a system that segments customers into actionable groups and recommends products based on their purchase history.🚀 Overview

The global e-commerce industry generates massive amounts of data. The goal of this project is to turn that raw transaction data into business insights. I focused on two main areas:
Customer Segmentation: Using RFM (Recency, Frequency, Monetary) analysis to categorize customers, helping businesses identify high-value users versus those at risk of churning.
Recommendation System: Using collaborative filtering to suggest relevant products to users based on shared purchase history.
🛠 Tech Stack
Languages & Libraries: Python, Pandas, NumPy, Scikit-Learn
Key Techniques: K-Means Clustering, RFM Analysis, Collaborative Filtering, Cosine Similarity
Deployment: Streamlit (for the interactive dashboard)
📊 Key Features
Customer Segmentation Module: Users can input customer metrics (Recency, Frequency, Monetary value) and the model will label them as High-Value, Regular, Occasional, or At-Risk.
Product Recommendation Module: Built on item-based collaborative filtering, this module takes a product name as input and outputs the top 5 most similar products based on cross-customer purchase trends.
📝 Project Workflow
Data Cleaning: Preprocessed the dataset by removing missing values, filtering out cancelled invoices, and handling negative/zero pricing.
EDA: Explored trends like top-selling products, purchase patterns over time, and RFM distributions.
Clustering: Applied K-Means clustering (supported by the Elbow Method and Silhouette Score) to categorize customers into segments.
Modeling: Built a product similarity matrix using cosine similarity to power the recommendation engine.
📱 How to Use

The project includes a Streamlit app that makes these insights interactive:
Recommendation: Enter any product name, and the app will suggest 5 related items.
Segmentation: Input specific customer stats (Recency, Frequency, Monetary spend) to see which segment a customer belongs to in real-time.

