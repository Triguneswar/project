import os

def scan(folder):
    files = []
    image_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.webp')

    for root, _, filenames in os.walk(folder):
        for file in filenames:
            if file.lower().endswith(image_extensions):
                files.append(os.path.join(root, file))

    return files