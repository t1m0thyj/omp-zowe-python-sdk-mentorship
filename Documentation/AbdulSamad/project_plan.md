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
| Week 2 | Modify the `list_dsn` function in the [zos/file].<br> Write unit tests for the `list_dsn` & update the integeration test | [zos-files] `list_dsn` should have option to return attributes |
| Week 3 | Resolved comments | Address the raised comments by refactoring the `list_dsn`, `copy_uss_to_dataset`, and `copy_dataset_or_member` functions |
| Week 4 | Write a method to credential values from multiple fields, assemble them, remove trailing null bytes| Load secure values from multiple credential entries on Windows |
| Week 5 | Create or update profiles in the highest priority layer.<br>Implement secure property storage based on an `is_secure` check.<br>Define properties and a profile in ProfileManager for the "profiles.zosmf" profile.| Save profile properties to zowe.config.json file  |
| Week 6 | Exam Break | Final Exams |
<!--| Week 7 | | |
| Week 8 |||
| Week 9 | . | |
| Week 10 |  ||--!>
