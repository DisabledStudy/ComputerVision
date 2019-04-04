import os


def clear_one_session_dir(special_foler = ''):
    path = os.path.normpath('one_session_dir\\' + special_foler)
    for any_file in os.listdir(path):
        os.remove(os.path.join(path,any_file))


def get_jpg_files_in_dir(path):
    """возвращает список jpg файлов в каталоге"""
    jpg_files = [os.path.join(path, jpg) for jpg in os.listdir(path) if jpg.endswith('.jpg')]
    return jpg_files
