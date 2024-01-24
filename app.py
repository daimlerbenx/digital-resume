from pathlib import Path
import streamlit as st
from PIL import Image

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital Resume | Daimler Benz Alebaba"
PAGE_ICON = ":wave:"
NAME = "Daimler Benz Alebaba"
DESCRIPTION = """
Researcher | Developer
"""
EMAIL = "daimlerbenx@gmail.com"
SOCIAL_MEDIA = {
    "Facebook": "https://www.facebook.com/daimlerbenx/",
    "LinkedIn": "https://www.linkedin.com/in/daimlerbenx/",
    "GitHub": "https://github.com/daimlerbenx",
    "Google Scholar": "https://bit.ly/daimlerbenx-google-scholar",
}
PROJECTS = {
    "🏆 Web Developer - Developed a data science/mining web app": "https://smuems.onrender.com/",
    "🏆 Graduate Research Assistant - Involved in a data mining and machine learning research project": None,
    "🏆 Graphic Designer - Designed posters and logos for E-commerce businesses": "https://www.milkpowder.sg/",
    "🏆 Front-End Developer - Developed a decentralized mobile application interface": "https://play.google.com/store/apps/details?id=my.gov.onegovappstore.USIMTASeScroll&hl=en&gl=US",
    "🏆 Web Developer - Developed the JPDS official website": "https://jpds.sabah.gov.my/",
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
st.subheader("About Me")
st.write(
    """
A technology enthusiast driven by passion and possessing a diverse skill set, I excel in both research and development. With a robust background in computer science research and a proficiency in technical skills, I contribute to elevating organizational product design and performance. My enthusiasm extends to exploring cutting-edge technologies, and I am always eager to learn and stay at the forefront of technological advancements.
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 🧑‍💻 Programming: Python, Java, PHP, SQL, Solidity
- 💻 Front-End Technologies: HTML5, CSS3, XML
- 📚 Interest Research: Artificial Intelligence, Blockchain, Data Mining, Internet of Things
- 🗄️ Databases: MySQL
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🧑‍💻", "**Graduate Research Assistant | Universiti Malaysia Sabah**")
st.write("2022 - 2024")
st.write(
    """
- ► Assist project leader with research projects, including literature reviews, data collection and analysis, and manuscript preparation
- ► Attend international conferences and seminars for research paper presentations
- ► Secured a research grant via the University grant scheme
"""
)

# --- JOB 2
st.write('\n')
st.write("🧑‍🏫", "**Tutor | Faculty of Computing and Informatics, Universiti Malaysia Sabah**")
st.write("2022 - 2023")
st.write(
    """
- ► Facilitate small group tutoring for undergraduate students in discrete mathematics and statistics
- ► Assist students in understanding and clarifying concepts covered in lectures
"""
)

# --- JOB 3
st.write('\n')
st.write("🧑‍💻", "**Front-End Developer | iExploTech Sdn. Bhd.**")
st.write("2021 - 2022")
st.write(
    """
- ► Involved in development projects with Malaysian government agencies and Institusi Pengajian Tinggi Malaysia
- ► Created Ethereum smart contracts using Remix IDE
- ► Developed the decentralized mobile application interface
- ► Designed graphics using Photoshop, and Android app prototypes using XD
- ► Compiled system administration manuals
"""
)


# --- EDUCATION BACKGROUND ---
st.write('\n')
st.subheader("Education Background")
st.write("---")

st.write("👨‍🎓", "**Bachelor of Information Technology with Honours (Business Computing) | Universiti Malaysia Sabah**")
st.write("2017 - 2021")
st.write(
    """
- ► Developed an Internet of Things-based smart mirror using Arduino and Raspberry Pi in the final year project
- ► Awarded Dean's List for four consecutive semesters
- ► Gold Medal in the iDEA 21 Competition, Ministry of Youth and Sports Malaysia 2021
- ► Published a review paper at the International Conference (ICETIS) 2021
- ► 1st Place in the UMS Innovation Competition 2021
- ► 1st Place in the FKI UMS Jersey Design Competition 2021
- ► Silver Medal in the UMS PEREKA Competition 2020
- ► 3rd Place in the UMSKAL Residential Logo Creation Competition 2018
- ► Team Leader at the Tamu Gadang Chess Tournament 2018
"""
)


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
