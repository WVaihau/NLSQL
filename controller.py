import model as md
import pandas as pd
import streamlit as st
from vanna.remote import VannaDefault


def run_sql(sql: str) -> pd.DataFrame:
    """Take in SQL query as string and return DataFrame."""
    conn = md.db_connexion
    st.toast('Connexion SQLite [OK]')

    df = pd.read_sql_query(
        sql,
        conn
    )
    return df

def get_agent():
    """Return vanna agent."""
    vn = VannaDefault(
        model=st.secrets.vanna.model,
        api_key=st.secrets.vanna.api_key
        )
    vn.run_sql = run_sql
    vn.run_sql_is_set = True

    st.toast('Vanna Agent [OK]')
    return vn


def read_readme_file():
    with open(md.readme, 'r') as file:
        content = file.read()
    return content


def setup():
    """Setup all necessary variables."""

    if "vn" not in st.session_state or \
            st.session_state["vn"] is None:
        st.session_state["vn"] = get_agent()
