# File handling in Python
def read_file(file_path):
    """Reads the content of a file and returns it."""
    with open(file_path, 'r') as file:
        content = file.read()
    return content


def write_file(file_path, content):
    """Writes content to a file."""
    with open(file_path, 'w') as file:
        file.write(content)


def append_file(file_path, content):
    """Appends content to a file."""
    with open(file_path, 'a') as file:
        file.write(content)

def delete_file(file_path):
    """Deletes a file."""
    import os
    if os.path.exists(file_path):
        os.remove(file_path)
    else:
        print("The file does not exist.")

def file_exists(file_path):
    """Checks if a file exists."""
    import os
    return os.path.exists(file_path)

def list_files(directory):
    """Lists all files in a directory."""
    import os
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]


def create_directory(directory):
    """Creates a new directory."""
    import os
    if not os.path.exists(directory):
        os.makedirs(directory)
    else:
        print("The directory already exists.")

        
def delete_directory(directory):
    """Deletes a directory."""
    import os
    import shutil
    if os.path.exists(directory):
        shutil.rmtree
