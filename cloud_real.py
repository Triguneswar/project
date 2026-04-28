from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
import os

def upload_to_drive(folder):
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()  # opens browser

    drive = GoogleDrive(gauth)

    for file in os.listdir(folder):
        filepath = os.path.join(folder, file)

        gfile = drive.CreateFile({'title': file})
        gfile.SetContentFile(filepath)
        gfile.Upload()

        print("Uploaded to Drive:", file)