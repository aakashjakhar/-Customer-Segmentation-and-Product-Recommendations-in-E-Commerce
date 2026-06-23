import streamlit as st
import pandas as pd
import pickle

# Load the saved recommendation data
@st.cache_resource
def load_data():
    with open("recommendation_model.pkl", "rb") as file:
        return pickle.load(file)

data = load_data()

similarity_matrix = data["similarity_matrix"]
product_names = data["product_names"]


# Function to get recommendations
def recommend(product_name, top_n=5):

    if product_name not in similarity_matrix.index:
        return None

    similar_products = similarity_matrix.loc[product_name]

    similar_products = similar_products.sort_values(ascending=False)

    similar_products = similar_products.iloc[1:top_n + 1]

    recommendations = pd.DataFrame({
        "Recommended Product": similar_products.index,
        "Similarity Score": similar_products.values
    })

    recommendations["Similarity Score"] = recommendations["Similarity Score"].round(3)

    return recommendations


# ---------------- UI ----------------

st.set_page_config(
    page_title="Product Recommendation System",
    page_icon="🛍️"
)

st.title("🛍️ Product Recommendation System")

st.write(
    "Select a product and get the top 5 similar product recommendations."
)

selected_product = st.selectbox(
    "Choose a Product",
    product_names
)

if st.button("Recommend"):

    result = recommend(selected_product)

    if result is None:
        st.error("Product not found.")

    else:
        st.subheader("Recommended Products")
        st.dataframe(result, use_container_width=True)