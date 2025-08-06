import os
import shutil
target_directory="target_dir"


def organize_files(target_dir):
    """
    Organizes files in the target directory into subfolders based on file types.
    
    Args:
        target_dir (str): Path to the directory to be organized
    """
    
    # File type categories and their corresponding extensions
    file_categories = {
        'Documents': ['.pdf', '.doc', '.docx', '.txt', '.rtf', '.xls', '.xlsx', '.ppt', '.pptx', '.odt'],
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.webp', '.tiff'],
        'Videos': ['.mp4', '.mov', '.avi', '.mkv', '.flv', '.wmv', '.webm'],
        'Audio': ['.mp3', '.wav', '.ogg', '.flac', '.aac', '.m4a'],
        'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz'],
        'Others': []  # Default category for unmatched files
    }
    
    # Create the subfolders if they don't exist
    for category in file_categories: 
        os.makedirs(os.path.join(target_dir, category), exist_ok=True)
                #exists ok=True tells the os.makedirs to not raise an error if the directory already exists
    
    # Getting all the files in the target directory
    files = [f for f in os.listdir(target_dir) 
    if os.path.isfile(os.path.join(target_dir, f))]# os.listdir returns a list of all files and directories in the target directory, os.path.isfile checks if the file is a file and not a directory

    moved_files = []
    # List to keep track of moved files
    
    for filename in files:
        file_ext = os.path.splitext(filename)[1].lower()
        moved = False
        #This part of the code gathers all files in the target directory, prepares to track which files are moved, and sets up for categorizing each file by its extension.
        
        # Finding the appropriate category for the file
        for category, extensions in file_categories.items():
            if file_ext in extensions:#checks if the file extension is in the list of extensions for that category
                src_path = os.path.join(target_dir, filename)
                dest_path = os.path.join(target_dir, category, filename)# os.path.join joins the target directory and the category and the filename
                
                # Move the file
                shutil.move(src_path, dest_path)
                moved_files.append((filename, category))# appends the filename and category to the moved_files list
                moved = True
                break
            #
        
        # If no category matched, move to 'Others'
        if not moved:
            src_path = os.path.join(target_dir, filename)
            dest_path = os.path.join(target_dir, 'Others', filename)
            shutil.move(src_path, dest_path)
            moved_files.append((filename, 'Others'))# appends the filename and 'Others' to the moved_files list
    
    return moved_files
#If a file doesn’t match any specific category, this code moves it to the "Others" folder and logs that action.
#This function organizes files in the target directory into subfolders based on their file types. It creates subfolders for documents, images, videos, audio files, archives, and others. It also returns a list of moved files with their new categories.

def print_results(results):#trying to create output in a table format
    """
    Prints the results of the file organization.
    
    Args:
        results (list): List of tuples containing (filename, category)
    """
    if not results:
        print("No files were moved.")
        return
    
    print("\nFile Organization Results:")
    print("-" * 40)
    print("{:<30} {:<10}".format("Filename", "Category"))
    print("-" * 40)
    
    for filename, category in results:
        print("{:<30} {:<10}".format(filename, category))#aligns the filename and category in a table format
    
    print("\nTotal files moved:", len(results))
    #Prints a table showing each file and the category it was moved to.
    #If no files were moved, it prints a message.
    #At the end, it prints the total number of files moved.


if __name__ == "__main__":
    import sys
    # sys is a module that provides access to some variables used or maintained by the interpreter and to functions that interact with the interpreter.
    
    if len(sys.argv) != 2:# checks if the number of command line arguments is not equal to 2
        print("Usage: python organize_files.py <target_directory>")
        sys.exit(1)
    
    target_directory = sys.argv[1]
    
    if not os.path.isdir(target_directory): # checks if the target directory is not a valid directory
        print(f"Error: '{target_directory}' is not a valid directory.")
        sys.exit(1)
    
    print(f"Organizing files in: {target_directory}")
    results = organize_files(target_directory)
    print_results(results)
    print("\nFile organization complete!")
    