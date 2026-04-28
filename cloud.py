import os
import shutil

def upload_to_cloud(folder):
    os.makedirs("cloud_storage", exist_ok=True)

    for file in os.listdir(folder):
        src = os.path.join(folder, file)
        dst = os.path.join("cloud_storage", file)

        shutil.move(src, dst)

    print("☁️ Uploaded to cloud_storage")