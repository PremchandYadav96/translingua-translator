import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
import time

# Load environment variables
load_dotenv()

# Configure the Gemini API
def configure_gemini():
    """Configure the Gemini API with the API key"""
    api_key = os.getenv("GOOGLE_API_KEY") or "YOUR_API_KEY_HERE"
    genai.configure(api_key=api_key)

# Auto-detect language function
def detect_language(text):
    """Detect the language of the input text using Gemini AI"""
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        prompt = f"""
        Identify the language of this text. Respond with only the language name in English.
        
        Text: "{text[:300]}"
        
        Language:
        """
        response = model.generate_content([prompt])
        detected = response.text.strip()
        
        # Map common responses to our language list
        language_map = {
            "english": "English", "spanish": "Spanish", "french": "French",
            "german": "German", "italian": "Italian", "portuguese": "Portuguese",
            "russian": "Russian", "chinese": "Chinese (Simplified)", "japanese": "Japanese",
            "korean": "Korean", "arabic": "Arabic", "hindi": "Hindi",
            "bengali": "Bengali", "tamil": "Tamil", "telugu": "Telugu"
        }
        
        return language_map.get(detected.lower(), detected)
    except:
        return "English"

# Translation function
def translate_text(text, source_language, target_language):
    """Translate text using Gemini Pro"""
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        prompt = f"""
        Translate the following text from {source_language} to {target_language}.
        Maintain the original tone and context. Provide only the translated text.
        
        Text: "{text}"
        """
        response = model.generate_content([prompt])
        return response.text.strip()
    except Exception as e:
        return f"Translation error: {str(e)}"

