import streamlit as st
import time
import random

st.set_page_config(
    page_title="ZenDen for Devs",
    page_icon="🧘",
    layout="centered",
    initial_sidebar_state="collapsed"
)

def main_page():
    st.title("ZenDen for Devs 🧘💻")
    st.markdown("Welcome! Choose a relaxation mode below.")
    
    st.markdown(
        """
        <style>
        body, div[data-testid="stAppViewContainer"], section.main, .main .block-container {
            background-color: #f0f0f0 !important;
            color: #333 !important;
        }
        header[data-testid="stHeader"], footer {
            display: block !important;
        }
        .main .block-container {
            padding: 2rem !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

def page_void():
    """The original void - pure black"""
    css_key = f"void_style_{st.session_state.get('void_toggle', False)}"
    if st.session_state.void_toggle:
        st.markdown(
            f"""
            <style key="{css_key}">
            body, div[data-testid="stAppViewContainer"], section.main, .main .block-container {{
                background-color: black !important;
                color: black !important;
                border: none !important;
                box-shadow: none !important;
                padding: 0 !important;
            }}
            header[data-testid="stHeader"], footer {{
                display: none !important;
            }}
            .exit-button-container {{
                position: fixed;
                bottom: 30px;
                left: 50%;
                transform: translateX(-50%);
                z-index: 9999;
            }}
            .exit-button-container button {{
                background-color: #181818 !important;
                color: #606060 !important;
