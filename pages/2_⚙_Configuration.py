import streamlit as st
import controller as ctrl
import pandas as pd
import vanna as vn

"# Configuration"

"## Vanna Agent"

f"Model: **{st.secrets.vanna.model}**"

"Training data:"
train_data = vn.get_training_data()
st.write(
    train_data[train_data["training_data_type"]=="ddl"][
        ["id",
        "training_data_type",
        "content"]
    ]
)

"## SQLite"
st.write(
    ctrl.run_sql(
        "SELECT name FROM sqlite_master;"
    )
)

tables = ["Contacts", "Messages"]
for table in tables:
    f"### Table {table}"
    st.write(ctrl.run_sql(
        f"SELECT * FROM {table}"
    ))