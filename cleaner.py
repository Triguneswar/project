import os

def delete_duplicates(duplicates):
    for file in duplicates:
        try:
            os.remove(file)
            print("🗑️ Deleted duplicate:", file)
        except Exception as e:
            print("Error deleting:", e)