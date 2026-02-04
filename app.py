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
    
    # Show some info about each mode
    st.markdown("### Available Modes")
    st.markdown("""
    - **⚫ The Void** - Pure black nothingness
    - **🌿 Stare at Green** - Calming green hues
    - **☁️ Watch Clouds** - Gentle drifting clouds
    - **🌧️ Listen to Rain** - Ambient rain sounds
    """)
    
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

def page_rain():
    """Rain ambience with visual"""
    css_key = f"rain_style_{st.session_state.get('rain_toggle', False)}"
    if st.session_state.rain_toggle:
        # Generate random raindrops
        raindrops = []
        for i in range(30):
            left = random.randint(0, 100)
            duration = random.uniform(0.5, 1.5)
            delay = random.uniform(0, 2)
            raindrops.append(f"""
                <div class="raindrop" style="
                    left: {left}%;
                    animation-duration: {duration}s;
                    animation-delay: {delay}s;
                "></div>
            """)
        
        st.markdown(
            f"""
            <style key="{css_key}">
            body, div[data-testid="stAppViewContainer"], section.main, .main .block-container {{
                background: linear-gradient(180deg, #2c3e50 0%, #34495e 100%) !important;
                color: transparent !important;
                border: none !important;
                box-shadow: none !important;
                padding: 0 !important;
                overflow: hidden !important;
            }}
            header[data-testid="stHeader"], footer {{
                display: none !important;
            }}
            .raindrop {{
                position: fixed;
                top: -10px;
                width: 2px;
                height: 50px;
                background: linear-gradient(transparent, rgba(174, 194, 224, 0.6));
                animation: fall linear infinite;
            }}
            @keyframes fall {{
                to {{ transform: translateY(100vh); }}
            }}
            .rain-message {{
                position: fixed;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%);
                color: rgba(174, 194, 224, 0.4);
                font-size: 1.1rem;
                font-style: italic;
                text-align: center;
            }}
            </style>
            {''.join(raindrops)}
            <div class="rain-message">Listen to the rain...<br/><small>(imagine the sound)</small></div>
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
if 'rain_toggle' not in st.session_state:
    st.session_state.rain_toggle = False

# Create toggle for mode selection
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
    
    rain_toggle = st.toggle(
        "🌧️ Listen to Rain",
        key="enable_rain",
        value=st.session_state.rain_toggle,
        help="Ambient rain (visual for now, imagine the sound)."
    )

# Only allow one mode at a time
if sum([void_toggle, green_toggle, clouds_toggle, rain_toggle]) > 1:
    st.warning("⚠️ Please select only one mode at a time.")
    st.session_state.void_toggle = False
    st.session_state.green_toggle = False
    st.session_state.clouds_toggle = False
    st.session_state.rain_toggle = False
else:
    st.session_state.void_toggle = void_toggle
    st.session_state.green_toggle = green_toggle
    st.session_state.clouds_toggle = clouds_toggle
    st.session_state.rain_toggle = rain_toggle

# Render the appropriate page
if st.session_state.void_toggle:
    page_void()
elif st.session_state.green_toggle:
    page_green()
elif st.session_state.clouds_toggle:
    page_clouds()
elif st.session_state.rain_toggle:
    page_rain()
else:
    main_page()
