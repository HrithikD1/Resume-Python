from pathlib import Path
import streamlit as st
from PIL import Image

# --- Path Settings --- #
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()

css_file = current_dir / "Styles" / "main.css"
resume_file = current_dir / "Assets" / "CV.pdf"
profile_pic = current_dir / "Assets" / "profile-pic.png"

# -- General Settings -- #
PAGE_TITLE = "Digital CV | Hrithik Reddy"
PAGE_ICON = "\U0001f4c4"
NAME = "Hrithik Reddy"
DESCRIPTION = """
Programmer - An Experienced Programmer in Java, Python, JS, C++.
"""
EMAIL = "hrithikreddy2011@gmail.com"
PROJECTS = {
    "🏆 AlignPro, A game made with Raylib": "https://github.com/HrithikD1/AlignPro",
    "🏆 TicTacToe made with vanilla javascript ": "https://github.com/HrithikD1/Tic-Tac-Toe-In-Your-Pocket",
    "🏆 Desktop Application - Notepad in Java": "https://github.com/HrithikD1/Notepad-In-Java",
    "🏆 Stopwatch and Timer made with ReactJs": "https://github.com/HrithikD1/StopWacthReactAndTime",
}

GITHUB = "https://github.com/HrithikD1"

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS, PDF & PROFILE PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)
    st.write("📁", GITHUB)

# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas, streamlit, flask), ReactJs, Swing(Java), Raylib(C++), Game Development with JS
- 📊 Data Visualization: MS Excel, Plotly
- 📄 HTML and CSS, Java, C++ Intermediate
"""
)

# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")

# --- JOB 1(Present Under school)
st.write("🚧", "**Programmer | Under School**")
st.write("03/2020 - Present")
st.write(
    """
- ► Used ReactJs and Flask to build a StudyHelper app
- ► Used Raylib and JS to make games coded in C++ and Jquery
- ► Made a Stopwatch with React and a Fibonacci Generator
- ► Made Basic Unit Converters in Java
"""
)

# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")

# --- SCROLLABLE IMAGES ---
st.write('\n')
st.subheader("Certficates")
image_paths = [
    current_dir / "Assets" / "C++.png",
    current_dir / "Assets" / "GamedevwithJs-Certificate.jpg",
    current_dir / "Assets" / "Html-Certificate.jpg",
    current_dir / "Assets" / "Java-Certificate.png",
    current_dir / "Assets" / "JavaScript-Certificate.png",
    current_dir / "Assets" / "Python-Certificate.png",
    current_dir / "Assets" / "React+Redux-Certificate.jpg"
]

st.markdown("<div style='display: flex; overflow-x: auto; padding: 10px;'>", unsafe_allow_html=True)
for image_path in image_paths:
    if not image_path.exists():
        st.warning(f"Image not found: {image_path}")
    else:
        try:
            image = Image.open(image_path)
            # Set fixed width for images, height will auto-adjust to maintain aspect ratio
            st.image(image, caption=image_path.name, width=500)  # Adjust the width as needed
        except Exception as e:
            st.error(f"Error loading image {image_path}: {e}")
st.markdown("</div>", unsafe_allow_html=True)


# --- FOOTER ---
st.markdown(
    """
    <footer style='text-align: center; padding: 20px; background-color: #f1f1f1;'>
        <p>© 2024 Hrithik Reddy | All Rights Reserved</p>
        <p>📫 hrithikreddy2011@gmail.com</p>
        <p><a href="https://github.com/HrithikD1" target="_blank">GitHub Profile</a></p>
    </footer>
    """,
    unsafe_allow_html=True
)