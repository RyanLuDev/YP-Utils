import os
import pathlib
import hashlib

IMG_TYPE = []


def list_file(f_path: str, f_ext: list[str]) -> list[str]:
    exts = ['.'+ext for ext in f_ext]
    files: list[str] = []
    for f in os.listdir(f_path):
        ext = ''.join(pathlib.Path(f).suffixes)
        if ext in exts:
            files.append(f)
    return files


def list_file_path(f_path: str, f_ext: list[str]) -> list[str]:
    return [os.path.join(f_path, f) for f in list_file(f_path, f_ext)]


def list_imgs(f_path: str, f_ext: list[str] = IMG_TYPE) -> list[str]:
    return list_file(f_path, f_ext)


def lsit_imgs_path(f_path: str, f_ext: list[str] = IMG_TYPE) -> list[str]:
    return list_file_path(f_path, f_ext)


def mkdir(dirpath: str) -> None:
    if not os.path.exists(dirpath):
        os.makedirs(dirpath)


def hash(f_name: str) -> str:
    return ''


def sha256(filename: str) -> str:
    file_names = os.path.split(filename)
    file_path = ''
    if len(file_names) == 2 and file_names[0] == '':
        file_path = os.path.join(os.getcwd(), file_names[1])
    else:
        file_path = filename

    if os.path.exists(file_path):
        with open(file_path, 'rb') as f:
            sha256_obj = hashlib.sha256()
            sha256_obj.update(f.read())

            return sha256_obj.hexdigest()
    else:
        return 'Invalid File'
