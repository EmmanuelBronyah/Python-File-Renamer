import os
import re


def main():
    """
    Executes the entire program.

    :return: Returns None.
    """
    right_path = True
    while right_path:
        path = get_path()
        if path != -1 and path is not None:
            do_renaming(path)
        else:
            if path == -1:
                print('Program ended.')
                right_path = False


def get_path():
    """
    Takes the path of where the files or folders to rename resides.

    :return: Returns the path if it is valid and returns -1 to exit.
    """
    user_folders = ['Desktop', 'Documents', 'Downloads', 'Music', 'Pictures', 'Videos']

    path = input(r'Enter the path to the directory where the files/folders you want to rename reside: ') or 'exit'

    user_folder_in_path = [user_folder for user_folder in user_folders if user_folder.lower() == path.lower()]
    user_folder_in_path = user_folder_in_path[0] if user_folder_in_path != [] else None

    if path == 'exit':
        return -1
    if any([os.path.isfile(path), os.path.isdir(path), user_folder_in_path]):
        if user_folder_in_path:
            path = os.path.join(os.path.expanduser('~'), user_folder_in_path)
            return path
        else:
            return path
    else:
        print('Invalid path.')


def do_renaming(path):
    """
    Takes the path as an argument and renames the files and folders within it.

    If the path points to a file, an error message is thrown.
    :param path: A path to the folder where the files and folders to be renamed exists.
    :return: Returns None.
    """
    try:
        for obj in os.listdir(path):
            obj_split = re.split(r'[,.+|\s\\%$*_#@~-]+', obj)
            new_obj_name = '-'.join(obj_split)
            os.rename(os.path.join(path, obj), os.path.join(path, new_obj_name.lower()))
        print('Files/folders renamed.')
    except NotADirectoryError:
        print('Path provided must point to a directory.')


if __name__ == '__main__':
    main()
