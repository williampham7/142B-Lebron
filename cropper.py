import os
from PIL import Image

# Class guide mapping
CLASS_GUIDE = {
    0: "curry",
    1: "kd",
    2: "lebron",
    3: "glasses",
    4: "mouse",
    5: "thermos",
}

def crop_images(base_folder):
    # Define the subfolders to process
    subfolders = ['train', 'valid', 'test']
    cropped_folder = os.path.join(base_folder, 'cropped')

    # Create the cropped folder if it doesn't exist
    if not os.path.exists(cropped_folder):
        os.makedirs(cropped_folder)

    for subfolder in subfolders:
        subfolder_path = os.path.join(base_folder, subfolder)
        if not os.path.exists(subfolder_path):
            continue  # Skip if the subfolder doesn't exist

        images_folder = os.path.join(subfolder_path, 'images')
        labels_folder = os.path.join(subfolder_path, 'labels')

        if not os.path.exists(images_folder) or not os.path.exists(labels_folder):
            continue  # Skip if images or labels folder doesn't exist

        for image_name in os.listdir(images_folder):
            if not image_name.endswith('.jpg'):
                continue  # Skip non-JPG files

            image_path = os.path.join(images_folder, image_name)
            label_path = os.path.join(labels_folder, image_name.replace('.jpg', '.txt'))

            if not os.path.exists(label_path):
                continue  # Skip if the corresponding label file doesn't exist

            # Open the image
            with Image.open(image_path) as img:
                # Read the label file
                with open(label_path, 'r') as label_file:
                    for line in label_file:
                        # Assuming the label file format is: class_id x_center y_center width height (normalized)
                        parts = line.strip().split()
                        if len(parts) != 5:
                            continue  # Skip invalid label lines

                        class_id, x_center, y_center, width, height = map(float, parts)

                        # Convert normalized coordinates to pixel values
                        img_width, img_height = img.size
                        x_center *= img_width
                        y_center *= img_height
                        width *= img_width
                        height *= img_height

                        # Calculate the bounding box
                        left = int(x_center - width / 2)
                        top = int(y_center - height / 2)
                        right = int(x_center + width / 2)
                        bottom = int(y_center + height / 2)

                        # Crop the image
                        cropped_img = img.crop((left, top, right, bottom))

                        # Get the label type from the class guide
                        label_type = CLASS_GUIDE.get(int(class_id), "unknown")

                        # Save the cropped image with the label type in the file name
                        cropped_image_name = f"{label_type} - {os.path.splitext(image_name)[0]}_cropped.jpg"
                        cropped_image_path = os.path.join(cropped_folder, cropped_image_name)
                        cropped_img.save(cropped_image_path)

if __name__ == "__main__":
    # Replace with the path to your base folder
    base_folder = "/Users/tai/Desktop/Projects/142B Project/NBA_objs"
    crop_images(base_folder)