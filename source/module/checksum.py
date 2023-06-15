import hashlib
import os.path


def run_checksum(path: str, algorithm: str):

    is_file = False
    is_dir = False

    if os.path.isfile(path):
        is_file = True

    if os.path.isdir(path):
        is_dir = True

    if not is_file and not is_dir:
        print("Invalid path, please choose file or folder")
        return 1

    print("Checksum")
    return 0


def run_verify():
    return 0


def run_generate():
    return 0


if __name__ == '__main__':
    run_checksum()
