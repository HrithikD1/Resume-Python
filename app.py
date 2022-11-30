from pathlib import Path
import streamlit as st
from PIL import Image

#--- Path Settings ---#
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()

css_file = current_dir / "Styles" / "main.css"

resume_file = current_dir / "Assets" / "CV.pdf"

profile_pic = current_dir / "Assets" / "profile-pic.png"


#-- General Settings --#
PAGE_TITLE = "Digital CV | Hrithik Reddy"
PAGE_ICON = "\U0001f4c4"
NAME = "Hrithik Reddy"
DESCRIPTION = """
Programmer - An Experienced Programmer in Java, Python, JS, C++.
"""
EMAIL = "hrithikreddy2011@gmail.com"
SOCIAL_MEDIA = {
    "GitHub": "https://github.com/Hrithikprobro"
}
PROJECTS = {
    "🏆 AlignPro, A game made with Raylib": "github.com/Hrithikprobro/AlignPro",
    "🏆 TicTacToe made with vanilla javascript ": "https://github.com/Hrithikprobro/Tic-Tac-Toe-In-Your-Pocket",
    "🏆 Desktop Application - Notepad in Java": "https://github.com/Hrithikprobro/Notepad-In-Java",
    "🏆 Stopwatch and Timer made with ReactJs": "https://github.com/Hrithikprobro/StopWactchReactAndTime" ,
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS, PDF & PROFIL PIC ---
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


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas, streamlit), ReactJs, Swing(Java), Raylib(C++)
- 📊 Data Visulization: MS Excel, Plotly
- 📚 Modeling: Logistic regression
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
- ► Used Raylib and JS to Make Games Which are 2D coded in C++ and Jquery
- ► Made a Stopwatch with React and a Fibonacci Generater
- ► Made Basic Unit Converters in Java
"""
)

# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
