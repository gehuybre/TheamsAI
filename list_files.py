import os

def list_files(directory):
    try:
        files = os.listdir(directory)
        for file in files:
            print(file)
    except FileNotFoundError:
        print(f"The directory {directory} does not exist.")

if __name__ == "__main__":
    directory = r"assets\images"
    list_files(directory)