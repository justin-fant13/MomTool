import streamlit as st
from functions.generate_report import generate_report

st.set_page_config(page_title="Mom's Tool", page_icon=":building_construction:", layout="wide", initial_sidebar_state="collapsed")
st.title("Mom's Tool")
st.subheader("Hi Mom :smile: Upload your file below:")

file = st.file_uploader("Upload your file", type=["xlsx", "xls"], label_visibility="hidden")
st.markdown('#') # Add space

if not 'saved_download' in st.session_state:
  st.session_state.saved_download = {}

# Main Page
if st.button("Generate Report", type="primary"):
  if file:
    file_name = file.name.split('.')[0]
    with st.spinner("Generating..."):
      report = generate_report(file) # Generate report     
      st.success("Done! :sunglasses:")
      file_data = open(report, 'rb').read() 
      st.session_state.saved_download[file_name] = file_data # Save file data to session state
      st.download_button("Download Report", data=file_data, file_name=f"{ file_name }.docx") 
  else: 
    st.error("No file uploaded! :astonished:")

# Sidebar
with st.sidebar:
  st.title("Generated Reports:")
  if st.session_state.saved_download:
    for file_name, file_data in st.session_state.saved_download.items(): # Display all saved files
      st.download_button(f"{ file_name }", data=file_data, file_name=f"{ file_name }.docx", key=file_name)  
  else:  
    st.info("No reports generated yet! :sweat_smile:")

# Footer
st.markdown('#') # Add space
st.write("Made with :heart: by [Justin Fant](https://justinfant.dev/)")