* Action items
  * Richard
    * In Progress - Create and delete zFS filesystems
      * Unit tests needed for patch coverage
    * In Progress - Mount and unmount zFS filesystems
      * Will open PR after create/delete is merged
    * Next Steps - Issues related to migrated data sets
  * Soumik
    * In Progress - Load user config and global config
      * Code refactoring is done, wrapping up tests
  * Timothy
    * In Progress - Publish prerelease wheels to GitHub
    * Will find out schedule and details of final demo/presentation
  * Next Steps
    * Investigate how to format docstrings for ReadTheDocs and add to contributing guidelines
    * Demo prep
      * GUI for browsing data sets
        * Soumik is investigating upload/download demo with Kivy
      * Automation script to run in USS
        * Timothy will try to install Python SDK on z/OS
        * Once working, Richard should be unblocked to test Python scripts in USS
    * Submit weekly status reports as PRs (Week 9 = Aug 8-14)

Questions:
What should zos-files unit tests look like?

Example of z/OSMF API unit test:
```
    @mock.patch('requests.Session.send')
    def test_list_systems(self, mock_send_request):
        """Listing z/OSMF systems should send a REST request"""
        mock_send_request.return_value = mock.Mock(headers={"Content-Type": "application/json"}, status_code=200)
        Zosmf(self.connection_dict).list_systems()
        mock_send_request.assert_called_once()
```

1. Mock the REST request (headers, payload, etc)
2. Invoke the Python API
3. Verify REST method was called

Two unit tests: one for create API and one for delete API
