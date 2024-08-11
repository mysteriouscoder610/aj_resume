import streamlit as st
from PIL import Image

# Set the layout of the page
st.set_page_config(layout="wide")

# Initialize session state to track the current section
if 'current_section' not in st.session_state:
    st.session_state.current_section = 'Profile'

# Create three columns: left column, spacer, and right column
left_column, spacer, right_column = st.columns([1, 0.1, 4])

# Custom CSS to style the buttons to look like resume sections
st.markdown("""
    <style>
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
    </style>
""", unsafe_allow_html=True)


# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([6,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

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
       st.markdown('''
        ## Education
        ''')
       
       txt('**Doctor of Philosophy** (Medical Technology), *Mahidol University*, Thailand',
            '2002-2006')
       txt('Third year Information Technology student pursuing B.Tech from **Kamla Nehru Institute of Technology**, Sultanpur','CGPA:`8.7`')
    elif st.session_state.current_section == 'Experience':
        st.write("## EXPERIENCE")
        st.write("This section showcases the user's work experience. Include job titles, companies, years of work, and responsibilities.")
    elif st.session_state.current_section == 'Education':
        st.write("## ACHIEVEMENTS")
        st.write("This section covers the user's educational background. Include degrees, institutions, years attended, and honors.")
    elif st.session_state.current_section == 'Skills':
        st.write("## SKILLS")
        st.write("This section highlights the user's skills. List out technical, interpersonal, and other relevant skills.")
