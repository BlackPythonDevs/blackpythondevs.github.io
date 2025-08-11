from PIL import Image
import os


def crop_to_ratio(img, target_ratio):
    """Crop image to target ratio (e.g., 16/9 or 1/1) without distortion."""
    width, height = img.size
    current_ratio = width / height

    if current_ratio > target_ratio:
        # Crop width
        new_width = int(height * target_ratio)
        left = (width - new_width) // 2
        return img.crop((left, 0, left + new_width, height))
    else:
        # Crop height
        new_height = int(width / target_ratio)
        top = (height - new_height) // 2
        return img.crop((0, top, width, top + new_height))


def process_image(file_path, ratio, max_size, format="webp"):
    """Process and overwrite the original image: crop, resize, convert format."""
    try:
        with Image.open(file_path) as img:
            # Crop to target ratio
            if ratio:
                img = crop_to_ratio(img, ratio)

            # Resize to max dimensions
            if max_size:
                img.thumbnail(max_size)

            # convert to webp if no transparency
            if format.lower() == "webp" and img.mode != "RGBA":
                file_path = os.path.splitext(file_path)[0] + ".webp"
                img.save(file_path, "webp", optimize=True, quality=85)
            else:
                img.save(file_path, optimize=True)

            print(f"✅ Overwritten: {file_path}")
    except Exception as e:
        print(f"❌ Failed {file_path}: {str(e)}")


def main():
    folder = "assets/images"

    # Rules for image types
    rules = [
        {
            "suffix": ["banner", "header"],
            "ratio": 16 / 9,
            "max_size": (1920, 1080),  # Min size enforced via cropping
            "format": "webp",
        },
        {
            "suffix": ["thumb", "profile"],
            "ratio": 1 / 1,
            "max_size": (800, 800),
            "format": "webp",
        },
    ]

    for filename in os.listdir(folder):
        if filename.lower().endswith((".jpg", ".jpeg", ".png", ".webp")):
            file_path = os.path.join(folder, filename)

            # Apply first rule
            matched_rule = None
            for rule in rules:
                if any(keyword in filename.lower() for keyword in rule["suffix"]):
                    matched_rule = rule
                    break

            # no cropping, resize to 800x600, convert to webp if no transparency
            if not matched_rule:
                with Image.open(file_path) as img:
                    format = "webp" if img.mode != "RGBA" else "png"
                matched_rule = {"ratio": None, "max_size": (800, 600), "format": format}

            process_image(file_path, **matched_rule)


if __name__ == "__main__":
    main()
