
import streamlit as st
import fitz  # PyMuPDF
from PIL import Image
import io

st.set_page_config(layout="wide")  # Set the layout to wide mode

# Initialize the state for the text box content
if 'name_sess' not in st.session_state:
    st.session_state.name_sess = ''

# Create two main columns
main_col1, main_col2 = st.columns([1, 1])

with main_col1:
    # with st.form("my_form"):
    st.title("User Information")
    name = st.text_input("Name", value=st.session_state.name_sess)
    col1, col2 = st.columns(2)
    with col1:
        phone = st.text_input("Contact Number")
        bdate = st.date_input("Date of Birth")
    with col2:
        mail = st.text_input("Email address")
        gender = st.radio("Gender", ("Male", "Female"),horizontal=True)
    edu_qualification = st.text_area("Educational Qualifications", "")
    edu_qualification = st.text_area("Professional Qualifications", "")
    Certifications = st.text_area("Certifications", "")
    skills = st.text_area("Skills", "")

    submit_button = st.button(label='Submit')

    if submit_button:
        st.write("Form submitted!")
        st.write(f"Name: {name}")
        st.write(f"Date: {bdate}")
        st.write(f"Gender: {gender}")
        st.write(f"Comments: {edu_qualification}")

with main_col2:
    st.title("PDF Viewer")
    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

    if uploaded_file is not None:
        # Read the PDF file
        proceed_button = st.button(label='Submit',key='proceed')
        
        with fitz.open(stream=uploaded_file.read(), filetype="pdf") as doc:
            num_pages = doc.page_count
            st.write(f"Number of pages: {num_pages}")

            # Create two sub-columns for displaying PDF pages
            col1, col2 = st.columns(2)

            for page_num in range(num_pages):
                page = doc.load_page(page_num)
                pix = page.get_pixmap()
                img = Image.open(io.BytesIO(pix.tobytes()))

                if page_num % 2 == 0:
                    with col1:
                        st.image(img, caption=f'Page {page_num + 1}', use_column_width=True)
                else:
                    with col2:
                        st.image(img, caption=f'Page {page_num + 1}', use_column_width=True)
        
        if proceed_button:
            st.session_state.name_sess = 'banana nanana nana'
