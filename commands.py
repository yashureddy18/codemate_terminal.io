import os
import psutil

def list_dir():
    return "\n".join(os.listdir())

def change_dir(path):
    try:
        os.chdir(path)
        return f"Changed directory to {os.getcwd()}"
    except FileNotFoundError:
        return f"No such directory: {path}"

def make_dir(name):
    try:
        os.mkdir(name)
        return f"Directory '{name}' created."
    except FileExistsError:
        return f"Directory '{name}' already exists."

def remove(path):
    try:
        if os.path.isdir(path):
            os.rmdir(path)
        else:
            os.remove(path)
        return f"Removed {path}"
    except Exception as e:
        return str(e)

def pwd():
    return os.getcwd()

def system_info():
    return f"CPU Usage: {psutil.cpu_percent()}% | Memory: {psutil.virtual_memory().percent}%"
