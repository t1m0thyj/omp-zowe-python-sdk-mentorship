from zowe.zosmf_for_zowe_sdk import Zosmf
from zowe.zos_files_for_zowe_sdk import Files
import os


password = os.environ.get('PASSWORD')
user = os.environ.get('USER')

profile = {
    "host": "zzow03.zowe.marist.cloud",
    "port": 10443,
    "user": user,
    "password": password,
    "rejectUnauthorized": False
}

files = Files(profile)
file_system_name = "MENTEE1.DEMO.FILE.ZFS"
create_zos_options = {"perms": 755,"cylsPri": 10,"cylsSec": 2,"timeout": 20, "volumes": ["VPMVSC"]}
mount_zos_file_system_options = {"fs-type": "ZFS", "mode": "rdonly"}
mount_point = mount_point = f"/u/mentee1/mount"


# Create, mount and list a zos file system
files.create_zFS_file_system(file_system_name, create_zos_options)
files.mount_file_system(file_system_name, mount_point, mount_zos_file_system_options)
file_list = files.list_unix_file_systems(file_system_name=file_system_name)
print(file_list["items"][0]["name"])

# Unmount and delete a zos file system
# files.unmount_file_system(file_system_name)
# files.delete_zFS_file_system(file_system_name)
