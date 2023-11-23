# Python File Renamer.
This command-line python program renames files or folders in
a directory by a format where file and folder names are 
converted to lowercase and separated with a hyphen.

## Features of the file renamer.
* **Takes a path:** The program takes a path to the directory where 
the files/folders you want to rename resides. Hitting the enter
key, that is, leaving the path empty will cause the program
to quit. Directories and files located at where the path
points are then renamed. An error is thrown if the path provided
is not valid.
* **Error prompt:** An error message is printed to the screen 
if the path provided does not point to a directory or if
an invalid path is provided.

## Getting started
1. **Clone the repository to your machine.**
```shell
git clone https://github.com/EmmanuelBronyah/Python-File-Renamer.git
```
2. **Navigate to the project directory.**
```shell
cd file-folder-renamer
```
3. **Run the program.**
```shell
python file_folder_renamer.py
```

## Usage
* When the program is run, there will be a prompt to provide
a path where the folders/files to be renamed resides. The
program renames all the folders/files by a 
format where the names are converted to lowercase and a 
hyphen is used to separate the names.

## Example
1. **Providing a valid path which points to a folder.**
```shell
Enter the path to the directory where the files/folders you want to rename reside: C:\Users\{your-username}\Desktop\{foldername}
Files/folders renamed.
```
2. **Providing a path which points to a file.**
```shell
Enter the path to the directory where the files/folders you want to rename reside: C:\Users\{your-username}\Desktop\{foldername}\{filename}
Path provided must point to a directory.
```
3. **Providing an invalid.**
```shell
Enter the path to the directory where the files/folders you want to rename reside: 2938yd
Invalid path.
```

# License
This project is licensed under the MIT license.

# Acknowledgements
* Built by Bronyah Emmanuel.