from scanner import scan
from deduplicator import find_duplicates
from classifier import classify
from compressor import compress
from cloud_real import upload_to_drive
# from cleaner import delete_originals   # keep disabled for now

def run():
    # 👉 Change this folder if needed
    folder = r"C:\Users\trigun\Pictures"

    print("🔍 Scanning files...")
    files = scan(folder)
    print("Total files:", len(files))

    if len(files) == 0:
        print("⚠️ No files found. Check your folder path.")
        return

    print("\n🧬 Finding duplicates...")
    duplicates = find_duplicates(files)
    print("Duplicates found:", len(duplicates))

    print("\n📊 Classifying files...")
    frequent, rare = classify(files)
    print("Rare files:", len(rare))

    if len(rare) == 0:
        print("⚠️ No rare files to process.")
        return

    print("\n🗜️ Compressing rare files...")
    compress(rare)

    print("\n☁️ Uploading to Google Drive...")
    upload_to_drive("compressed")

    # ⚠️ ENABLE ONLY AFTER TESTING
    # print("\n🧹 Deleting original files...")
    # delete_originals(rare)

    print("\n✅ Optimization Complete")


if __name__ == "__main__":
    run()