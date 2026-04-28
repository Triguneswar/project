from PIL import Image
import os

def compress(files):
    os.makedirs("compressed", exist_ok=True)

    original_size = 0
    compressed_size = 0

    for file in files:
        try:
            print("Compressing:", file)

            # Get original size
            original_size += os.path.getsize(file)

            # Open and convert image
            img = Image.open(file).convert("RGB")

            # Create new file path
            new_path = os.path.join("compressed", os.path.basename(file))

            # Save compressed image
            img.save(new_path, "JPEG", quality=30, optimize=True)

            # Get compressed size
            compressed_size += os.path.getsize(new_path)

        except Exception as e:
            print("Error:", e)

    # Calculate storage saved
    saved = (original_size - compressed_size) / (1024 * 1024)

    print(f"💾 Storage saved: {saved:.2f} MB")