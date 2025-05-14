import os
from PIL import Image
import imagehash

def remove_duplicates(folder_path):
    hashes = {}
    removed_count = 0

    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            file_path = os.path.join(folder_path, filename)
            try:
                with Image.open(file_path) as img:
                    hash_val = imagehash.average_hash(img)
                if hash_val in hashes:
                    print(f"Duplicate found: {filename} (same as {hashes[hash_val]}) — removing")
                    os.remove(file_path)
                    removed_count += 1
                else:
                    hashes[hash_val] = filename
            except Exception as e:
                print(f"Error reading {filename}: {e}")

    print(f"✅ Done. Removed {removed_count} duplicate(s) from: {folder_path}")

# Apply to all class folders
base_dir = 'nigerian_attire'  # make sure this matches your actual folder
for class_name in os.listdir(base_dir):
    class_path = os.path.join(base_dir, class_name)
    if os.path.isdir(class_path):
        remove_duplicates(class_path)
