* Introduction
  * Weekly meeting time - Mon 10am
  * Known time off
    * Soumik - mid-July (15-20) for 2-3 days
* Expectations
  * ~30 hrs a week
  * Weekly status report - put them in "Status Reports" folder
  * Project design due Jul 15
  * Project allocation
    * [z/OSMF Files and Jobs APIs](https://github.com/zowe/zowe-client-python-sdk/milestone/35)
    * [Zowe v2 Team Configuration](https://github.com/zowe/zowe-client-python-sdk/milestone/36)
* Access to contribute
  * GitHub repository
    * Mentorship repo - direct access
    * Python SDK repo - create forks from `next` branch
  * z/OS Marist system
* Get acquainted with Zowe
  * z/OSMF REST API (z/OS Management Facility)
    * Can test APIs with cURL or [Postman](https://www.postman.com/product/rest-client/)
      * Disable SSL certificate validation
      * Pass header X-CSRF-ZOSMF-HEADER
  * [Zowe Explorer](https://marketplace.visualstudio.com/items?itemName=Zowe.vscode-extension-for-zowe) (VS Code extension) to access
    * Data sets
    * Unix System Services (USS)
    * Jobs
  * Team configuration to store connection details
    * `zowe.config.json` - Simple team config
    * `zowe.schema.json` - Schema file to provide IntelliSense
    * `zowe.config.nested.json` - Sample nested config
* Action items
  * Timothy
    * Send out connection info
    * Set up Slack channel
    * Set up GitHub repo
    * Merge SDK pull requests
  * Richard - see below
  * Soumik - see below
* Getting started tasks
  * Report on code coverage in repo (Richard)
    * Document command to run unit tests and report on coverage
    * Set up automated coverage check that runs on PR builds (with GitHub Actions)
  * Implement a method that given a profile type, returns connection details for that profile (Soumik)
    * For example: given the profile type "zosmf", load all connection details from the default "zosmf" and "base" profiles in `zowe.config.json`
  * System test framework
    * For example: upload a test file to z/OS, and verify that downloading it returns the same file contents
