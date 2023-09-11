from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "f3.pdf"
profile_pic = current_dir / "assets" / "profile-pic.jpg"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Dinesh Raya"
PAGE_ICON = ":wave:"
NAME = "Dinesh Raya"
DESCRIPTION = """
6 monts expereince with python and mysql database also along with andvanced python concepts.
"""
EMAIL = "dineshraya365@email.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/dinesh-raya/",
    "GitHub":   "https://github.com/Dinesh-raya?tab=repositories/"
}
PROJECTS = {
    "🏆 Streamlit app for youtube video & audio downloader": "https://github.com/Dinesh-raya/R_O_D-YT",
    "🏆 MCA project based on Deep learning | Marine trash detection": "https://github.com/Dinesh-raya/mca-project",
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


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ 6 monts expereince extracting actionable insights from data
- ✔️ Strong hands on experience and knowledge in Python and mysql
- ✔️ Good understanding of Oops principles and their respective applications
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python ( Pandas), SQL
- 📊 Data Visulization: MS Excel, Plotly
- 📚 Modeling: Logistic regression, linear regression, decition trees, Naive Bayes
- 🗄️ Databases: Postgres, MongoDB, MySQL
"""
)

# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
