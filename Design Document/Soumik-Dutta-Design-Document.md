# Team Config Support in Zowe Python SDK

## Motivation
Last version of Python SDK used to use different YAML files for different profile configuration. However the Nodejs SDK has moved on to JSON configs containing different profiles in one single file. There is also the concept of global and user configs for use for teams with multiple members and multiple roles. Hence to support such configs in Zowe Python SDK, we are introducing a new Profile Manager class [Zowe Team Config](https://medium.com/zowe/zowe-cli-getting-started-made-easy-f53d769c678e).

## Split-Up of Tasks
The task is split up in the following steps
1. Load profiles from zowe.config.json file team-config
2. Load secure profile properties from vault
3. Load profiles from zowe.config.user.json file
4. Merge global config with project config team-config
5. Save secure profile properties to vault team-config
6. Save profile properties to zowe.config.json file
7. Validate that zowe.config.json file matches schema team-config

## Tasks
### Task 1 - Load profiles from zowe.config.json file team-config
ProfileManager (PM) Class has two stages
#### Stage 1
Find the config file and load it. PM can autodiscover the file based on current working directory or it can load the file given the directory. However at all times filename must be specified before the directory.
#### Stage 2
Load the given profile. PM can load profile based on profile type and profile name. If profile type is mentioned, it looks into the defaults, which if not found, it looks serially and tries to load the
Task 1. and 2. are already complete and are fully covered by unittests.
### Task 2 - Load secure profile properties from vault
This load the secure credentials using Python package Keyring. The credentials are base64 encoded json file. The structure looks as follows :

```
{
    "$config_file_location" : {
        "profiles.$profile_name.properties.$key" : "$value"
    }
}
```
First it tries to load credentials based on config_file_location, if it fails, then it tries to load global config credentials.
### Task 3 - Load profiles from zowe.config.user.json file
Zowe User Configs are there to override the Currently Loaded Team Config.
Timeline to implement : July 11 - July 17
### Task 4 -