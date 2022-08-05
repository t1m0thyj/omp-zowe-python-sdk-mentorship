**Student's Name:** Richard Gregory

**Mentor:** Timothy Johnson

**Project:** Zowe Python SDK Enhancements for Zowe v2 

**Project Description:** There is growing interest in the Zowe Python SDK! The goal of the project is to make various enhancements to the Zowe Python SDK z/OSMF files and jobs.

**Problem Definition:** Mainframe users who want to easily interact with z/OSMF using Python do not have a feature-complete SDK.

**Deliverables:** By the end of the internship, the Files APIs in this [milestone](https://github.com/zowe/zowe-client-python-sdk/milestone/35) should be exposed in the SDK.

**Coding Plan**

| Week | Tasks | Goals |
|------|-------|-------|
| _Week 1_ | _• Document command to run unit tests and report on coverage. • Set up automated coverage check that runs on PR builds (with GitHub Actions)_ | _• Documented command to run unit tests and report on coverage.  • Partially set up automated coverage check that runs on PR builds (with GitHub Actions)_ |
| _Week 2_ | _• Set up automated coverage check that runs on PR builds (with GitHub Actions). • Start tackling z/OSMF Files and Jobs milestone - issues #81, #82 In pull request that fixes issues, add a system test to verify fix - [zos-files system test](https://github.com/zowe/zowe-client-python-sdk/blob/next/tests/integration/test_zos_files.py)_ | _• Done setting up an automated coverage check that runs on PR builds (with GitHub Actions). • Create a zowe profile for integration tests_ |
| _Week 3_ | _• Start tackling z/OSMF Files and Jobs [milestone](https://github.com/zowe/zowe-client-python-sdk/milestone/35)_ | _• Fixed issues that caused streaming requests to fail. Related to issues #81 and #82. • Added test coverage for `performed_streamed_request` method. • Work on project design_ |
| _Week 4_ | _• Wrap up implementing download and upload streamed data to dsn • Submit project plan_ | _• PR merged. • Project plan accepted_ |
| _Week 5_ | _• Implement SdkApi class that loads properties from a profile dictionary_ | _• New SdkApi merged to next branch_ |
| _Week 6_ | _• Update tests that use SdkApi_ | _• Test cases using the SdkApi updated and merged into next branch_ |
| _Week 7_ | _• Add method to create a zFS file system. • Add method to delete a zFS file system._ | _Methods merged into `next` branch_ |
| _Week 8_ | _• Add method to mount a z/OS file system. • Add method to unmount a z/OS file system. • Add method to list z/OS file systems._ | _Methods merged into `next` branch_ |
| _Week 9_ | _• Add method to migrate data set. • Add method to recall a migrated data set. • Add method to delete a migrated data set._ | _Methods merged into `next` branch_ |
| _Week 10_ | _• Add method to copy data set or member. • Add method to rename data set._ | _Methods merged into `next` branch_ |
| _Week 11_ | _• `delete_uss` should support recursive option._ | _Methods merged into `next` branch_ |
| _Week 12_ | _• Prepare presentation if needed and internship roundup_ | _Submit presentation if needed. Internship Concluded._ |
| ... | ... | ... |
