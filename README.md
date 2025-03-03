# Advanced File Renamer

## 📌 Overview
The **Advanced File Renamer** is a powerful tool that allows users to rename files in bulk using a user-friendly GUI. It supports multi-threading for fast processing, regex pattern filtering, metadata-based naming (EXIF for images, ID3 for MP3), preview mode, and backup/restore functionality.

## 🚀 Features
- **Graphical User Interface (GUI)** for ease of use.
- **Multi-threading** for high-speed renaming.
- **Metadata Extraction**:
  - Uses **EXIF** data for images.
  - Uses **ID3 tags** for MP3 files.
- **Regex Filtering**: Modify file names based on regular expressions.
- **Preview Mode**: See changes before applying them.
- **Backup & Restore**: Automatically backs up files before renaming, allowing easy restoration.
- **Dark/Light Theme Toggle** for better user experience.
- **Supports all file types** and multiple extensions.

---

## 📂 Installation
### 🔹 Requirements
Ensure you have **Python 3.x** installed and the following dependencies:

```sh
pip install pillow mutagen
```

### 🔹 Run the Application
Clone this repository and run the script:

```sh
git clone https://github.com/Burhanali2211/File-Renamer/.git
cd File-Renamer
python advanced_file_renamer.py
```

---

## 🛠️ How to Use
1. **Select a Directory**: Click `Browse` to choose the folder containing files to rename.
2. **Enter File Extensions**: Provide comma-separated extensions (e.g., `.txt,.jpg`).
3. **Set New Extension**: Define the new extension (e.g., `.mp3`).
4. **Use Regex (Optional)**: Enter a regex pattern to filter file names.
5. **Enable Metadata Naming**: Check this option if you want filenames based on metadata.
6. **Preview Changes**: Click `Preview Changes` to see the modifications before applying them.
7. **Rename Files**: Click `Rename Files` to execute the renaming process.
8. **Restore Files**: If needed, click `Restore Files` to revert changes.

---

## 🎯 Example Usage
### 🔹 Scenario 1: Rename `.jpg` files based on EXIF data
- Set `Current Extensions`: `.jpg,.jpeg`
- Enable `Use Metadata for Naming`
- Click `Rename Files`

### 🔹 Scenario 2: Change `.txt` to `.md` and remove numbers from names
- Set `Current Extensions`: `.txt`
- Set `New Extension`: `.md`
- Use `Regex Pattern`: `\d+` (removes numbers)
- Click `Rename Files`

---

## ⚙️ Supported File Types
| File Type | Metadata Support |
|-----------|-----------------|
| Images (`.jpg`, `.jpeg`, `.png`) | Uses EXIF data |
| Audio (`.mp3`) | Uses ID3 tags |
| Other files | Normal renaming |

---

## 🔄 Backup & Restore
- **Backup**: The script creates a `.bak` copy before renaming files.
- **Restore**: Click `Restore Files` to revert files to their original names.

---


## 📜 License
This project is open-source and available under the **MIT License**.

---

## 🤝 Contributing
Feel free to submit pull requests and suggestions to improve this tool!

---

## 📧 Contact
For issues or improvements, reach out at **gamingcristy19@gmail.com** or open an issue in the repository.

---

Happy Renaming! 🚀

