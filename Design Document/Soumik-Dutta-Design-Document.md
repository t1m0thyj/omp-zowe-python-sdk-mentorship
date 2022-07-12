# Team Config Support in Zowe Python SDK

## Motivation
Last version of Python SDK used to use different YAML files for different profile configuration. However the Nodejs SDK has moved on to JSON configs ([Zowe Team Config](https://medium.com/zowe/zowe-cli-getting-started-made-easy-f53d769c678e)) containing different profiles in one single file. There is also the concept of global and user configs for use for teams with multiple members and multiple roles. Hence to support such configs in Zowe Python SDK, we are introducing a new Profile Manager class.

## Split-Up of Tasks
The task is split up in the following steps
1. Load profiles from zowe.config.json file team-config
2. Load secure profile properties from vault
3. Write a new Session class
4. Load profiles from zowe.config.user.json file
5. Merge global config with project config team-config
6. Save secure profile properties to vault team-config

### Stretch Goals
- Save profile properties to zowe.config.json file
- Validate that zowe.config.json file matches schema team-config

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

``` json
{
    "$config_file_location" : {
        "profiles.$profile_name.properties.$key" : "$value",
    },
}
```
First it tries to load credentials based on config_file_location, if it fails, then it tries to load global config credentials.

### Task 3 - Session Class
Write a new Session Manager class that will receive profile properties from PM and create different session types:
- Basic: Username and Password
- Token: TokenType and TokenValue

Timeline to implement: July 11 - July 17
### Task 4 - Load profiles from zowe.config.user.json file
Zowe User Configs are there to override the Currently Loaded Team Config. The path of the file will be loaded in the same way as the Zowe Team Config.

Timeline to implement: July 22 - July 28
### Task 5 - Merge global config with project config
There can be two types of configs:
- Project Config - Specific to a particular project
- Global Config - Can be used to load defaults for any project

In addition to these, "User Configs" can be used to override the values of the given config. For example Project "User" Config will override Project Config and Global "User" Config will override Global Config.

Profile Manager should be able to load Project Configs, and for values that could not be found, Global Config will provide the defaults. Again the values of either of the configs should be overridable by the values in the User Configs.

#### Scenarios
##### Scenario 1 ("User Config overriding defaults"):
1. Project user config: "my_zosmf" profile defines `"host": "example1.com"`
2.  Project config: "my_zosmf" profile defines `"host": "example2.com", "port": 1443`

OR

3. Global user config: "my_zosmf" profile defines `"host": "example1.com"`
4. Global config: "my_zosmf" profile defines `"host": "example2.com", "port": 1443`

should be loaded as:

`"host": "example1.com", "port": 1443`

##### Scenario 2 (Profiles with same name do not provide defaults):
2. Project config: "my_zosmf" profile defines `"host": "example1.com"`
4. Global config: "my_zosmf" profile defines `"host": "example2.com", "port": 1443`

should be loaded as:

`"host": "example1.com"`

##### Scenario 3 (Exception to 2, base profile can provide defaults)
3. Project config: "my_zosmf" profile of type zosmf defines `"host": "example1.com"`
4. Global config: "my_base" profile of type base defines `"host": "example2.com", "port": 1443`

should be loaded as:

`"host": "example1.com", "port": 1443`

Timeline to implement: July 29 - August 5
### Task 6 - Save secure profile properties to vault
Using keyring.set_password() we can update the secure profile properties. `ProfileManager.update_secure_props(profile_name="", properties: dict = {})` will update/add new properties to the secure credentials.

Timeline to implement: August 6 - August 12
### Stretch Goals
#### Save profile properties to zowe.config.json file
Using jsonc.dump(JSONCDict, file) we can add profile. We will add a new function `ProfileManager.add_profile(name="", type="")` and then using setters add properties. Also we will be using setters to add the secure properties and due to the work done on task 5, we will be able to save the secure values to keyring. Finally `ProfileManager.save_profile()` will output the file. Also `ProfileManager.remove_profile()` will remove a named profile and its secure properties on keyring.

#### Validate that zowe.config.json file matches schema
I plan to implement validation using jsonschema as well as a custom function to implement custom rules and emit warnings.

Timeline to implement: August 13 - August 25

## Approach strategy
Write actual code, then add custom Exceptions for unexpected issues. Then finally write unittests.