## Global Team Configuration

Always load these config layers:

(1) Project user config

(2) Project config

Also fall back to these if useGlobal flag is set:

(3) Global user config

(4) Global config

### Scenarios

(1) Project user config: "my_zosmf" profile defines `"host": "example1.com"`

(2) Project config: "my_zosmf" profile defines `"host": "example2.com", "port": 1443`

OR

(3) Global user config: "my_zosmf" profile defines `"host": "example1.com"`

(4) Global config: "my_zosmf" profile defines `"host": "example2.com", "port": 1443`

should be loaded as:

`"host": "example1.com", "port": 1443`

---

(2) Project config: "my_zosmf" profile defines `"host": "example1.com"`

(4) Global config: "my_zosmf" profile defines `"host": "example2.com", "port": 1443`

should be loaded as:

`"host": "example1.com"`

---

(2) Project config: "my_zosmf" profile of type zosmf defines `"host": "example1.com"`

(4) Global config: "my_base" profile of type base defines `"host": "example2.com", "port": 1443`

should be loaded as:

`"host": "example1.com", "port": 1443`

## Session Refactoring

Suggest to work on as a collaborative effort :)

[S] Create the Session class

Should store connection properties including session type (basic or token)

```
class Session:
    def __init__(self, host=None, port=443, protocol="https", user=None, password=None,
            tokenType=None, tokenValue=None, rejectUnauthorized=False):
        if user is not None and password is not None:
            self.user = user
            self.password = password
            self.type = "basic"
            pass # Then we have a session with basic auth
        elif tokenType is not None and tokenValue is not None:
            self.type = "token"
            pass # Then we have a session with token auth
        else:
            raise "An authentication method must be supplied"
    
    @property
    def host_url():
         return f"{self.protocol}://{self.host}:{self.port}"
```

---

[R] In the SdkApi code, replace all references to `connection` with `session`

Also support multiple session types for authentication

```
        self.request_arguments = {
            "url": self.request_endpoint,
            "headers": self.default_headers
        }
        if session type is basic:
            request_arguments "auth" = (self.connection.user, self.connection.password),
        elif session_type is token:
            request_arguments "auth" = token
```

Don't load ZosmfProfile in the constructor
```
        if "plugin_profile" in connection:
            self.connection = ZosmfProfile(connection['plugin_profile']).load()
        else:
            self.connection = ApiConnection(**connection)
```
The above can be replaced with something like the following:
```
        self._profile = profile
        self._session = Session(**profile)
```

---

[Both] Update integration tests to use team config

In tests that use a connection dict to load profile like this:
```
        self.connection_dict = {"plugin_profile": test_profile}
        self.console = Console(self.connection_dict)
```
Replace with something like the following:
```
        self.profile_dict = ZosmfProfile(test_profile).load()
        self.console = Console(self.profile_dict)
```
Instead of `ZosmfProfile`, load v2 team config with the `ProfileManager` class.
