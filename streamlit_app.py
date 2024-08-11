import streamlit as st
from PIL import Image
# Set the layout of the page
st.set_page_config(layout="wide")

# Initialize session state to track the current section
if 'current_section' not in st.session_state:
    st.session_state.current_section = 'Profile'

# Create two columns, with the left column taking 25% of the width and the right column 75%
left_column, right_column = st.columns([1, 4])

# Custom CSS to style the buttons to look like resume sections
st.markdown("""
    <style>
    div[data-testid="column"]:nth-of-type(1) {
        background-color: lightblue;
        height: 100vh;
        padding: 10px;
        display: flex;
    }
    .stButton > button {
        width: 100%;
        margin-bottom: 10px;
        background-color: black;
        color: white;
        border: 2px solid black;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 16px;
        text-transform: uppercase;
        cursor: pointer;
        transition: background-color 0.3s, border-color 0.3s;
    }

    .stButton > button:hover {
        background-color: white;
        color: blue;
        border: 2px solid black;
    }

    .stButton > button:active {
        background-color: blue;
        color: black;
        border: 2px solid blue;
    }
    </style>
""", unsafe_allow_html=True)

# Add buttons to the left column (like a resume section)
with left_column:
    image = Image.open('ayush.jpg')
    st.image(image, width=200)
    st.write("# AYUSH JHA")
    if st.button("EDUCATION"):
        st.session_state.current_section = 'Profile'
    if st.button("EXPERIENCE"):
        st.session_state.current_section = 'Experience'
    if st.button("ACHIEVEMENTS"):
        st.session_state.current_section = 'Education'
    if st.button("SKILLS"):
        st.session_state.current_section = 'Skills'

# Content in the right column based on the selected section
with right_column:
    if st.session_state.current_section == 'Profile':
        st.write("## EDUCATION")
        st.markdown('''
    - GPA: :blue[`3.89`]
        - Research
        - thesis entitled `Computer-aided molecular design for biological and chemical applications : Quantum chemical and machine learning approach`.
    - Received Royal Golden Jubilee Ph.D. Scholarship of `2.152 million THB` covering tuition and stipend.
    - Thesis awarded `1st` Prize by the National Research Council of Thailand.
    ''')
    elif st.session_state.current_section == 'Experience':
        st.write("## EXPERIENCE")
        st.write("This section showcases the user's work experience. Include job titles, companies, years of work, and responsibilities.")
    elif st.session_state.current_section == 'Education':
        st.write("## ACHIEVEMENTS")
        st.write("This section covers the user's educational background. Include degrees, institutions, years attended, and honors.")
    elif st.session_state.current_section == 'Skills':
        st.write("## SKILLS")
        st.write("This section highlights the user's skills. List out technical, interpersonal, and other relevant skills.")
