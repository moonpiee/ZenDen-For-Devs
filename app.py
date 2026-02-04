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
                border: 1px solid #303030 !important;
                font-size: 0.9rem;
                padding: 0.3rem 0.8rem;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )
        st.markdown('<div class="exit-button-container"></div>', unsafe_allow_html=True)

def page_green():
    """Calming green mode - easy on the eyes"""
    css_key = f"green_style_{st.session_state.get('green_toggle', False)}"
    if st.session_state.green_toggle:
        st.markdown(
            f"""
            <style key="{css_key}">
            body, div[data-testid="stAppViewContainer"], section.main, .main .block-container {{
                background: linear-gradient(135deg, #1e4d2b 0%, #2d5a3d 50%, #1e4d2b 100%) !important;
                color: #2d5a3d !important;
                border: none !important;
                box-shadow: none !important;
                padding: 0 !important;
                animation: gentlePulse 8s ease-in-out infinite;
            }}
            @keyframes gentlePulse {{
                0%, 100% {{ opacity: 1; }}
                50% {{ opacity: 0.85; }}
            }}
            header[data-testid="stHeader"], footer {{
                display: none !important;
            }}
            .zen-message {{
                position: fixed;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%);
                color: rgba(144, 238, 144, 0.3);
                font-size: 1.2rem;
                font-style: italic;
                text-align: center;
                z-index: 1;
            }}
            </style>
            <div class="zen-message">Let your eyes rest...</div>
            """,
            unsafe_allow_html=True
        )

def page_clouds():
    """Drifting clouds animation"""
    css_key = f"clouds_style_{st.session_state.get('clouds_toggle', False)}"
    if st.session_state.clouds_toggle:
        st.markdown(
            f"""
            <style key="{css_key}">
            body, div[data-testid="stAppViewContainer"], section.main, .main .block-container {{
                background: linear-gradient(180deg, #87CEEB 0%, #E0F6FF 100%) !important;
                color: transparent !important;
                border: none !important;
                box-shadow: none !important;
                padding: 0 !important;
                overflow: hidden !important;
            }}
            header[data-testid="stHeader"], footer {{
                display: none !important;
            }}
            .cloud {{
                position: fixed;
                background: rgba(255, 255, 255, 0.8);
                border-radius: 100px;
                animation: drift linear infinite;
            }}
            .cloud:before, .cloud:after {{
                content: '';
                position: absolute;
                background: rgba(255, 255, 255, 0.8);
                border-radius: 100px;
            }}
            .cloud1 {{
                width: 100px;
                height: 40px;
                top: 20%;
                left: -100px;
                animation-duration: 35s;
            }}
            .cloud1:before {{
                width: 50px;
                height: 50px;
                top: -25px;
                left: 10px;
            }}
            .cloud1:after {{
                width: 60px;
                height: 40px;
                top: -15px;
                right: 10px;
            }}
            .cloud2 {{
                width: 120px;
                height: 50px;
                top: 50%;
                left: -120px;
                animation-duration: 45s;
                animation-delay: 5s;
            }}
            .cloud2:before {{
                width: 60px;
                height: 60px;
                top: -30px;
                left: 15px;
            }}
            .cloud2:after {{
                width: 70px;
                height: 50px;
                top: -20px;
                right: 15px;
            }}
            .cloud3 {{
                width: 80px;
                height: 35px;
                top: 70%;
                left: -80px;
                animation-duration: 40s;
                animation-delay: 10s;
            }}
            .cloud3:before {{
                width: 40px;
                height: 40px;
                top: -20px;
                left: 10px;
            }}
            .cloud3:after {{
                width: 50px;
                height: 35px;
                top: -15px;
                right: 10px;
            }}
            @keyframes drift {{
                from {{ transform: translateX(0); }}
                to {{ transform: translateX(calc(100vw + 200px)); }}
            }}
            </style>
            <div class="cloud cloud1"></div>
            <div class="cloud cloud2"></div>
            <div class="cloud cloud3"></div>
            """,
            unsafe_allow_html=True
        )

