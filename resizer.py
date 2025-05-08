import os
from PIL import Image

# Define input and output directories
input_folder = "cropped_all"
output_folder = "resized_all"

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Loop through all files in the input folder
for filename in os.listdir(input_folder):
    input_path = os.path.join(input_folder, filename)
    output_path = os.path.join(output_folder, filename)

    # Check if the file is an image
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
        try:
            # Open the image
            with Image.open(input_path) as img:
                # Resize the image to 256x256
                resized_img = img.resize((128, 128))
                # Save the resized image to the output folder
                resized_img.save(output_path)
                print(f"Resized and saved: {filename}")
        except Exception as e:
            print(f"Error processing {filename}: {e}")
    else:
        print(f"Skipped non-image file: {filename}")