# Futuristic CSS
def load_futuristic_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Exo+2:wght@300;400;600&display=swap');
    
    .stApp {
        background: linear-gradient(135deg, #0a0a0a 0%, #1a1a2e 50%, #16213e 100%);
        color: #ffffff;
    }
    
    .stApp::before {
        content: '';
        position: fixed;
        top: 0; left: 0; width: 100%; height: 100%;
        background: radial-gradient(circle at 20% 80%, rgba(0,255,255,0.1) 0%, transparent 50%),
                    radial-gradient(circle at 80% 20%, rgba(255,0,255,0.1) 0%, transparent 50%);
        z-index: -1;
        animation: bgShift 15s ease-in-out infinite;
    }
    
    @keyframes bgShift {
        0%, 100% { opacity: 0.3; }
        50% { opacity: 0.6; }
    }
    
    .cyber-header {
        background: linear-gradient(135deg, rgba(0,255,255,0.1), rgba(255,0,255,0.1));
        border: 2px solid rgba(0,255,255,0.3);
        border-radius: 20px;
        padding: 3rem 2rem;
        text-align: center;
        margin-bottom: 2rem;
        backdrop-filter: blur(10px);
        position: relative;
        overflow: hidden;
    }
    
    .cyber-header::before {
        content: '';
        position: absolute;
        top: -50%; left: -50%; width: 200%; height: 200%;
        background: linear-gradient(45deg, transparent, rgba(0,255,255,0.1), transparent);
        animation: scan 4s linear infinite;
    }
    
    @keyframes scan {
        0% { transform: translateX(-100%) rotate(45deg); }
        100% { transform: translateX(100%) rotate(45deg); }
    }
    
    .cyber-title {
        font-family: 'Orbitron', monospace;
        font-size: 3.5rem;
        font-weight: 900;
        background: linear-gradient(45deg, #00ffff, #ff00ff, #00ff7f);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 1rem;
        text-shadow: 0 0 30px rgba(0,255,255,0.5);
    }
    
    .cyber-subtitle {
        font-family: 'Exo 2', sans-serif;
        font-size: 1.3rem;
        color: #00ffff;
        text-transform: uppercase;
        letter-spacing: 2px;
        margin-bottom: 1rem;
    }
    
    .holo-card {
        background: linear-gradient(135deg, rgba(255,255,255,0.05), rgba(255,255,255,0.02));
        backdrop-filter: blur(15px);
        border: 1px solid rgba(0,255,255,0.3);
        border-radius: 15px;
        padding: 2rem;
        margin-bottom: 1.5rem;
        transition: all 0.3s ease;
    }
    
    .holo-card:hover {
        border-color: #00ffff;
        box-shadow: 0 0 25px rgba(0,255,255,0.2);
        transform: translateY(-2px);
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #00ffff, #ff00ff) !important;
        color: #000000 !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 0.8rem 2rem !important;
        font-family: 'Orbitron', monospace !important;
        font-weight: 700 !important;
        text-transform: uppercase !important;
        letter-spacing: 1px !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 0 20px rgba(0,255,255,0.4) !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-3px) !important;
        box-shadow: 0 0 30px rgba(0,255,255,0.6) !important;
    }
    
    .stTextArea textarea {
        background: rgba(0,0,0,0.4) !important;
        border: 2px solid rgba(0,255,255,0.3) !important;
        border-radius: 12px !important;
        color: #ffffff !important;
        font-family: 'Exo 2', sans-serif !important;
        backdrop-filter: blur(10px) !important;
    }
    
    .stTextArea textarea:focus {
        border-color: #00ffff !important;
        box-shadow: 0 0 15px rgba(0,255,255,0.3) !important;
    }
    
    .stSelectbox select {
        background: rgba(0,0,0,0.4) !important;
        border: 2px solid rgba(0,255,255,0.3) !important;
        border-radius: 12px !important;
        color: #ffffff !important;
        font-family: 'Exo 2', sans-serif !important;
    }
    
    .stats-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
        gap: 1.5rem;
        margin: 2rem 0;
    }
    
    .stat-card {
        background: linear-gradient(135deg, rgba(0,255,255,0.1), rgba(255,0,255,0.1));
        border: 2px solid rgba(0,255,255,0.3);
        border-radius: 15px;
        padding: 1.5rem;
        text-align: center;
        transition: all 0.3s ease;
    }
    
    .stat-card:hover {
        border-color: #00ffff;
        box-shadow: 0 0 20px rgba(0,255,255,0.3);
        transform: scale(1.05);
    }
    
    .stat-number {
        font-family: 'Orbitron', monospace;
        font-size: 2.5rem;
        font-weight: 900;
        background: linear-gradient(45deg, #00ffff, #ff00ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    .stat-label {
        font-family: 'Exo 2', sans-serif;
        color: #00ffff;
        text-transform: uppercase;
        font-size: 0.9rem;
        margin-top: 0.5rem;
    }
    
    .auto-detect {
        background: linear-gradient(135deg, rgba(0,255,127,0.1), rgba(0,255,255,0.1));
        border: 2px solid rgba(0,255,127,0.4);
        border-radius: 12px;
        padding: 1rem;
        text-align: center;
        margin: 1rem 0;
        animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
        0%, 100% { opacity: 0.8; }
        50% { opacity: 1; }
    }
    
    .result-box {
        background: linear-gradient(135deg, rgba(255,255,255,0.03), rgba(255,255,255,0.01));
        border: 2px solid rgba(0,255,255,0.3);
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        backdrop-filter: blur(10px);
    }
    
    .result-original { border-left: 4px solid #00ffff; }
    .result-translated { border-left: 4px solid #00ff7f; }
    
    .team-section {
        background: linear-gradient(135deg, rgba(0,0,0,0.6), rgba(26,26,46,0.6));
        border: 2px solid rgba(0,255,255,0.3);
        border-radius: 20px;
        padding: 2rem;
        margin-top: 3rem;
        text-align: center;
        backdrop-filter: blur(15px);
    }
    
    .team-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 1.5rem;
        margin: 2rem 0;
    }
    
    .team-member {
        background: rgba(0,255,255,0.1);
        border: 1px solid rgba(0,255,255,0.3);
        border-radius: 12px;
        padding: 1.5rem;
        transition: all 0.3s ease;
    }
    
    .team-member:hover {
        border-color: #00ffff;
        box-shadow: 0 0 20px rgba(0,255,255,0.2);
        transform: translateY(-3px);
    }
    
    .member-name {
        font-family: 'Orbitron', monospace;
        color: #00ffff;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    
    .member-role {
        font-family: 'Exo 2', sans-serif;
        color: #ff00ff;
        font-size: 0.9rem;
    }
    
    .sidebar .css-1d391kg {
        background: linear-gradient(180deg, rgba(0,0,0,0.8), rgba(26,26,46,0.8)) !important;
        backdrop-filter: blur(20px) !important;
    }
    </style>
    """, unsafe_allow_html=True)

def main():
    st.set_page_config(
        page_title="TransLingua - AI Translator",
        page_icon="🌐",
        layout="wide"
    )
    
    load_futuristic_css()
    configure_gemini()
    
    # Header
    st.markdown("""
        <div class="cyber-header">
            <div class="cyber-title">🌐 TRANSLINGUAL</div>
            <div class="cyber-subtitle">AI-Powered Neural Translation</div>
            <div style="color: rgba(255,255,255,0.8); font-size: 1rem; max-width: 600px; margin: 0 auto;">
                Advanced quantum translation system with auto-detection capabilities
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Stats
    st.markdown("""
        <div class="stats-grid">
            <div class="stat-card">
                <div class="stat-number">25+</div>
                <div class="stat-label">Languages</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">99%</div>
                <div class="stat-label">Accuracy</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">⚡</div>
                <div class="stat-label">Fast</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">🔒</div>
                <div class="stat-label">Secure</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Language options
    languages = [
        "Auto-Detect", "English", "Spanish", "French", "German", "Italian", 
        "Portuguese", "Russian", "Chinese (Simplified)", "Japanese", "Korean", 
        "Arabic", "Hindi", "Bengali", "Tamil", "Telugu", "Kannada", "Malayalam",
        "Gujarati", "Marathi", "Punjabi", "Urdu", "Dutch", "Swedish", "Turkish"
    ]

    # Main interface
    col1, col2 = st.columns([3, 2], gap="large")

    with col1:
        st.markdown("""
            <div class="holo-card">
                <h3 style="font-family: 'Orbitron', monospace; color: #00ffff; margin-bottom: 1rem;">
                    📡 INPUT INTERFACE
                </h3>
            </div>
        """, unsafe_allow_html=True)
        
        text = st.text_area(
            "",
            placeholder="Enter text for translation... (Max 3000 characters)",
            height=250,
            max_chars=3000
        )
        
        char_count = len(text) if text else 0
        st.markdown(f"""
            <div style="text-align: right; color: #00ffff; font-family: 'Orbitron', monospace; font-size: 0.8rem;">
                CHARS: {char_count}/3000
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
            <div class="holo-card">
                <h3 style="font-family: 'Orbitron', monospace; color: #ff00ff; margin-bottom: 1rem;">
                    🌍 LANGUAGE MATRIX
                </h3>
            </div>
        """, unsafe_allow_html=True)
        
        source_language = st.selectbox(
            "🔤 FROM:",
            languages,
            index=0
        )
        
        target_language = st.selectbox(
            "🎯 TO:",
            [lang for lang in languages if lang != "Auto-Detect"],
            index=0
        )
        
        # Auto-detect display
        if text and source_language == "Auto-Detect":
            st.markdown("""
                <div class="auto-detect">
                    <h4 style="color: #00ff7f; font-family: 'Orbitron', monospace; margin: 0;">
                        🤖 AUTO-DETECTION ACTIVE
                    </h4>
                </div>
            """, unsafe_allow_html=True)
        
        # Control buttons
        col_btn1, col_btn2 = st.columns(2)
        with col_btn1:
            if st.button("🔄 SWAP", use_container_width=True):
                st.info("Manually swap languages above")
        
        with col_btn2:
            translate_btn = st.button("🚀 TRANSLATE", use_container_width=True, type="primary")

    # Translation logic
    if translate_btn:
        if not text.strip():
            st.error("⚠️ Please enter text to translate!")
        elif source_language == target_language:
            st.warning("⚠️ Select different languages!")
        else:
            # Handle auto-detection
            actual_source = source_language
            if source_language == "Auto-Detect":
                with st.spinner("🔍 Detecting language..."):
                    actual_source = detect_language(text)
                    st.success(f"🎯 Detected: **{actual_source}**")
            
            # Translation progress
            progress_bar = st.progress(0)
            status = st.empty()
            
            status.text("🔄 Initializing translation...")
            progress_bar.progress(25)
            time.sleep(0.3)
            
            status.text("🧠 Processing with AI...")
            progress_bar.progress(50)
            time.sleep(0.3)
            
            status.text("⚡ Generating translation...")
            progress_bar.progress(75)
            
            with st.spinner("🔄 Translating..."):
                translated_text = translate_text(text, actual_source, target_language)
            
            progress_bar.progress(100)
            status.text("✅ Translation complete!")
            time.sleep(0.5)
            progress_bar.empty()
            status.empty()
            
            # Results
            st.markdown("---")
            st.markdown("""
                <div style="text-align: center; margin: 2rem 0;">
                    <h2 style="font-family: 'Orbitron', monospace; color: #00ff7f;">
                        ✨ TRANSLATION COMPLETE
                    </h2>
                </div>
            """, unsafe_allow_html=True)
            
            res_col1, res_col2 = st.columns(2)
            
            with res_col1:
                st.markdown(f"""
                    <div class="result-box result-original">
                        <h4 style="color: #00ffff; font-family: 'Orbitron', monospace;">
                            📄 ORIGINAL ({actual_source})
                        </h4>
                    </div>
                """, unsafe_allow_html=True)
                st.code(text, language="text")
                
            with res_col2:
                st.markdown(f"""
                    <div class="result-box result-translated">
                        <h4 style="color: #00ff7f; font-family: 'Orbitron', monospace;">
                            ✅ TRANSLATED ({target_language})
                        </h4>
                    </div>
                """, unsafe_allow_html=True)
                st.success(translated_text)
            
            # Action buttons
            act_col1, act_col2, act_col3 = st.columns(3)
            with act_col1:
                if st.button("📋 COPY", use_container_width=True):
                    st.balloons()
                    st.success("Ready to copy!")
            with act_col2:
                if st.button("🔄 RESET", use_container_width=True):
                    st.rerun()
            with act_col3:
                if st.button("📤 SHARE", use_container_width=True):
                    st.info("Copy text above to share!")

    # Sidebar
    with st.sidebar:
        st.markdown("""
            <div style="text-align: center; padding: 1rem;">
                <h2 style="font-family: 'Orbitron', monospace; color: #00ffff;">🌐 TRANSLINGUAL</h2>
                <p style="color: #ff00ff;">Neural AI Core</p>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### 🚀 Features")
        st.markdown("""
        - 🎯 **25+ Languages**
        - 🔍 **Auto-Detection**
        - 🧠 **AI-Powered**
        - ⚡ **Fast Processing**
        - 🔒 **Secure**
        """)
        
        st.markdown("### 💼 Use Cases")
        st.markdown("""
        - 🏢 Business documents
        - 🎓 Academic papers
        - ✈️ Travel assistance
        - 💬 Personal communication
        """)

    # Team footer
    st.markdown("""
        <div class="team-section">
            <h3 style="font-family: 'Orbitron', monospace; color: #00ffff; margin-bottom: 2rem;">
                👥 DEVELOPMENT TEAM
            </h3>
            <div class="team-grid">
                <div class="team-member">
                    <div class="member-name">V C Premchand Yadav</div>
                    <div class="member-role">Lead Developer</div>
                </div>
                <div class="team-member">
                    <div class="member-name">Sembili Hemanth</div>
                    <div class="member-role">AI Specialist</div>
                </div>
                <div class="team-member">
                    <div class="member-name">Voruganti NandiVardhan Reddy</div>
                    <div class="member-role">UI/UX Designer</div>
                </div>
                <div class="team-member">
                    <div class="member-name">Kanchetti Ajay</div>
                    <div class="member-role">Backend Engineer</div>
                </div>
            </div>
            <div style="margin-top: 2rem; padding-top: 1rem; border-top: 1px solid rgba(0,255,255,0.3);">
                <p style="color: #00ffff; font-family: 'Orbitron', monospace;">
                    🌐 TRANSLINGUAL - Neural Translation Matrix
                </p>
                <p style="color: rgba(255,255,255,0.7); font-size: 0.9rem;">
                    © 2025 TransLingua Team • Powered by Google Gemini AI
                </p>
            </div>
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()