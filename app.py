import streamlit as st
from PIL import Image
from OCR import ImageToSpeechConverter
from scene_understanding import scene_understanding
from navigation import object_detection
from assistance import provide_task_assistance
import streamlit.components.v1 as components
from streamlit_option_menu import option_menu

# Configure the page with light theme
st.set_page_config(
    page_title="AI Assistive App",
    page_icon="👁️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for light theme and better visibility
st.markdown("""
<style>
    /* Main background and text colors */
    .stApp {
        background-color: #ffffff;
        color: #333333;
    }
    
    /* Sidebar styling */
    .css-1d391kg {
        background-color: #f0f2f6;
    }
    
    /* Header styling */
    h1, h2, h3 {
        color: #1f1f1f;
        font-weight: 600;
    }
    
    /* Cards and containers */
    div.css-1r6slb0 {
        background-color: #ffffff;
        border: 1px solid #e0e0e0;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    /* Button styling */
    .stButton>button {
        background-color: #4A90E2;
        color: white;
        border-radius: 10px;
        padding: 0.5rem 1rem;
        border: none;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    /* File uploader */
    .uploadedFile {
        background-color: #f8f9fa;
        border: 2px dashed #4A90E2;
        border-radius: 10px;
        padding: 20px;
    }
    
    /* Alert boxes */
    .stAlert {
        background-color: #ffffff;
        border: 1px solid #e0e0e0;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    /* Menu items */
    .nav-link {
        background-color: #ffffff !important;
        color: #333333 !important;
        border-radius: 5px !important;
        margin: 5px 0 !important;
    }
    
    .nav-link:hover {
        background-color: #f0f2f6 !important;
    }
    
    .nav-link-selected {
        background-color: #4A90E2 !important;
        color: #ffffff !important;
    }
</style>
""", unsafe_allow_html=True)

# Header with improved visibility
st.markdown("""
    <div style='background-color: #ffffff; padding: 1.5rem; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);'>
        <div style='display: flex; align-items: center;'>
            <img src='https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/eye.svg' style='width: 50px; margin-right: 20px;'>
            <div>
                <h1 style='color: #1f1f1f; margin: 0;'>🌟 AI-Powered Assistive Application</h1>
                <p style='color: #666666; font-size: 1.2em; margin-top: 10px;'>
                    Empowering vision through artificial intelligence - Your digital eyes to the world.
                </p>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# Sidebar with improved contrast
with st.sidebar:
    st.markdown("""
        <div style='background-color: #ffffff; padding: 1rem; border-radius: 10px; margin-bottom: 20px;'>
            <h3 style='color: #1f1f1f; margin: 0;'>🎯 Features</h3>
        </div>
    """, unsafe_allow_html=True)
    
    selected_feature = option_menu(
        menu_title=None,
        options=[
            "Real-Time Scene Understanding",
            "Text-to-Speech Conversion (OCR)",
            "Object and Obstacle Detection",
            "Personalized Assistance"
        ],
        icons=['camera-fill', 'chat-dots-fill', 'map-fill', 'person-workspace'],
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {"padding": "0!important", "background-color": "#ffffff"},
            "icon": {"color": "#4A90E2", "font-size": "20px"},
            "nav-link": {
                "font-size": "16px",
                "text-align": "left",
                "margin": "5px 0",
                "padding": "10px 15px",
                "border-radius": "5px",
                "background-color": "#ffffff",
                "color": "#333333"
            },
            "nav-link-selected": {
                "background-color": "#4A90E2",
                "color": "#ffffff"
            },
        }
    )

# Main content area with improved visibility
main_container = st.container()
with main_container:
    # File uploader section
    st.markdown("""
        <div style='background-color: #ffffff; padding: 1.5rem; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); margin-bottom: 2rem;'>
            <h3 style='color: #1f1f1f;'>📤 Upload Image</h3>
        </div>
    """, unsafe_allow_html=True)
    
    uploaded_file = st.file_uploader(
        "Choose an image file:",
        type=["png", "jpg", "jpeg"],
        help="Supported formats: PNG, JPG, JPEG"
    )

    if uploaded_file:
        # Image display and processing sections
        col1, col2 = st.columns([2, 1])
        with col1:
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded Image", use_container_width=True)
        
        with col2:
            st.markdown("""
                <div style='background-color: #f8f9fa; padding: 1rem; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);'>
                    <h4 style='color: #1f1f1f;'>📋 Image Details</h4>
                    <ul style='color: #333333;'>
                        <li>Format: {}</li>
                        <li>Size: {}x{}</li>
                    </ul>
                </div>
            """.format(image.format, image.size[0], image.size[1]), unsafe_allow_html=True)

        # Feature processing section with improved visibility
        st.markdown(f"""
            <div style='background-color: #ffffff; padding: 1.5rem; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); margin-top: 2rem;'>
                <h2 style='color: #1f1f1f;'>🔍 {selected_feature}</h2>
            </div>
        """, unsafe_allow_html=True)

        # Process the selected feature
        if selected_feature == "Real-Time Scene Understanding":
            with st.spinner("🔄 Analyzing the scene..."):
                try:
                    description = scene_understanding(image)
                    st.success("Analysis Complete!")
                    st.markdown("""
                        <div style='background-color: #f8f9fa; padding: 1rem; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);'>
                            <h3 style='color: #1f1f1f;'>📝 Scene Description:</h3>
                            <p style='color: #333333;'>{}</p>
                        </div>
                    """.format(description), unsafe_allow_html=True)
                except Exception as e:
                    st.error(f"❌ Error: {e}")


        elif selected_feature == "Text-to-Speech Conversion (OCR)":
            with st.spinner("🔄 Extracting text and converting to speech..."):
                try:
                    converter = ImageToSpeechConverter()
                    text = converter.extract_text(uploaded_file)
                    
                    if text:
                        st.success("Text Extraction Complete!")
                        st.markdown("### 📑 Extracted Text:")
                        st.markdown(f"""
                            <div style='background-color: #f8f9fa; padding: 1rem; border-radius: 10px;'>
                                {text}
                            </div>
                        """, unsafe_allow_html=True)
                        st.info("🔊 Playing audio...")
                        converter.text_to_speech(text)
                    else:
                        st.warning("📢 No text detected in the image.")
                except Exception as e:
                    st.error(f"❌ Error: {e}")

        elif selected_feature == "Object and Obstacle Detection":
            with st.spinner("🔄 Detecting objects and obstacles..."):
                try:
                    navigation_guidance = object_detection(image)
                    st.success("Detection Complete!")
                    st.markdown("### 🚸 Navigation Guidance:")
                    st.markdown(f"""
                        <div style='background-color: #f8f9fa; padding: 1rem; border-radius: 10px;'>
                            {navigation_guidance}
                        </div>
                    """, unsafe_allow_html=True)
                except Exception as e:
                    st.error(f"❌ Error: {e}")

        elif selected_feature == "Personalized Assistance":
            st.markdown("### 🎯 Select Task Type")
            task_type = st.selectbox(
                "Choose a task:",
                ["item_identification", "label_reading", "navigation_help", "daily_tasks"],
                format_func=lambda x: {
                    "item_identification": "🔍 Item Identification",
                    "label_reading": "📝 Label Reading",
                    "navigation_help": "🧭 Navigation Help",
                    "daily_tasks": "📋 Daily Tasks"
                }[x]
            )
            
            with st.spinner("🔄 Providing assistance..."):
                try:
                    assistance = provide_task_assistance(image, task_type)
                    st.success("Analysis Complete!")
                    st.markdown("### 📋 Assistance Report:")
                    st.markdown(f"""
                        <div style='background-color: #f8f9fa; padding: 1rem; border-radius: 10px;'>
                            {assistance}
                        </div>
                    """, unsafe_allow_html=True)
                except Exception as e:
                    st.error(f"❌ Error: {e}")

    else:
        st.markdown("""
            <div style='text-align: center; padding: 3rem; background-color: #f8f9fa; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);'>
                <h3 style='color: #1f1f1f;'>👆 Please upload an image to get started</h3>
                <p style='color: #666666;'>Supported formats: PNG, JPG, JPEG</p>
            </div>
        """, unsafe_allow_html=True)



# Footer section
st.markdown("""
    <div style='text-align: center; padding: 1rem; background-color: #ffffff; border-top: 1px solid #e0e0e0; margin-top: 2rem;'>
        <p style='color: #666666;'>Made with ❤️ for Accessibility</p>
        <h4>📫 Contact</h4>
        <p style='color: #333333;'>For issues or suggestions, please contact:</p>
        <p style='color: #4A90E2; font-weight: bold;'>
            <a href="mailto:tannaprasanthkumar76@gmail.com" style='text-decoration: none;'>tannaprasanthkumar76@gmail.com</a>
        </p>
        <p>
            <a href="https://github.com/TannaPrasanthkumar/VisionAssist" target="_blank" style='color: #4A90E2; text-decoration: none;'>
                🌐 View on GitHub
            </a>
        </p>
    </div>
""", unsafe_allow_html=True)
