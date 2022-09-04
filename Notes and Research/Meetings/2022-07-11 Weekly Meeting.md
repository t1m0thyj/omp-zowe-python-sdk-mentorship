* Action items
  * Timothy
    * Get someone from team as a second reviewer for enhancement PRs
    * Check with Mark about z/OSMF endpoint to obtain tokens
  * Richard
    * Done - Wrap up PR #92
    * Done - Finish draft of Project Design doc
    * In Progress - SdkApi class (see [here](https://github.com/t1m0thyj/omp-zowe-python-sdk-mentorship/blob/master/Notes%20and%20Research/Meetings/2022-06-28%20Profile%20Discussion.md))
  * Soumik
    * Done - Fix automated tests for PR #96
    * Done - Finish draft of Project Design doc
    * In Progress - Add unit tests for exception on PR #96
    * In Progress - Session class (see [here](https://github.com/t1m0thyj/omp-zowe-python-sdk-mentorship/blob/master/Notes%20and%20Research/Meetings/2022-07-07%20Profile%20Discussion.md))
  * Next Steps
    * Submit weekly status reports as PRs (Week 3 = Jul 4-Jul 10)
    * Review test fixture updates on PR #95
      * Timothy - Log tests that fail and send Slack message
      * Someone else - Verify that tests pass with changes from this PR

**Question:** How should SdkApi class initialize profiles?

Currently, it is done like this:
```
connection = {"plugin_profile": "my_zosmf"}
my_files = Files(connection)
```

In the future, to load v1 profiles (YAML files in ~/.zowe directory):
```
profile = ZosmfProfile("my_zosmf").load()
my_files = Files(profile)
```

In the future, to load v2 profiles (team config in zowe.config.json):
```
profile = ProfileManager.load("zosmf", "my_zosmf")
my_files = Files(profile)
```

So the SdkApi doesn't need to initialize the profile, it will already be loaded.

**Question:** What should be done with the default_url parameter?

Previous example was missing `default_url`:
```
class SdkApi:
    def __init__(self, profile, default_url):
        self._profile = profile
        self._session = Session(**profile)
```

Classes that extend it will supply the default URL:
```
class Files(SdkApi):
    def __init__(self, profile):
        super().__init__(profile, "/zosmf/restfiles/")
```

**Question:** What should be done with the constants object?

Ok to remove `self.constants = constants` line from SdkApi

In scripts that use constants, they can import them directly

**Question:** How will tokens be passed to z/OSMF?

Some z/OSMF requests return tokens in the response header.

This token can be used for authentication instead of user/password.

It should be passed as a "bearer token" with the requests package.
