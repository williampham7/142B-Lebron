import os

def count_photos_per_class(all_cropped_folder):
    if not os.path.exists(all_cropped_folder):
        print(f"The folder '{all_cropped_folder}' does not exist.")
        return

    # Iterate through each class subfolder in all_cropped
    for class_name in os.listdir(all_cropped_folder):
        class_folder = os.path.join(all_cropped_folder, class_name)
        if not os.path.isdir(class_folder):
            continue  # Skip if it's not a folder

        # Count the number of photos in the class folder
        photo_count = len([f for f in os.listdir(class_folder) if f.endswith('.jpg')])
        print(f"{class_name}: {photo_count} photos")

if __name__ == "__main__":
    # Replace with the path to your all_cropped folder
    all_cropped_folder = "/Users/tai/Desktop/Projects/142B Project/mega_batch"
    count_photos_per_class(all_cropped_folder)