def page_breathe():
    """Box breathing animation - 4-4-4-4 pattern"""
    css_key = f"breathe_style_{st.session_state.get('breathe_toggle', False)}"
    if st.session_state.breathe_toggle:
        st.markdown(
            f"""
            <style key="{css_key}">
            body, div[data-testid="stAppViewContainer"], section.main, .main .block-container {{
                background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%) !important;
                color: transparent !important;
                border: none !important;
                box-shadow: none !important;
                padding: 0 !important;
                overflow: hidden !important;
            }}
            header[data-testid="stHeader"], footer {{
                display: none !important;
            }}
            .breathing-container {{
                position: fixed;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%);
                display: flex;
                flex-direction: column;
                align-items: center;
                z-index: 1;
            }}
            .breathing-circle {{
                width: 120px;
                height: 120px;
                border: 3px solid rgba(100, 200, 255, 0.6);
                border-radius: 50%;
                animation: breathe 16s ease-in-out infinite;
                box-shadow: 0 0 30px rgba(100, 200, 255, 0.4);
            }}
            @keyframes breathe {{
                0%, 100% {{
                    transform: scale(1);
                    border-color: rgba(100, 200, 255, 0.6);
                }}
                25% {{
                    transform: scale(2);
                    border-color: rgba(100, 200, 255, 0.9);
                }}
                50% {{
                    transform: scale(2);
                    border-color: rgba(100, 200, 255, 0.6);
                }}
                75% {{
                    transform: scale(1);
                    border-color: rgba(100, 200, 255, 0.4);
                }}
            }}
            .breathing-text {{
                margin-top: 100px;
                font-size: 1.5rem;
                color: rgba(100, 200, 255, 0.7);
                font-weight: 300;
                letter-spacing: 2px;
                animation: breatheText 16s ease-in-out infinite;
            }}
            @keyframes breatheText {{
                0%, 100% {{ opacity: 0.5; }}
                12.5% {{ opacity: 1; content: 'Breathe In'; }}
                25% {{ opacity: 0.5; }}
                37.5% {{ opacity: 1; content: 'Hold'; }}
                50% {{ opacity: 0.5; }}
                62.5% {{ opacity: 1; content: 'Breathe Out'; }}
                75% {{ opacity: 0.5; }}
                87.5% {{ opacity: 1; content: 'Hold'; }}
            }}
            .breathing-text::before {{
                content: 'Breathe In';
                animation: cycleText 16s ease-in-out infinite;
            }}
            @keyframes cycleText {{
                0%, 24.99% {{ content: 'Breathe In'; }}
                25%, 49.99% {{ content: 'Hold'; }}
                50%, 74.99% {{ content: 'Breathe Out'; }}
                75%, 100% {{ content: 'Hold'; }}
            }}
            </style>
            <div class="breathing-container">
                <div class="breathing-circle"></div>
                <div class="breathing-text"></div>
            </div>
            """,
            unsafe_allow_html=True
        )

# Initialize session state
if 'void_toggle' not in st.session_state:
    st.session_state.void_toggle = False
if 'green_toggle' not in st.session_state:
    st.session_state.green_toggle = False
if 'clouds_toggle' not in st.session_state:
    st.session_state.clouds_toggle = False
if 'breathe_toggle' not in st.session_state:
    st.session_state.breathe_toggle = False

# Check if any mode is active
any_mode_active = (st.session_state.void_toggle or 
                   st.session_state.green_toggle or 
                   st.session_state.clouds_toggle or 
                   st.session_state.breathe_toggle)

# Only show toggles if no mode is active
if not any_mode_active:
    st.markdown("### Choose Your Zen Mode")
    
    col1, col2 = st.columns(2)
    
    with col1:
        void_toggle = st.toggle(
            "⚫ The Void",
            key="enable_void",
            value=st.session_state.void_toggle,
            help="Pure black nothingness. Stare into the void."
        )
        
        clouds_toggle = st.toggle(
            "☁️ Watch Clouds",
            key="enable_clouds",
            value=st.session_state.clouds_toggle,
            help="Gentle drifting clouds across a blue sky."
        )
    
    with col2:
        green_toggle = st.toggle(
            "🌿 Stare at Green",
            key="enable_green",
            value=st.session_state.green_toggle,
            help="Calming green hues, easy on your tired eyes."
        )
        
        breathe_toggle = st.toggle(
            "🫁 Breathe",
            key="enable_breathe",
            value=st.session_state.breathe_toggle,
            help="Box breathing exercise - follow the expanding circle."
        )
    
    # Update session state
    st.session_state.void_toggle = void_toggle
    st.session_state.green_toggle = green_toggle
    st.session_state.clouds_toggle = clouds_toggle
    st.session_state.breathe_toggle = breathe_toggle
else:
    # Show single toggle for the active mode
    if st.session_state.void_toggle:
        void_toggle = st.toggle(
            "⚫ Exit The Void",
            key="exit_void",
            value=True,
            help="Click to return to mode selection"
        )
        st.session_state.void_toggle = void_toggle
        
    elif st.session_state.green_toggle:
        green_toggle = st.toggle(
            "🌿 Exit Green Mode",
            key="exit_green",
            value=True,
            help="Click to return to mode selection"
        )
        st.session_state.green_toggle = green_toggle
        
    elif st.session_state.clouds_toggle:
        clouds_toggle = st.toggle(
            "☁️ Exit Cloud Mode",
            key="exit_clouds",
            value=True,
            help="Click to return to mode selection"
        )
        st.session_state.clouds_toggle = clouds_toggle
        
    elif st.session_state.breathe_toggle:
        breathe_toggle = st.toggle(
            "🫁 Exit Breathing Mode",
            key="exit_breathe",
            value=True,
            help="Click to return to mode selection"
        )
        st.session_state.breathe_toggle = breathe_toggle

# Render the appropriate page
if st.session_state.void_toggle:
    page_void()
elif st.session_state.green_toggle:
    page_green()
elif st.session_state.clouds_toggle:
    page_clouds()
elif st.session_state.breathe_toggle:
    page_breathe()
else:
    main_page()
