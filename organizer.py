import os
import shutil
import tkinter

try:
    extension_dirs = {
    ".txt": "Text Files",
    ".pdf": "PDF Files",
    ".doc": "Word Documents",
    ".docx": "Word Documents",
    ".xls": "Excel Files",
    ".xlsx": "Excel Files",
    ".ppt": "PowerPoint Presentations",
    ".pptx": "PowerPoint Presentations",
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".mp3": "Audio Files",
    ".wav": "Audio Files",
    ".mp4": "Video Files",
    ".avi": "Video Files",
    ".m4a": "Audio Files",
    ".exe": "executables"
    
}

    # Path to your desktop (change this to your actual desktop path)
    desktop_path = os.path.join(os.path.expanduser("~"), "C:/Users/user/Desktop")


    # Create the directories if they don't exist
    for dir_name in extension_dirs.values():
        dir_path = os.path.join(desktop_path, dir_name)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

# List all files in the desktop
    for item in os.listdir(desktop_path):
        item_path = os.path.join(desktop_path, item)
    
# Check if it's a file (not a folder)
        if os.path.isfile(item_path):
# Split the file extension
            _, ext = os.path.splitext(item)
            print(f"File: {item}, Extension: {ext}")
        
            if ext in extension_dirs:
                target_dir =os.path.join(desktop_path, extension_dirs[ext])
                shutil.move(item_path, target_dir)
                
except FileExistsError as e:
    print(f"file or folder already exists: {e}")
except PermissionError as e:
    print(f"You do not have the recquired access: {e}")
except Exception as e:
    print(f"An unexpected error occurred ): {e}")
        
print("Organization complete")


#setting up tikinter
root = tkinter.Tk()
root.title("Desktop Organizer")
root.geometry("500x300")
root.title("Desktop Organizer")
root.configure(bg="#f0f0f0")  # Light gray background

#label to display compeletion message
Label = tkinter.Label(root, text="Organization Complete")
Label.pack()
Label.configfont=("Helvetica", 12)

#button that closes the window
button = tkinter.Label(root, text="Close window", command = root.quit())
button.pack()

root.mainloop()


