**Student's Name:** Abdul Samad Siddiqui

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
| Week 1 | Familiarize with the existing Zowe Python SDK codebase.<br>Set up the development environment.<br> Added methods to copy (dataset or member) & USS files in [zos/file]<br>Write unit & integeration tests  | Add method to copy data set or member |
| Week 2 | Modify the `list_dsn` function in the [zos/file].<br> Write unit tests for the `list_dsn` | [zos-files] `list_dsn` should have option to return attributes |
| Week 3 | Resolved comments & update the integeration test for `list_dsn`| Address the raised comments by refactoring the `list_dsn`, `copy_uss_to_dataset`, and `copy_dataset_or_member` functions |
| Week 4-5 | create a method to credential values from multiple fields, assemble them, and remove trailing null bytes<br>Write unit & integeration tests|Load secure values from multiple credential entries on Windows |
| Week 6 | Exam Break | Final Exams |
| Week 7 | Create or update profiles in the highest priority layer |[core]  Save profile properties to `zowe.config.json` file  |
| Week 8 | Implement secure property storage based on an `is_secure` check.| [core]  Save profile properties to `zowe.config.json` file  |
| Week 9 | Define properties and a profile in ProfileManager for the `profiles.zosmf` profile <br>Write unit & integeration tests| [core]  Save profile properties to `zowe.config.json` file  |
| Week 10 |Read and extract the secure properties from the `zowe.config.json` and `zowe.config.user.json` files.<br>Establish a connection to the vault and store the extracted secure properties.| [core] Save secure profile properties to vault|
| Week 11 | Implement encryption or secure storage mechanisms for the properties and handle error logging.<br> Create unit and integeration tests for the implementation |[core] Save secure profile properties to vault  |
| Week 12 | Final Presentation | Final Presentation|
