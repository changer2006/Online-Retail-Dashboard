import streamlit as st
import pandas as pd

# ---------------------------------
# PAGE CONFIG
# ---------------------------------

st.set_page_config(
    page_title="Online Retail Dashboard",
    page_icon="📊",
    layout="wide"
)

# ---------------------------------
# CUSTOM CSS
# ---------------------------------

st.markdown(
    """
    <style>

    .main {
        background-color: #f8fafc;
    }

    div[data-testid="metric-container"] {
        background-color: white;
        border: 2px solid #4f46e5;
        padding: 15px;
        border-radius: 15px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
    }

    h1 {
        color: #4f46e5;
        text-align: center;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# ---------------------------------
# TITLE
# ---------------------------------

st.markdown(
    """
    <h1>📊 Online Retail Analytics Dashboard</h1>
    """,
    unsafe_allow_html=True
)

st.success(
    "✅ Interactive Business Dashboard"
)

# ---------------------------------
# LOAD DATA
# ---------------------------------

df = pd.read_excel("Online Retail.xlsx")

df = df.drop_duplicates()

df = df.dropna(
    subset=["CustomerID"]
)

df["Revenue"] = (
    df["Quantity"] *
    df["UnitPrice"]
)

# ---------------------------------
# KPI SECTION
# ---------------------------------

total_revenue = round(
    df["Revenue"].sum(),
    2
)

total_customers = (
    df["CustomerID"].nunique()
)

total_products = (
    df["StockCode"].nunique()
)

total_countries = (
    df["Country"].nunique()
)

st.subheader("📌 Business Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "💰 Revenue",
    f"${total_revenue:,.0f}"
)

col2.metric(
    "👥 Customers",
    total_customers
)

col3.metric(
    "📦 Products",
    total_products
)

col4.metric(
    "🌍 Countries",
    total_countries
)

# ---------------------------------
# TOP PRODUCTS
# ---------------------------------

st.subheader(
    "🏆 Top 10 Products By Revenue"
)

top_products = (
    df.groupby("Description")["Revenue"]
    .sum()
    .sort_values(
        ascending=False
    )
    .head(10)
)

st.bar_chart(top_products)

# ---------------------------------
# TOP COUNTRIES
# ---------------------------------

st.subheader(
    "🌎 Top 10 Countries By Revenue"
)

top_countries = (
    df.groupby("Country")["Revenue"]
    .sum()
    .sort_values(
        ascending=False
    )
    .head(10)
)

st.bar_chart(top_countries)

# ---------------------------------
# MONTHLY SALES TREND
# ---------------------------------

df["InvoiceDate"] = pd.to_datetime(
    df["InvoiceDate"]
)

df["Month"] = (
    df["InvoiceDate"]
    .dt.to_period("M")
    .astype(str)
)

monthly_sales = (
    df.groupby("Month")["Revenue"]
    .sum()
)

st.subheader(
    "📈 Monthly Revenue Trend"
)

st.line_chart(monthly_sales)

# ---------------------------------
# DATA PREVIEW
# ---------------------------------

st.subheader(
    "📋 Dataset Preview"
)

st.dataframe(
    df.head(20)
)