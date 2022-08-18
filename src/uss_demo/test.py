from zowe.zosmf_for_zowe_sdk import Zosmf

profile = {
    "host": "zzow03.zowe.marist.cloud",
    "port": 10443,
    "user": "MENTOR1",
    "password": "MENTOR1",
    "rejectUnauthorized": False
}
print(Zosmf(profile).get_info())
