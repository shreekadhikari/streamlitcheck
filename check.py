import streamlit as st

# --- Page settings ---
st.set_page_config(page_title="My CV", layout="centered")

# --- Header ---
st.title("📄 Shreek Adhikari")
st.subheader("Software Developer")
st.write("📍 Kathmandu, Nepal")
st.write("📧 shreek@example.com | 📱 +977-98xxxxxx | 🌐 github.com/shreekadhikari")

# --- Summary ---
st.header("🧾 Profile Summary")
st.write("""
Passionate full-stack developer with experience in modern web technologies and cloud platforms. 
I enjoy building scalable web apps, RESTful APIs, and clean user interfaces.
""")

# --- Skills ---
st.header("💼 Skills")
cols = st.columns(2)
cols[0].markdown("- Python\n- JavaScript\n- HTML/CSS\n- Flask\n- FastAPI")
cols[1].markdown("- React\n- PostgreSQL\n- Docker\n- Git/GitHub\n- Streamlit")

# --- Experience ---
st.header("🧰 Experience")
st.subheader("Software Developer @ MyCompany")
st.write("2022 - Present")
st.write("""
- Developed internal dashboards using Flask and React.
- Implemented REST APIs with FastAPI.
- Deployed Dockerized apps to DigitalOcean.
""")

# --- Education ---
st.header("🎓 Education")
st.subheader("BSc in Computer Science")
st.write("Tribhuvan University, 2017 - 2021")

# --- Footer ---
st.markdown("---")
st.write("Made with ❤️ using Streamlit")
