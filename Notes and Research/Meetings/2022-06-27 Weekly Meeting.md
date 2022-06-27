* Action items
  * Timothy
    * Done - Set up GitHub repo
    * Done - Merge SDK pull requests
    * Done - Add contributor rights on GitHub repo
    * Fix the files.json and jobs.json fixtures
  * Richard
    * Done - Set up automated coverage check that runs on PR builds (with GitHub Actions)<br>
      CodeCov is set up now :)
    * In Progress - Start tackling z/OSMF Files and Jobs milestone - issues #81, #82<br>
      In pull request that fixes issues, add a system test to verify fix - [zos-files system test](https://github.com/zowe/zowe-client-python-sdk/blob/next/tests/integration/test_zos_files.py)
    * Questions:
      * System test error - Dataset not found error<br>
        The files.json fixture was pointing to a data set that does not exist, updating it to use `MENTOR1.PUBLIC.JCL(IEFBR14)` which does exist works.
      * System test error - Invalid keyword error for stream<br>
        Need to pass in stream as session arguments rather than request arguments, this can be accomplished with a new `perform_streamed_request` method.
    * Next steps: Fix/add integration tests to close issues #81, #82
  * Soumik
    * In Progress - Implement a method that given a profile type, returns connection details for that profile (#68)
    * In Progress - Load secure credentials from a profile (#70)
    * Questions:
      * Minimum Python version? (type hints added in 3.5)<br>
        Probably 3.6 is fine
      * When loading secure credentials, what paths should it look for?<br>
        For now, it should only look in the same path as the project config file
        For falling back to global config, that can be handled later when full support for layers is addeed in issue #71
      * Schema validation?<br>
        Let's focus on writing tests for first issues in the milestone first and get them closed out, this would be a nice stretch goal :)
      * Exception handling?<br>
        Good idea to add custom exception classes as needed
      * ApiConnection class used in v1? How should we handle other properties like tokenType and tokenValue in v2? Perhaps a new class?
        Scheduled meeting to discuss this tomorrow
    * Next steps: Add unit tests to close In Progress issues
  * Next Steps
    * Submit weekly status reports as PRs (Week 2 = Jan 20-26)
    * For pull requests on the SDK, at least 80% coverage on new code
    * Look at milestones to plan project design report
