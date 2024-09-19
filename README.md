Desktop File Organizer
Project Overview

The Desktop File Organizer is a Python-based tool that helps organize files on your desktop automatically. It sorts files into designated folders based on their file types (e.g., images, documents, videos, etc.). This project aims to provide a simple, effective way to keep your desktop clutter-free.
Features

    Automatically organizes files by type (e.g., images, documents, videos, etc.).
    Supports various file formats like .jpg, .png, .pdf, .docx, .mp4, and more.
    Configurable folder structure: Users can define custom categories and destinations for specific file types.
    Runs as a standalone executable (built using PyInstaller) for ease of use without requiring Python to be installed on the user's system.

Project Structure

graphql

Desktop-File-Organizer/
│
├── src/
│ ├── organizer.py # Main script that runs the file organization
│ ├── config.py # Configuration file for defining file categories
│
├── build/ # Directory containing PyInstaller build outputs
│
├── README.md # Project documentation
├── LICENSE # License file
└── DesktopOrganizer.exe # Executable for running the application

How It Works

    File Scanning: The application scans the desktop directory for files.
    File Classification: Files are categorized based on their extensions.
    File Sorting: Files are moved into corresponding folders based on their types.
        Example: All .jpg and .png files are moved to the "Images" folder, .pdf files to the "Documents" folder, etc.

How to Use
Executable Version

    Download the DesktopOrganizer.exe file from the releases section.
    Run the executable.
    The application will automatically organize files on your desktop according to predefined categories.

Running from Source

    Clone the repository:

    bash

git clone https://github.com/yourusername/Desktop-File-Organizer.git

Install the required dependencies:

bash

pip install -r requirements.txt

Run the organizer:

bash

    python src/organizer.py

Building the Executable

If you want to create the executable yourself, follow these steps:

    Install PyInstaller:

    bash

pip install pyinstaller

Create the executable:

bash

    pyinstaller --onefile src/organizer.py

The output executable will be available in the dist/ folder.
Configuration

The file organizer can be customized by modifying the config.py file. This allows you to define different file types and their corresponding destination folders.

Example:

python

file_types = {
"Images": [".jpg", ".jpeg", ".png", ".gif"],
"Documents": [".pdf", ".docx", ".txt"],
"Videos": [".mp4", ".avi", ".mkv"],
}

You can add more categories or change folder paths as per your needs.
Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.
License

This project is licensed under the MIT License. See the LICENSE file for more details.
