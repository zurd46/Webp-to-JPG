import os
from PIL import Image

def convert_webp_to_jpg(directory):
    # Ensure the directory exists
    if not os.path.exists(directory):
        print(f"The directory {directory} does not exist.")
        return
    
    # Loop through all files in the directory
    for filename in os.listdir(directory):
        if filename.endswith(".webp"):
            # Construct full file path
            webp_path = os.path.join(directory, filename)
            # Change the file extension to .jpg
            jpg_path = os.path.splitext(webp_path)[0] + ".jpg"
            
            # Open the .webp image and convert it to .jpg
            with Image.open(webp_path) as img:
                img.convert("RGB").save(jpg_path, "JPEG")
            
            print(f"Converted {webp_path} to {jpg_path}")
            
            # Delete the .webp file after conversion
            os.remove(webp_path)
            print(f"Deleted {webp_path}")

# Replace the path with a raw string
convert_webp_to_jpg(r'path\to\your\folder')
