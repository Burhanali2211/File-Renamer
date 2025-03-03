import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import threading
import re
import json
from concurrent.futures import ThreadPoolExecutor
from mutagen.easyid3 import EasyID3
from PIL import Image
from PIL.ExifTags import TAGS


def get_exif_data(image_path):
    try:
        image = Image.open(image_path)
        exif_data = image._getexif()
        if exif_data:
            return {TAGS.get(tag, tag): value for tag, value in exif_data.items()}
    except Exception:
        pass
    return {}


def rename_files(target_directory, old_extensions, new_extension, regex_pattern, use_metadata, preview=False):
    log = []
    old_extensions = [ext.strip() for ext in old_extensions.split(',')]
    regex = re.compile(regex_pattern) if regex_pattern else None

    for root, dirs, files in os.walk(target_directory):
        for file in files:
            file_path = os.path.join(root, file)
            base, ext = os.path.splitext(file)

            if ext in old_extensions or not old_extensions:
                new_name = base

                if regex:
                    new_name = regex.sub('', new_name)

                if use_metadata and ext.lower() in ['.jpg', '.jpeg', '.png']:
                    exif = get_exif_data(file_path)
                    if 'DateTime' in exif:
                        new_name = exif['DateTime'].replace(
                            ':', '-').replace(' ', '_')

                elif use_metadata and ext.lower() == '.mp3':
                    try:
                        audio = EasyID3(file_path)
                        new_name = f"{audio['artist'][0]} - {audio['title'][0]}"
                    except Exception:
                        pass

                new_file_path = os.path.join(
                    root, f"{new_name}{new_extension}")
                if not preview:
                    # Backup original
                    shutil.copy(file_path, f"{file_path}.bak")
                    os.rename(file_path, new_file_path)
                    log.append((file_path, new_file_path))

    with open('rename_log.json', 'w') as f:
        json.dump(log, f, indent=4)

    return log


def restore_files():
    try:
        with open('rename_log.json', 'r') as f:
            log = json.load(f)

        for original, renamed in log:
            if os.path.exists(f"{original}.bak"):
                shutil.move(f"{original}.bak", original)
                os.remove(renamed)

        messagebox.showinfo("Restore", "Files restored successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to restore: {e}")


def start_renaming():
    directory = dir_entry.get()
    old_ext = ext_entry.get()
    new_ext = new_ext_entry.get()
    regex = regex_entry.get()
    use_metadata = metadata_var.get()

    if not directory:
        messagebox.showerror("Error", "Please select a directory")
        return

    with ThreadPoolExecutor() as executor:
        executor.submit(rename_files, directory, old_ext,
                        new_ext, regex, use_metadata)

    messagebox.showinfo("Success", "Renaming completed!")


def browse_directory():
    folder_selected = filedialog.askdirectory()
    dir_entry.delete(0, tk.END)
    dir_entry.insert(0, folder_selected)


def preview_changes():
    directory = dir_entry.get()
    old_ext = ext_entry.get()
    new_ext = new_ext_entry.get()
    regex = regex_entry.get()
    use_metadata = metadata_var.get()

    preview_log = rename_files(
        directory, old_ext, new_ext, regex, use_metadata, preview=True)
    preview_text.delete('1.0', tk.END)
    preview_text.insert(tk.END, "Preview of Changes:\n\n")
    for old, new in preview_log:
        preview_text.insert(tk.END, f"{old} -> {new}\n")


def toggle_theme():
    theme = style.theme_use()
    style.theme_use("clam" if theme == "default" else "default")


app = tk.Tk()
app.title("Advanced File Renamer")
app.geometry("600x500")

style = ttk.Style()
style.theme_use("default")

frame = ttk.Frame(app, padding=10)
frame.pack(expand=True, fill='both')

ttk.Label(frame, text="Select Directory:").grid(row=0, column=0, sticky='w')
dir_entry = ttk.Entry(frame, width=50)
dir_entry.grid(row=0, column=1)
ttk.Button(frame, text="Browse", command=browse_directory).grid(
    row=0, column=2)

ttk.Label(frame, text="Current Extensions (comma separated):").grid(
    row=1, column=0, sticky='w')
ext_entry = ttk.Entry(frame)
ext_entry.grid(row=1, column=1)

ttk.Label(frame, text="New Extension:").grid(row=2, column=0, sticky='w')
new_ext_entry = ttk.Entry(frame)
new_ext_entry.grid(row=2, column=1)

ttk.Label(frame, text="Regex Pattern (optional):").grid(
    row=3, column=0, sticky='w')
regex_entry = ttk.Entry(frame)
regex_entry.grid(row=3, column=1)

metadata_var = tk.BooleanVar()
ttk.Checkbutton(frame, text="Use Metadata for Naming",
                variable=metadata_var).grid(row=4, column=1, sticky='w')

progress = ttk.Progressbar(frame, mode='indeterminate')
progress.grid(row=5, column=0, columnspan=3, sticky='ew', pady=5)

ttk.Button(frame, text="Preview Changes",
           command=preview_changes).grid(row=6, column=0)
ttk.Button(frame, text="Rename Files",
           command=start_renaming).grid(row=6, column=1)
ttk.Button(frame, text="Restore Files",
           command=restore_files).grid(row=6, column=2)

ttk.Button(frame, text="Toggle Theme",
           command=toggle_theme).grid(row=7, column=1)

preview_text = tk.Text(frame, height=10, wrap='word')
preview_text.grid(row=8, column=0, columnspan=3, sticky='ew')

app.mainloop()
