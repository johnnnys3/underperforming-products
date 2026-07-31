import streamlit as st
import pandas as pd
import sqlite3

st.set_page_config(page_title="Underperforming Products", layout="wide")
st.title("Underperforming Products by Region")

conn = sqlite3.connect('superstore.db')
df = pd.read_sql("SELECT * FROM orders", conn)

regions = sorted(df['Region'].unique())
selected_region = st.sidebar.selectbox("Select Region", ["All"] + regions)

if selected_region != "All":
    filtered = df[df['Region'] == selected_region]
else:
    filtered = df

summary = (
    filtered.groupby(['Region', 'Sub-Category'])
    .agg(total_sales=('Sales', 'sum'), total_profit=('Profit', 'sum'), order_count=('Sales', 'count'))
    .reset_index()
)
summary['profit_margin_pct'] = (100 * summary['total_profit'] / summary['total_sales']).round(2)
summary = summary[summary['order_count'] >= 3]
summary = summary.sort_values('total_profit')

st.subheader("Underperforming Sub-Categories")
st.dataframe(summary.head(15))

st.subheader("Total Profit by Sub-Category")
chart_data = summary.head(15).set_index('Region')['total_profit']
st.bar_chart(chart_data)