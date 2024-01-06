import streamlit as st
from functions.generate_report import generate_report


st.set_page_config(page_title="Mom's Tool", page_icon=":building_construction:", layout="wide")
st.title("Mom's Tool")
st.subheader("Hi Mom :smile: Upload your file below:")

file = st.file_uploader("Upload your file", type=["xlsx", "xls"], label_visibility="hidden")
st.markdown('#') # Add space


# Main Page
if st.button("Evaluate", type="primary"):
  if file:
    file_name = file.name.split('.')[0]
    with st.spinner("Evaluating..."):
      report = generate_report(file) # Generate report     
      st.success("Done! :sunglasses:")
      st.download_button("Download Report", data=open(report, "rb").read(), file_name=f"{file_name}.docx")
 
  else: 
    st.error("No file uploaded! :astonished:")


# Footer
st.markdown('#') # Add space
st.write("Made with :heart: by [Justin Fant](https://justinfant.dev/)")