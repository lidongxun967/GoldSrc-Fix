import os
import string
import shutil

import os

def find_sdl2_dll_folders(root_path, dll_filename="SDL2.dll"):
    sdl2_dll_folders = []
    seen_dirs = set()

    # 遍历根文件夹
    for dirpath, dirnames, filenames in os.walk(root_path):
        # 检查是否是一级子文件夹，不是则跳过
        if dirpath != root_path and os.path.dirname(dirpath) != root_path:
            continue

        # 如果当前文件夹包含SDL2.dll，则将其绝对路径添加到列表中
        if dll_filename in filenames and dirpath not in seen_dirs:
            sdl2_dll_folders.append(os.path.abspath(dirpath))
            seen_dirs.add(dirpath)

        # 从遍历中排除二级子文件夹
        for dirname in dirnames[:]:
            dir_to_exclude = os.path.join(dirpath, dirname)
            if os.path.dirname(dir_to_exclude) != root_path:
                dirnames.remove(dirname)

    return sdl2_dll_folders


def find_steam_common_folders():
    steam_common_folders = []

    # 检查C盘下的SteamLibrary\steamapps\common文件夹
    c_drive = "C:\\"
    steam_common_path_c = os.path.join(c_drive, "Program Files (x86)", "Steam", "steamapps", "common")
    if os.path.exists(steam_common_path_c):
        steam_common_folders.append(os.path.abspath(steam_common_path_c))

    # 获取所有硬盘盘符
    drives = [drive + ":\\" for drive in string.ascii_uppercase if os.path.exists(drive + ":")]

    # 在每个盘符下查找SteamLibrary\steamapps\common文件夹
    for drive in drives:
        steam_common_path = os.path.join(drive, "SteamLibrary", "steamapps", "common")
        if os.path.exists(steam_common_path):
            steam_common_folders.append(os.path.abspath(steam_common_path))

    return steam_common_folders

def find():
    atf=find_steam_common_folders()
    gsf=[]
    for i in atf:
        gsf += find_sdl2_dll_folders(i)
    return gsf


def backup_and_copy_sdl2_dll(target_path):
    # 获取SDL2.dll的完整路径
    source_dll = os.path.join(os.getcwd(), "SDL2.dll")
    
    # 备份目标路径下的SDL2.dll
    target_dll = os.path.join(target_path, "SDL2.dll")
    target_dll_backup = os.path.join(target_path, "SDL2.dll.bak")
    if os.path.exists(target_dll_backup):
        os.remove(target_dll_backup)
    
    if os.path.exists(target_dll):
        os.rename(target_dll, target_dll_backup)

    # 复制当前目录下的SDL2.dll到目标路径
    shutil.copy(source_dll, target_path)

def list_to_dict_and_list(input_list):
    result_dict = {}
    result_list = []

    for path in input_list:
        folder_name = os.path.basename(path)
        name = folder_name.split("\\")[-1]
        result_dict[name] = path
        result_list.append(name)

    return result_dict, result_list

