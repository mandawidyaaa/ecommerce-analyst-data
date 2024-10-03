import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the merged dataset
data = pd.read_csv('dashboard/combined_data_for_dashboard (1).csv')

# Dashboard title
st.title('E-commerce Data Analysis Dashboard')

# Helper function to display top sellers by revenue
def top_sellers(data, top_n=5):
    top_sellers_data = data.groupby('seller_id')['price'].sum().nlargest(top_n).reset_index()
    return top_sellers_data

# Helper function to display top products by revenue
def top_products(data, top_n=10):
    top_products_data = data.groupby('product_category_name')['price'].sum().nlargest(top_n).reset_index()  
    return top_products_data

# Helper function to display top customer states by orders
def top_states(data, top_n=10):
    top_states_data = data['customer_state'].value_counts().nlargest(top_n).reset_index()
    top_states_data.columns = ['customer_state', 'number_of_orders']  
    return top_states_data

# Create tabs for different analysis views
tab1, tab2, tab3 = st.tabs(["Top Sellers", "Top Products", "Customer States"])

# Tab 1: Top Sellers
with tab1:
    st.header("Top 5 Sellers Dari Pendapatan")
    top_sellers_data = top_sellers(data)
    st.write(top_sellers_data)

    # Bar chart for top sellers
    plt.figure(figsize=(20, 15))
    plt.bar(top_sellers_data['seller_id'], top_sellers_data['price'], color='skyblue')
    plt.xlabel('Seller ID', fontsize=20)  # Perbesar ukuran font untuk label sumbu X
    plt.ylabel('Sales Count', fontsize=20)  # Perbesar ukuran font untuk label sumbu Y
    plt.title('Top 5 Sellers Dari Pendapatan', fontsize=24)  # Perbesar ukuran font untuk judul
    plt.xticks(rotation=0, fontsize=10)  # Ukuran font untuk label sumbu X
    plt.yticks(fontsize=15)  # Ukuran font untuk nilai sumbu Y (50000, 100000, dll)
    st.pyplot(plt)


# Tab 2: Top Products
with tab2:
    st.header("Produk dengan Pendapatan Tertinggi")
    top_products_data = top_products(data)
    st.write(top_products_data)

    # Pie chart for top products
    plt.figure(figsize=(10, 6))
    plt.pie(top_products_data['price'], labels=top_products_data['product_category_name'], autopct='%1.1f%%', startangle=140)
    plt.title('Produk dengan Pendapatan Tertinggi', fontsize=14)
    st.pyplot(plt)

# Tab 3: Customer States
with tab3:
    st.header("Wilayah Negara yang Memiliki Pelanggan Terbanyak")
    top_states_data = top_states(data)
    st.write(top_states_data)

    # Bar chart for top customer states
    plt.figure(figsize=(10, 6))
    plt.barh(top_states_data['customer_state'], top_states_data['number_of_orders'], color='orange')  # Horizontal bar chart
    plt.xlabel('Customer Count', fontsize=12)  # Update label for clarity
    plt.ylabel('Customer State', fontsize=12)  # Updated label
    plt.title('Wilayah Negara yang Memiliki Pelanggan Terbanyak', fontsize=14)
    st.pyplot(plt)
