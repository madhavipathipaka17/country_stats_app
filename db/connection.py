import streamlit as st
import mysql.connector
import pandas as pd

@st.cache_resource
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Madhu123$",   # change if needed
        database="country_data"
    )

@st.cache_data
def run_query(query):
    conn = get_connection()
    return pd.read_sql(query, conn)