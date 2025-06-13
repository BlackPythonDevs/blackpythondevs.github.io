from PIL import Image
import os

folder = "assets/images"
new_size = (800, 600)

for filename in os.listdir(folder):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
        file_path = os.path.join(folder, filename)
        original_size = os.path.getsize(file_path)

        with Image.open(file_path) as img:
            img.thumbnail(new_size)
            img.save(file_path)

        new_size_bytes = os.path.getsize(file_path)
        reduction = original_size - new_size_bytes
        percent = (reduction / original_size) * 100 if original_size else 0

        print(f"✅ Resized: {filename} | Saved {reduction//1024}KB ({percent:.1f}%)")
