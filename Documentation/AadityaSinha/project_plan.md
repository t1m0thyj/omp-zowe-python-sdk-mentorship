**Student's Name:** Aaditya Sinha

**Mentor:** Fernando Rijo Cedeno, Timothy Johnson

**Project:** OMP Zowe Python SDK Mentorship

**Project Description:** Finalize team configuration support and make other enhancements to support a v2 release.

**Problem Definition:** The Zowe Python SDK is missing the following:
- APIs for interacting with z/OSMF Files and Jobs that are present in the Node.js SDK.
- APIs to load and save properties in Zowe team configuration files and the user's environment.
- Sample SDK for extenders who want to create a Python SDK for other mainframe APIs besides z/OSMF.

The first two items are prerequisites for a stable 1.0 release, and the last item is a stretch goal.

**Deliverables:**
1. Add APIs for interacting with z/OSMF Files and Jobs.
2. Implement APIs to load and save properties in Zowe team configuration files and the user's environment.
3. Create a sample SDK for extenders to develop Python SDKs for other mainframe APIs.

**Coding Plan:**

| Week | Tasks | Goals |
|------|-------|-------|
| Week 1 | <li> Familiarize with the existing Zowe Python SDK codebase.<li> Set up the development environment.<li> Added method to change the job class in [zos_jobs] <li> Added unit & integeration tests  | Add method to change the job class |
| Week 2 | <li> Added utility method for hold/release jobs method in [zos/jobs].<li> Write unit & integeration tests | [zos-jobs] Add methods to hold/release a job |
| Week 3 | <li> Created a utility method `_issue_job_request` <li> Refactored the `change_job_class` method | [zos-jobs] Add methods to hold/release a job |
| Week 4 | <li> Auto detect schema filename from $schema property in the config file - filepath or internet_url | [core] Validate that zowe.config.json file matches schema |
| Week 5 | <li> Move the validation logic into the ProfileManager class as opt-in behavior to auto-validate when profiles are loaded | [core] Validate that zowe.config.json file matches schema |
| Week 6 | <li> Work on 4 Scenarios: - <br> 1. Missing $schema property <br> If the schema property is not defined than it will be better option to raise a warning <br> 2. Invalid $schema <br> When an invalid instance is encountered, a ValidationError will be raised or returned, depending on which method or function is used. <br> 3. Valid $schema <br> Run the validate function and throw error for any validation fails <br> 4. Have a flag to disable $schema validaiton <li> Create unit and integeration tests for the implementation | [core] Validate that zowe.config.json file matches schema |
| Week 7 | <li> When loading a profile from team config, have an opt-in flag to support loading of properties from environment variables. <li> Ex:- `ZOWE_OPT_USER` and `ZOWE_OPT_PASSWORD` to load user and passwords securely | Load profile properties from environment variables |
| Week 8 | <li> Create a list from schema and only load those properties <li> Override the properties in the config json file <li> The priority order should be command_line -> env_variables -> service_type_profiles -> base_type_profiles <li> Create unit and integeration tests for the implementation | Load profile properties from environment variables |
| Week 9-10 | <li> In the previous PR for nested config we have successfully loaded the nested profiles but it was failing to load the `user` and `password` for the base profile <li> The ProfileManager.load method loops through config files in the following order: <br> Project User Config -> Project Config -> Global User Config  -> Global Config <li> Merge all the layers together then load the profile properties from the resulting merged object <li> Create unit and integeration tests for the implementation | Fix profile merge order to match Node.js SDK |
| Week 11 | <li> Refactor the `ProfileManager.load` <li> Create unit and integeration tests for the implementation | Fix profile merge order to match Node.js SDK |
| Week 12 | <li> Final presentation | Wrap up the work |
<!--| Week 7 | | |
| Week 8 |||
| Week 9 | . | |
| Week 10 |  ||--!>
