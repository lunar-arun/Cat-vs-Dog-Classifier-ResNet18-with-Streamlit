import streamlit as st
import numpy as np
from PIL import Image
import os
from packages import model

# Use raw string for Windows paths or os.path.join for cross-platform compatibility
IMAGE_FOLDER = r'packages\test-images'
thumbnail_size = (50, 50)  # Size for each thumbnail
rows, cols = 5, 4  # Define the grid dimensions

def default_image():
    # List all image files in the specified folder
    image_files = [f for f in os.listdir(IMAGE_FOLDER) if os.path.isfile(os.path.join(IMAGE_FOLDER, f))]

    # Create full paths for each image file
    image_paths = [os.path.join(IMAGE_FOLDER, img) for img in image_files]
    
    # Number of images per row
    images_per_row = cols
    
    # Calculate the number of rows needed to fit all images
    num_images = len(image_paths)
    rows_needed = (num_images + images_per_row - 1) // images_per_row  
    
    # Pad image_paths to ensure grid dimensions match
    while len(image_paths) < rows_needed * images_per_row:
        image_paths.append(None)  # Append a placeholder for empty slots
    
    # Reshape the list of image paths into a 2D array for grid layout
    image_paths_array = np.array(image_paths).reshape((rows_needed, images_per_row))
    
    # Create a new blank image to hold the grid of thumbnails
    grid_width = cols * thumbnail_size[0]
    grid_height = rows * thumbnail_size[1]
    grid_image = Image.new('RGB', (grid_width, grid_height))
    
    for i in range(rows):
        for j in range(cols):
            # Get the path of the image to be added to the grid
            image_path = image_paths_array[i, j]
            if image_path and os.path.isfile(image_path):
                img = Image.open(image_path)
                
                # Resize the image to fit in the thumbnail
                img.thumbnail(thumbnail_size)
                
                # Calculate the position where the thumbnail should be placed
                x = j * thumbnail_size[0]
                y = i * thumbnail_size[1]
                
                # Paste the thumbnail into the grid image
                grid_image.paste(img, (x, y))
    
    # Display the grid image using Streamlit
    col1, col2 = st.columns([2, 1])  # Adjust column width ratios for layout
    with st.container(border=True): 
        with col1:
            for i in range(rows):
                # Create columns for each row of images
                cols_in_row = st.columns(cols)
                for j in range(cols):
                    image_path = image_paths_array[i, j]
                    if image_path:
                        with cols_in_row[j]:
                            # Display each image thumbnail
                            st.image(image_path, use_column_width=True)
                            # Button to select the image
                            if st.button(f"Select Image {i*cols+j+1}", key=f"btn_{i}_{j}"):
                                # Save the path of the selected image to session state
                                st.session_state.selected_image_path = image_path
    
    # Initialize session state for selected image path if not already set
    if 'selected_image_path' not in st.session_state:
        st.session_state.selected_image_path = None
        
    with st.container(border=True):
        with col2:
            # Display the selected image and its prediction if an image is selected
            if st.session_state.selected_image_path:
                selected_image = Image.open(st.session_state.selected_image_path)
                st.image(selected_image, caption="Selected Image", use_column_width=True)
                # Replace `model.predict_image` with your actual prediction function
                prediction = model.predict_image(selected_image)
                st.write(f"Prediction: {prediction}")
