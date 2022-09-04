* Action items
  * Timothy
    * In Progress - Get someone from team as a second reviewer for enhancement PRs
      * Created items on my team's board to review Python SDK PRs
      * Suggest to put PR in draft mode until it is ready for review - n/a
    * Done - Send cURL command to retrieve z/OSMF token
    * Set up auto-generation of docs on the ReadTheDocs
      * Recommend to add docstrings to any new APIs
  * Richard
    * Done - Refactoring of SdkApi class
    * In Progress - Update tests for SdkApi class
      * New tests done, fixing existing unit tests
  * Soumik
    * Done - Add unit tests for exception on PR #96
    * Done - Implementation of Session class
    * In Progress - Update tests for Session class
      * Tests are done, will address PR feedback
  * Next Steps
    * Test using SdkApi with z/OSMF token instead of user/password
    * Submit weekly status reports as PRs (Week 5 = Jul 18-Jul 24)
    * Demo ideas - Investigate this week

Questions:
How should user config be loaded?
Filename - given an app name like "zowe", the project config filename is "<appName>.config.json" and the user config filename is "<appName>.config.user.json"
Flag to override - default behavior should be detect user config and override if present, ok to have flag to disable user config but not required
Config not always in same directory - should search up for both files, e.g. zowe.config.json in /a/b and zowe.config.user.json in /a/b/c
  
How should session handle properties
* ISession property should be host for consistency with profile property
* Protocol is not required, should default to `"https"`
* Port should not be required, default is `443`
* Reject unauthorized, default is true
