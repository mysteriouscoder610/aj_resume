import streamlit as st
from PIL import Image

# Set the layout of the page
st.set_page_config(layout="wide")

# Initialize session state to track the current section
if 'current_section' not in st.session_state:
    st.session_state.current_section = 'Profile'

# Custom CSS to style the buttons and apply a gradient background
st.markdown("""
    <style>
    .main {
        background: linear-gradient(to right, #46b8fa,#9ee6ef );
        padding: 20px;
        border-radius: 15px;
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
        display: flex;
        align-items: center;
        justify-content: left;
    }

    .stButton > button:hover {
        background-color: white;
        color: blue;
        border: 2px solid black;
    }

    .stButton > button img {
        margin-right: 10px;
    }

    .centered-text {
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# Custom function for printing text
def txt(a, b):
    col1, col2 = st.columns([6, 1])
    with col1:
        st.markdown(a)
    with col2:
        st.markdown(b)

def txt2(a, b):
    col1, col2 = st.columns([1, 4])
    with col1:
        st.markdown(f'`{a}`')
    with col2:
        st.markdown(b)

def txt3(a, b):
    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown(a)
    with col2:
        st.markdown(b)
  
def txt4(a, b, c):
    col1, col2, col3 = st.columns([1.5, 2, 2])
    with col1:
        st.markdown(f'`{a}`')
    with col2:
        st.markdown(b)
    with col3:
        st.markdown(c)

# Add buttons to the left column (like a resume section)
left_column, spacer, right_column = st.columns([1, 0.5, 4])

with left_column:
    
    image = Image.open('ayush1.jpg')
    st.image(image, width=200)

    st.write("# AYUSH JHA")

    if st.button("📝 EDUCATION"):
        st.session_state.current_section = 'Profile'
    if st.button("💼 EXPERIENCE"):
        st.session_state.current_section = 'Experience'
    if st.button("🏆 ACHIEVEMENTS"):
        st.session_state.current_section = 'Education'
    if st.button("💻 TECHNICAL SKILLS"):
        st.session_state.current_section = 'Skills'
    if st.button("📞 CONTACT"):
        st.session_state.current_section = 'Contact'

# Content in the right column based on the selected section
with right_column:
    if st.session_state.current_section == 'Profile':
        st.markdown('<div class="centered-text"><h1>EDUCATION</h1></div>', unsafe_allow_html=True)
        txt('Third year Information Technology student pursuing B.Tech from **Kamla Nehru Institute of Technology**, Sultanpur', 'CGPA:`8.7`')
        st.markdown('''
            **Bachelor of Technology**
''')
        st.markdown('''
            - Intermediate:
        ''')
        txt('D.A.V Senior Secondary Public School, Anpara', 'Percentage:`91.2`')
        st.markdown('''
            - High School:
        ''')
        txt('D.A.V Senior Secondary Public School, Anpara', 'Percentage:`97.8`')

    elif st.session_state.current_section == 'Experience':
        st.markdown('<div class="centered-text"><h1>EXPERIENCE</h1></div>', unsafe_allow_html=True)
        st.write("This section showcases the user's work experience. Include job titles, companies, years of work, and responsibilities.")
        
    elif st.session_state.current_section == 'Education':
        st.markdown('<div class="centered-text"><h1>ACHIEVEMENTS</h1></div>', unsafe_allow_html=True)
        st.write("This section covers the user's achievements. Include notable awards, recognitions, and accomplishments.")
        
    elif st.session_state.current_section == 'Skills':
        st.markdown('<div class="centered-text"><h1>TECHNICAL SKILLS</h1></div>', unsafe_allow_html=True)
        st.write("This section highlights the user's skills. List out technical, interpersonal, and other relevant skills.")

    elif st.session_state.current_section == 'Contact':
      for img_path, link, text in [
        ('./linkedin.png', 'https://www.linkedin.com/in/ayushjha6104/', 'Ayush Jha - Linkedin'),
        ('./phone.png', 'tel:+1234567890', 'Phone'),
        ('./gmail.png', 'mailto:jha2004ayush@gmail.com', 'Email'),
        ('./github1.png', 'https://github.com/mysteriouscoder610', 'GitHub')
    ]:
        col1, col2 = st.columns([0.2, 4])
        with col1:
            img = Image.open(img_path)
            st.image(img, width=40)
        with col2:
            st.markdown(f'<a href="{link}" target="_blank">{text}</a>', unsafe_allow_html=True)
