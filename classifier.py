import os
import time

# 🔧 CONFIGURATION
RARE_DAYS = 30          # change this anytime (e.g., 1 for testing)
DEBUG = True            # set False to disable logs


def classify(files):
    frequent = []
    rare = []

    now = time.time()
    threshold = RARE_DAYS * 24 * 60 * 60  # convert days → seconds

    for file in files:
        try:
            # 📅 Get timestamps
            last_access = os.path.getatime(file)
            last_modified = os.path.getmtime(file)

            # ⚠️ Windows fallback:
            # If access time looks invalid, use modified time
            if last_access < 100000:
                last_access = last_modified

            # 🧠 Decide rare or frequent
            if now - last_access > threshold:
                rare.append(file)
                status = "RARE"
            else:
                frequent.append(file)
                status = "FREQUENT"

            # 🧾 Debug logs
            if DEBUG:
                print(f"{status}: {file}")
                print("   Last opened:", time.ctime(last_access))

        except Exception as e:
            print("Error processing:", file, e)

    return frequent, rare