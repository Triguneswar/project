import tkinter as tk
from tkinter import ttk
import threading
import os
import shutil

from scanner import scan
from deduplicator import find_duplicates
from classifier import classify
from compressor import compress
from cloud_real import upload_to_drive


class StorageApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Storage Optimizer Pro 🚀")
        self.root.geometry("900x600")
        self.root.configure(bg="#0f172a")

        self.folder_path = os.path.join(os.path.expanduser("~"), "Pictures")

        # ===== SIDEBAR =====
        sidebar = tk.Frame(root, bg="#020617", width=200)
        sidebar.pack(side="left", fill="y")

        tk.Label(sidebar, text="⚡ Optimizer",
                 bg="#020617", fg="#38bdf8",
                 font=("Segoe UI", 14, "bold")).pack(pady=20)

        tk.Button(sidebar, text="🏠 Dashboard",
                  bg="#020617", fg="white", bd=0).pack(pady=10)

        tk.Button(sidebar, text="📊 Stats",
                  bg="#020617", fg="white", bd=0).pack(pady=10)

        tk.Button(sidebar, text="⚙ Settings",
                  bg="#020617", fg="white", bd=0).pack(pady=10)

        # ===== MAIN AREA =====
        main = tk.Frame(root, bg="#0f172a")
        main.pack(side="right", fill="both", expand=True)

        # Title
        tk.Label(main, text="Storage Optimizer Dashboard",
                 bg="#0f172a", fg="white",
                 font=("Segoe UI", 18, "bold")).pack(pady=10)

        # ===== CARDS =====
        cards = tk.Frame(main, bg="#0f172a")
        cards.pack(pady=10)

        self.files_label = self.create_card(cards, "Files", "0")
        self.dup_label = self.create_card(cards, "Duplicates", "0")
        self.rare_label = self.create_card(cards, "Rare", "0")

        # ===== BUTTON =====
        self.run_btn = tk.Button(
            main,
            text="🚀 Run Optimization",
            command=self.start_thread,
            bg="#22c55e",
            fg="black",
            font=("Segoe UI", 12, "bold"),
            padx=20,
            pady=8,
            relief="flat"
        )
        self.run_btn.pack(pady=15)

        # ===== PROGRESS =====
        self.progress = ttk.Progressbar(main, length=500, mode="indeterminate")
        self.progress.pack(pady=5)

        self.status = tk.Label(main, text="Idle",
                               bg="#0f172a", fg="#94a3b8")
        self.status.pack()

        # ===== LOG =====
        self.log_box = tk.Text(main,
                               bg="#020617",
                               fg="#38bdf8",
                               height=15,
                               font=("Consolas", 10),
                               insertbackground="white")
        self.log_box.pack(fill="both", expand=True, padx=10, pady=10)

    # ===== CARD UI =====
    def create_card(self, parent, title, value):
        frame = tk.Frame(parent, bg="#1e293b", padx=25, pady=15)
        frame.pack(side="left", padx=10)

        tk.Label(frame, text=title,
                 bg="#1e293b", fg="#94a3b8").pack()

        label = tk.Label(frame, text=value,
                         bg="#1e293b", fg="#38bdf8",
                         font=("Segoe UI", 16, "bold"))
        label.pack()

        return label

    def log(self, msg):
        self.log_box.insert(tk.END, msg + "\n")
        self.log_box.see(tk.END)

    def start_thread(self):
        threading.Thread(target=self.run_optimizer).start()

    # ===== MAIN ENGINE =====
    def run_optimizer(self):
        self.progress.start()
        self.status.config(text="Running...")
        self.run_btn.config(state="disabled")

        try:
            self.log("🔍 Scanning...")
            files = scan(self.folder_path)
            self.files_label.config(text=str(len(files)))

            self.log("🧬 Finding duplicates...")
            duplicates = find_duplicates(files)
            self.dup_label.config(text=str(len(duplicates)))

            if duplicates:
                self.log("🗑 Cleaning duplicates...")
                os.makedirs("trash", exist_ok=True)
                for f in duplicates:
                    shutil.move(f, "trash")

            self.log("📊 Classifying...")
            _, rare = classify(files)
            self.rare_label.config(text=str(len(rare)))

            if rare:
                self.log("🗜 Compressing...")
                compress(rare)

            self.log("☁ Uploading...")
            upload_to_drive("compressed")

            self.log("✅ Done!")

        except Exception as e:
            self.log(f"❌ Error: {e}")

        finally:
            self.progress.stop()
            self.status.config(text="Completed")
            self.run_btn.config(state="normal")


if __name__ == "__main__":
    root = tk.Tk()
    app = StorageApp(root)
    root.mainloop()