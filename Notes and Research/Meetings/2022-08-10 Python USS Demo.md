1. Figure out how to get Python installed
Currently are getting errors both from Zowe CLI and TSO methods
Timothy will reach out to Mark to debug further

2. Install the Python SDK in USS
Richard and Timothy will work together on this

3. Test that Python SDK is installed and can connect to z/OSMF

**Note:** We may need to add SDK directory to `sys.path`
```python
from zowe.zosmf_for_zowe_sdk import Zosmf

profile = {
    "host": "localhost",
    "port": 10443,
    "user": "",
    "password": "",
    "rejectUnauthorized": False
}

my_zosmf = Zosmf(profile)
print(my_zosmf.get_info())
```

4. Set up files needed for the demo:
- Python script to create (if it doesn't exist) and mount ZFS
- zowe.config.json (similar to what we've used so far but with localhost)
- zowe.config.user.json (to hide secure fields: user and password)

**Note:** If we can't get Python set up on USS, then Step 4 could be done on local machine.
