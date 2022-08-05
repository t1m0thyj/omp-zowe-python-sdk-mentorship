"""
Sample script to smoke test the Zowe Python SDK.

Before running, update the connection properties for your mainframe system.
To define user and password, create .env file in the same folder that defines
ZOWE_OPT_USER and ZOWE_OPT_PASSWORD for your mainframe ID.

If successful, output should look like the following:
  IEE136I LOCAL: TIME=10.47.11 DATE=2022.217  UTC: TIME=14.47.11 DATE=2022.217
 JOB09546
 INPUT
 OUTPUT
"""

import time
from decouple import config
from zowe.zos_console_for_zowe_sdk import Console
from zowe.zos_jobs_for_zowe_sdk import Jobs

# Define connection properties
profile = {
    "host": "zzow03.zowe.marist.cloud",
    "port": 10443,
    "user": config("ZOWE_OPT_USER"),
    "password": config("ZOWE_OPT_PASSWORD"),
    "rejectUnauthorized": False
}
jcl_dsname = "ZOWE.TESTS.JCL(IEFBR14T)"

# Initialize objects
my_console = Console(profile)
my_job = Jobs(profile)

# Send a console command
command_result = my_console.issue_command("D T")
print(command_result['cmd-response'])

# Submit a job on TSO
job01 = my_job.submit_from_mainframe(jcl_dsname)
print(job01['jobid'])

# Retrieve the job status
job_status = my_job.get_job_status(job01['jobname'], job01['jobid'])
print(job_status['status'])
assert job_status['status'] == "INPUT"

# Wait for job to complete
time.sleep(5)

# Retrieve the job status again
job_status = my_job.get_job_status(job01['jobname'], job01['jobid'])
print(job_status['status'])
assert job_status['status'] == "OUTPUT"
