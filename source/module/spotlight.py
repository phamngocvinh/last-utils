import os
import shutil
import sys
from PIL import Image
from datetime import datetime


# Get Windows Lockscreen Spotlight Wallpaper
def get_spotlight(ext: str = "png", output_path: str = "", prefix: str = "", is_include_phone: bool = False):
    # get windows version
    win_ver = sys.getwindowsversion()
    # check Windows version
    if win_ver.major == 10 and win_ver.major == 11:
        print("Only support Windows 10 and Windows 11")
        return 1

    # get current datetime
    now = datetime.now()

    # if output path not set
    if not output_path:
        output_path = "spotlight_" + now.strftime("%Y%m%d%H%M%S")

    # create folder if not exist
    if not os.path.exists(output_path):
        os.mkdir(output_path)

    # get spotlight path
    spotlight_path = os.path.expandvars(
        r"%localappdata%\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets"
    )

    # get the list of files in the spotlight directory
    src_files = os.listdir(spotlight_path)

    # loop over the files and copy them to the destination directory
    for file_name in src_files:
        base_name, old_extension = os.path.splitext(file_name)
        src_file = os.path.join(spotlight_path, file_name)
        dst_file = os.path.join(output_path, prefix + base_name + "." + ext)

        # copy only files
        if os.path.isfile(src_file):
            shutil.copy(src_file, dst_file)

    # delete image with resolution lower than 1080
    for file_name in output_path:
        file = os.path.join(output_path, file_name)

        if os.path.isfile(file):
            im = Image.open(file)
            width, height = im.size

            if is_include_phone:
                if width != 1080 and height != 1080:
                    os.remove(file)
            else:
                if width != 1080:
                    os.remove(file)

    # if cannot get wallpaper, delete output folder and return error
    if len([name for name in os.listdir(output_path) if os.path.isfile(name)]) == 0:
        os.rmdir(output_path)
        print("No spotlight wallpaper was found")
        return 1

    print("Spotlight wallpaper created at " + output_path)
    return 0
