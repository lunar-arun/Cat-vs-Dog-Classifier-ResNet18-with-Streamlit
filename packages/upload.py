import streamlit as st
from PIL import Image
from packages import model, default

def image_uploader():
    # Create a container for uploading an image
    with st.container(border=True):
        # Upload an image file (supports jpg, jpeg, and png formats)
        uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    
    # Create another container for displaying the uploaded image and prediction
    with st.container(border=True):
        if uploaded_image:
            # Open the uploaded image file
            image = Image.open(uploaded_image)
            
            # Display the uploaded image with a caption and fixed width
            st.image(image, width=500, caption="Uploaded Image", use_column_width=False)
            
            # Make a prediction using the uploaded image
            prediction = model.predict_image(image)
            
            # Display the prediction result
            st.write(f"Prediction: {prediction}")

