import streamlit as st
import pymysql

pymysql.install_as_MySQLdb()
conn = st.connection("my_database")
df = conn.query("select * from financial_transactions")
st.dataframe(df)
