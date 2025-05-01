import os
import shutil

def organize_cropped_images(base_folder):
    # Define the new folder to store all cropped images
    all_cropped_folder = os.path.join(base_folder, 'all_cropped')

    # Create the all_cropped folder if it doesn't exist
    if not os.path.exists(all_cropped_folder):
        os.makedirs(all_cropped_folder)

    # Iterate through all subfolders (train, valid, test)
    subfolders = ['Lebron1', 'Lebron2', 'NBA', 'NBA_objs']
    for subfolder in subfolders:
        cropped_folder = os.path.join(base_folder, subfolder, 'cropped')
        if not os.path.exists(cropped_folder):
            continue  # Skip if the cropped folder doesn't exist

        # Iterate through all images in the cropped folder
        for image_name in os.listdir(cropped_folder):
            if not image_name.endswith('.jpg'):
                continue  # Skip non-JPG files

            # Extract the class name from the file name (e.g., "class - img_name.jpg")
            class_name = image_name.split(' - ')[0]

            # Create a subfolder for the class in the all_cropped folder
            class_folder = os.path.join(all_cropped_folder, class_name)
            if not os.path.exists(class_folder):
                os.makedirs(class_folder)

            # Copy the image to the corresponding class subfolder
            source_path = os.path.join(cropped_folder, image_name)
            destination_path = os.path.join(class_folder, image_name)
            shutil.copy(source_path, destination_path)

if __name__ == "__main__":
    # Replace with the path to your base folder
    base_folder = "/Users/tai/Desktop/Projects/142B Project"
    organize_cropped_images(base_folder)