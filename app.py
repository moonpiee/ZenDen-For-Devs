import streamlit as st
import time

st.set_page_config(
    page_title="ZenDen for Devs",
    page_icon="🧘",
    layout="centered",
    initial_sidebar_state="collapsed"
)
def main_page():
    st.title("ZenDen for Devs 🧘💻")
    st.markdown("Welcome! Choose a relaxation module from above.")
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
            .exit-void-button-container {{
                position: fixed;
                bottom: 30px;
                left: 50%;
                transform: translateX(-50%);
                z-index: 9999;
            }}
            .exit-void-button-container button {{
                background-color: #181818 !important;
                color: #606060 !important;
                border: 1px solid #303030 !important;
                font-size: 0.9rem;
                padding: 0.3rem 0.8rem;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )
        st.markdown('<div class="exit-void-button-container"></div>', unsafe_allow_html=True)
    else:
        st.markdown(
            f"""
            <style key="{css_key}">
            body, div[data-testid="stAppViewContainer"], section.main, .main .block-container {{
                background-color: "" !important;
                color: "" !important;
                padding: "" !important;
            }}
            header[data-testid="stHeader"], footer {{
                display: "" !important;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )
page_names_to_funcs = {
    "🏠 Home": main_page,
    "⚫ The Void": page_void,
}

if 'void_toggle' not in st.session_state:
    st.session_state.void_toggle = False

void_toggle = st.toggle(
    "Enable The Void.",
    key="enable_void",
    value=False,
    help="Click to toggle the void screen. This will turn your screen black for a moment, allowing you to take a break from your work."
)
st.session_state.void_toggle = void_toggle
if void_toggle:
    page_void()
else:
    main_page()
