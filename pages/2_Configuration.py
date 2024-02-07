import streamlit as st
import model as md
import pandas as pd

vn = st.session_state["vn"]

"# Configuration"

"## Vanna Agent"

f"Model: **{st.secrets.vanna.model}**"

"Training data:"
train_data = st.session_state["vn"].get_training_data()
st.write(
    train_data[train_data["training_data_type"]=="ddl"][
        ["id",
        "training_data_type",
        "content"]
    ]
)

"## SQLite"
tables = ["Contacts", "Messages"]

for table in tables:
    f"### Table {table}"
    st.write(pd.read_sql_query(
        f"SELECT * FROM {table}",
        md.db_connexion
    ))