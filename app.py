import streamlit as st
from streamlit_option_menu import option_menu
from packages import page, default, upload

def main():
    # Configure the Streamlit app's page settings
    st.set_page_config(page_title="ResNet18 Classifier", page_icon=":books:", layout="wide")
    
    # Set the title of the Streamlit app
    st.title("Dog vs Cat Classifier")
    
    # Create a sidebar with options for navigation
    with st.sidebar:
        # Define the list of options for the sidebar menu
        Options: list = ["Introduction", "Default-Image", "Upload-Image"]
        
        # Use the option_menu widget to create a navigation menu in the sidebar
        selected: str = option_menu("Main Menu", Options, 
            icons=['clipboard', 'search', 'image'], menu_icon="cast", default_index=0)
        
    # Display content based on the selected menu option
    if selected == "Introduction":
        # Render the introduction page content from the page module
        st.markdown(page.INTRODUCTION, unsafe_allow_html=True)
    elif selected == "Default-Image":
        # Call the function to display the default image page from the default module
        default.default_image()
    elif selected == "Upload-Image":
        # Call the function to display the image uploader page from the upload module
        upload.image_uploader()

# Entry point for the script
if __name__ == "__main__":
    main()
