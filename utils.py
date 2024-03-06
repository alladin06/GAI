import os

def get_subdirs(b='.'):
    '''
        Returns all sub-directories in a specific Path
    '''
    result = []
    for d in os.listdir(b):
        bd = os.path.join(b, d)
        if os.path.isdir(bd):
            result.append(bd)
    return result


def get_detection_folder():
    '''
        Returns the latest folder in runs\detect
    '''
    try:
        return max(get_subdirs(os.path.join('runs', 'detect')), key=os.path.getmtime)
    except ValueError:
        # Handle the case where no subdirectories are found
        print("No 'detect' subdirectories found.")
        return None

def check_folders():
    paths = {
        'data_path': 'data',
        'images_path': 'data/images',
        'videos_path': 'data/videos',
    }
    # Check whether the specified path exists or not
    notExist = [path for path in paths.values() if not os.path.exists(path)]

    if notExist:
        print(f'Folders {notExist} do not exist. We will create them.')
        # Create a new directory because it does not exist
        for folder in notExist:
            try:
                os.makedirs(folder)
                print(f"The new directory {folder} is created!")
            except OSError as e:
                print(f"Error creating directory {folder}: {e}")

# Example usage:
check_folders()
detection_folder = get_detection_folder()
if detection_folder:
    print(f"Latest detection folder: {detection_folder}")
