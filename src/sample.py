import sys
import time
from zowe.zos_console_for_zowe_sdk import Console
from zowe.zos_jobs_for_zowe_sdk import Jobs

# Connection dictionary
connection = {
    "plugin_profile": sys.argv[1]
}

# Initialize objects
my_console = Console(connection)
my_job = Jobs(connection)

# Send a console command
command_result = my_console.issue_command("D T")
print(command_result['cmd-response'])

# Submit a job on TSO
job01 = my_job.submit_from_mainframe(sys.argv[2])
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
