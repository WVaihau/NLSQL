import streamlit as st
import controller as ctrl

st.set_page_config(
    page_title="NLSQL",
    page_icon="🇵🇫",
)

def main():
    """Main."""
    with st.spinner('Setting up..'):
        ctrl.setup()

    st.markdown(
        ctrl.read_readme_file()
    )


if __name__ == "__main__":
    main()