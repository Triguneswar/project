from PIL import Image
import imagehash

def find_duplicates(files):
    hashes = {}
    duplicates = []

    for path in files:
        try:
            img = Image.open(path)
            h = imagehash.phash(img)

            if h in hashes:
                duplicates.append(path)  # duplicate file
            else:
                hashes[h] = path  # keep first as original

        except Exception as e:
            print("Error processing:", path, e)

    return duplicates