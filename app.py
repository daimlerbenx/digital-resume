from pathlib import Path
import streamlit as st
from PIL import Image

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital Resume - Daimler Benz Alebaba"
PAGE_ICON = ":wave:"
NAME = "Daimler Benz Alebaba"
DESCRIPTION = """
Software Developer | Engineer
"""
EMAIL = "daimlerbenx@gmail.com"
SOCIAL_MEDIA = {
    "Facebook": "https://www.facebook.com/daimlerbenx",
    "LinkedIn": "https://www.linkedin.com/in/daimlerbenx",
    "GitHub": "https://github.com/daimlerbenx",
    "Google Scholar": "https://bit.ly/daimlerbenx-google-scholar",
}
PROJECTS = {
    "🏆 Web App Developer - Developed data mining web app for user engagement pattern discovery": "https://smuems.onrender.com/",
    "🏆 Graduate Research Assistant - Researched on data mining and machine learning research project": None,
    "🏆 Graphic Designer - Designed posters and logos for E-commerce brand": "https://www.milkpowder.sg/",
    "🏆 Front-End Software Developer - Developed a decentralized mobile application (DApps) interface": "https://play.google.com/store/apps/details?id=my.gov.onegovappstore.USIMTASeScroll&hl=en&gl=US",
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
col1, col2 = st.columns([1, 2], gap="small")
with col1:
    st.image(profile_pic, width=200)

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
st.subheader("Professional Summary")
st.write(
    """
I am a passionate technology enthusiast with a strong interest in both research and development, complemented by solid research expertise and experience in software and web development. I continuously explore state-of-the-art technologies and am committed to staying at the forefront of advancements. My willingness to learn new knowledge and skills allows me to excel independently with minimal supervision.
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Technical Skills")
st.write(
    """
- 🧑‍💻 Back-End: C++, Python, Java, PHP, SQL, Solidity
- 💻 Front-End: HTML5, CSS3, Bootstrap, XML, JavaScript
- 📚 Design: Adobe Photoshop, Illustrator, XD, Premiere Pro
"""
)

st.write('\n')
st.subheader("Soft Skills")
st.write(
    """
- Critical Thinking, Problem Solving, Self-Motivated, Independence, Time Management, Team Orientated
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🧑‍💻", "**Graduate Research Assistant | Universiti Malaysia Sabah | Feb 2022 - Jan 2024**")
st.write(
    """
- ► Researched and structured algorithms on Semi-Supervised Machine Learning models for user engagement pattern discovery.
- ► Led in-depth literature reviews, spearheaded data collection and analysis, and authored manuscripts to develop new model, contributed to practitioners', influencers', and industry professionals' understanding of their social media user engagement.
"""
)

# --- JOB 2
st.write('\n')
st.write("👨‍🏫", "**Tutor | Universiti Malaysia Sabah | Nov 2022 - Jan 2023**")
st.write(
    """
- ► Enhanced undergraduate problem-solving skills and understanding in discrete mathematics and statistics through hands-on practice.
"""
)

# --- JOB 3
st.write('\n')
st.write("🧑‍💻", "**Front-End Software Developer | iExploTech Sdn. Bhd. | Mar 2021 - Dec 2022**")
st.write(
    """
- ► Developed Ethereum smart contracts on Blockchain using Solidity in Remix IDE.
- ► Designed Android Decentralized Apps (dApps) high-fidelity user interface using UI/UX principles, enhanced consistency and scalability.
- ► Served as Back-End (Java) when deemed necessary.
- ► Created dApps graphics and prototypes using Adobe tools.
- ► Compiled system administration manuals.

"""
)

# --- JOB 4
st.write('\n')
st.write("👨‍🏫", "**Web Developer | Jabatan Pelabuhan dan Dermaga Sabah | Apr 2021 - May 2021**")
st.write(
    """
- ► Developed official website using WordPress as freelance.
"""
)


# --- EDUCATION BACKGROUND ---
st.write('\n')
st.subheader("Education Background")
st.write("---")

st.write("👨‍🎓", "**Master of Science (Computer Science) | Universiti Malaysia Sabah | 2022 - 2024**")
st.write(
    """
- ► Data Mining and Machine Learning specialization.
- ► Secured research grant by University Grant Scheme and sponsored study by Graduate Excellence Programme, MARA.
- ► Achieved EXCELLENT (92% - 95%) results for four consecutive semesters.
- ► Participated in international conferences and seminars for new research findings discussion.
- ► Published research papers in SCOPUS-indexed journals.
- ► Developed Data Mining Web App using Streamlit Python Framework and deployed to Render from GitHub.
- ► [International Level] UMS EXCOCIPTA Research and Innovation Competition 2024 - Bronze Medal
"""
)

st.write("👨‍🎓", "**Bachelor of Information Technology with Honours (Business Computing) | Universiti Malaysia Sabah | 2017 - 2021**")
st.write(
    """
- ► Awarded Dean's list for four consecutive semesters.
- ► Developed Internet of Things smart system for organizational efficiency using Arduino and Raspberry Pi in final year project.
- ► Published review paper in SCOPUS-indexed conferences.
- ► [National Level] iDEA’21 Ministry of Youth and Sports Malaysia Innovation Competition 2021 - Gold Medal
- ► [University Level] “One Way Ticket to Success” Innovation Competition 2021 - 1st Place
- ► [University Level] Persatuan Mahasiswa Fakulti Komputeran dan Informatik Jersey Design Competition 2021 - 1st Place
- ► [International Level] UMS EXCOCIPTA Research and Innovation Competition 2020 - Silver Medal
- ► [University Level] UMSKAL Residential Logo Creation Competition 2019 - 3rd Place
- ► Tamu Gadang Chess Tournament 2018 – Publicity Team Leader

"""
)

st.write("👨‍🎓", "**Professional Certificates**")
st.write(
    """
- ► [Coursera] Google Data Analytics and IBM AI Developer
- ► [edX] HarvardX: Data Science: Machine Learning
"""
)

st.write("👨‍🎓", "**Spoken Language**")
st.write(
    """
- ► Fluent written and spoken English and Malay
- ► Intermediate spoken Mandarin
"""
)

st.write("👨‍🎓", "**Research Interests**")
st.write(
    """
- ► Blockchain, Data Mining, Internet of Things, Machine Learning
"""
)


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
