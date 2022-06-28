1. Handle all profile types (not just "zosmf") in ProfileManager class
    * It should accept `profile_name` AND/OR `profile_type`
    * If both are specified, load by name and validate the type
    * If only name is specified, load it (can be anything, e.g. "profile1")
    * If only type is specified, load the default profile for that type
    * If neither are specified, load base profile only and issue warning
2. Profile load method should return a dictionary
    * Contains properties resolved from `profile_type` profile, base profile, secure vault, etc.
    * No validation of properties needs to be performed here
    * Example of a profile dictionary:
    ```
    {
        "host": "example.com",
        "port": 443,
        "protocol": "https",
        "user": "XXX",
        "password": "XXX"
    }
    ```
3. Create `Session` class to replace `ApiConnection`
    * It can be instantiated with keyword args from profile (`Session(**profile)`)
    * Evaluation and validation of session-related properties can be performed here
    * For example, to validate authentication for the session:
    ```python
    class Session:
        def __init__(self, host=None, port=None, protocol=None, user=None, password=None,
                tokenType=None, tokenValue=None, rejectUnauthorized=False):
            if user is not None and password is not None:
                pass # Then we have a session with basic auth
            elif tokenType is not None and tokenValue is not None:
                pass # Then we have a session with token auth
            else:
                raise "An authentication method must be supplied"
    ```
4. `SdkApi` class should load properties from a profile dictionary
    * On the `__init__` method, `connection` argument should be renamed to `profile`
    * The profile can be stored, and used to create a session - for example:
    ```python
    class SdkApi:
        def __init__(self, profile):
            self._profile = profile
            self._session = Session(**profile)
    ```
    * Then specific APIs like `Files` and `Jobs` can access profile properties (`self._profile.get("encoding")`)
