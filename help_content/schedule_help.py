# help_content/schedule_help.py

def get_schedule_content():
    """Schedule and jobs related help content - adjusted with UI references"""
    return {

# -----------------------------------------      Schedule     -----------------------------------        

"Schedule": {
    "title": "📅 Schedule",
    "description": """
<b>Schedule a Test Case – Help Guide</b><br><br>

<b>Overview</b><br>
The Schedule feature allows you to automate test case executions on either your local Airflow server or on Astronomer. 
This enables flexible, repeatable, and timed data validation, analysis, and reporting - supporting complex validation workflows, monitoring, and automated alerting.<br><br>

<b>Platforms Supported</b><br>
• <b>Airflow Local Server:</b> Run and schedule tests directly using an Airflow instance that runs on your own machine (WSL/Ubuntu).<br>
• <b>Astronomer:</b> Schedule test cases on a managed Astronomer (cloud-native Airflow) platform.<br>
Select your desired platform from the Platform dropdown menu at the top of the Schedule page.<br><br>

<b>Pre-requisites</b><br>
• <b>For Airflow Local Server:</b><br>
&nbsp;&nbsp; • Ubuntu WSL and Airflow must be installed on your system.<br>
&nbsp;&nbsp; • If not installed, simply click the buttons provided in the UI (WSL Install, Install Ubuntu, Airflow Install) and follow prompts - they automate the setup for you.<br>
&nbsp;&nbsp; • You only need to install these components once per machine.<br><br>
• <b>For Astronomer:</b><br>
&nbsp;&nbsp; • Simply click the Astro Setup button before scheduling - this ensures necessary back-end setup for Astronomer integration.<br><br>

<b>Step-by-Step Guide</b><br>
1. <b>Select Platform:</b><br>
&nbsp;&nbsp; • Use the Platform dropdown to choose Airflow Local Server or Astronomer.<br>
&nbsp;&nbsp; • The form will adjust based on your selected platform.<br><br>

2. <b>Complete Platform Setup (if needed):</b><br>
&nbsp;&nbsp; • <b>For Airflow Local Server:</b> Ensure WSL, Ubuntu, and Airflow are all installed using the setup buttons.<br>
&nbsp;&nbsp; • <b>For Astronomer:</b> Click Astro Setup for one-time environment configuration.<br><br>

3. <b>Select Test Case:</b><br>
&nbsp;&nbsp; • In Test Case Name, start typing the name or use the search bar to find the test case you want to schedule.<br>
&nbsp;&nbsp; • <i>Note: You must create the test case in advance (see the separate “Create Test Case” help guide).</i><br><br>

4. <b>Fill Scheduling Details:</b><br>
&nbsp;&nbsp; • <b>Task Name:</b> (Optional) Enter a recognizable name for your scheduled task.<br>
&nbsp;&nbsp; • <b>Timezones:</b> Select or start typing your timezone. The dropdown supports search for convenience.<br>
&nbsp;&nbsp; • <b>Start Date & End Date:</b> Set the period during which you want the test case to run.<br>
&nbsp;&nbsp; • <b>Frequency of Scheduling:</b><br>
&nbsp;&nbsp;&nbsp;&nbsp;• Once (default) • runs just one time<br>
&nbsp;&nbsp;&nbsp;&nbsp;• Hourly, Daily, Weekly, Monthly – regular intervals<br>
&nbsp;&nbsp;&nbsp;&nbsp;• Custom – set your own frequency rules<br>
&nbsp;&nbsp; • <b>Start Time:</b> Set the exact time when the test should begin on the chosen days.<br><br>

5. <b>Schedule the Test Case:</b><br>
&nbsp;&nbsp; • Click the <b>SCHEDULE</b> button to queue the job.<br><br>
&nbsp;&nbsp;• <b>For Airflow Local Server only:</b><br>
&nbsp;&nbsp;&nbsp;&nbsp;• After your first test case scheduling in a session (or after login), two additional buttons will appear: <b>Airflow Server</b> and <b>Airflow Webserver</b>.<br>
&nbsp;&nbsp;&nbsp;&nbsp;• Click both buttons, one after the other. This action starts the Airflow server and brings up the webserver UI.<br>
&nbsp;&nbsp;&nbsp;&nbsp;• This step is only needed the first time you schedule after starting or logging into the application. On subsequent schedules (in the same session), simply click <b>SCHEDULE</b>.<br>
&nbsp;&nbsp;&nbsp;&nbsp;• <i>Note: If you log out and back in, you must repeat this two-button process at the start of each new session.</i><br><br>
&nbsp;&nbsp;– <b>For Astronomer:</b><br>
&nbsp;&nbsp;&nbsp;&nbsp;• Setup is one-time: after clicking Astro Setup once (if needed), proceed to SCHEDULE as above.<br><br>

<b>Summary of Process (Airflow Local Server)</b><br>
• Select or install WSL, Ubuntu, and Airflow (use buttons if not installed).<br>
• Search and select the test case.<br>
• Set timezone, scheduling frequency, start/end dates, start time.<br>
• Click <b>SCHEDULE</b>.<br>
• (First test case of the session) Click <b>Airflow Server → Airflow Webserver</b>.<br>
• For all subsequent test case schedules in the same session, just click <b>SCHEDULE</b>.<br><br>

<b>Summary of Process (Astronomer)</b><br>
• Click <b>Astro Setup</b> (one-time each session, as prompted).<br>
• Search/select the test case, set schedule details, and click <b>SCHEDULE</b>.<br><br>

<b>Best Practices</b><br>
• Always ensure system time and selected timezone match your scheduling intentions.<br>
• Only schedule as frequently as operationally necessary to avoid resource conflicts.<br>
• Use descriptive task names for easy job identification and audit.<br>
• Double-check test case selection to avoid running the wrong test scenario.<br><br>

<b>Troubleshooting</b><br>
• If scheduling fails, ensure all required installations are complete and running.<br>
• <b>Airflow Server</b> and <b>Airflow Webserver</b> buttons may need to be clicked again if the application has been restarted or after logout/login.<br>
• For Astronomer, confirm Astro Setup is complete before first scheduling action.<br><br>

<i>Using the Schedule feature, you can automate and orchestrate your data validation workflows across platforms-ensuring consistent, policy-driven execution and peace of mind.</i>
"""
},


# ------------------------------------          Show Schedule        -------------------------- 

"Show Scheduled Jobs": {
    "title": "📋 Show Scheduled Jobs",
    "description": """
<b>Show Schedule Jobs – Help Guide</b><br><br>

<b>Overview:</b><br>
The Show Schedule Jobs page provides a comprehensive view and control of all scheduled test case jobs in INFOFISCUS Data Validation Tool. Users can review, search, edit, delete, or re-generate test executions quickly and efficiently.<br><br>

<b>Key Functionalities:</b><br>

1. <b>Edit Scheduled Job</b><br>
<b>Purpose:</b> Edit allows users to reschedule an already existing job—updating its timing, frequency, or timezone without recreating it from scratch.<br>
<b>How to Use:</b> Select the desired scheduled job from the table by clicking its row (radio button). Click <b>Edit</b> (blue button). Navigate to the scheduling form. Change Timezone, Start Date, End Date, Frequency (Once, Hourly, Daily, Weekly, Monthly, Custom), and Start Time as needed. Click <b>Schedule</b> to save and re-schedule the test case.<br>
<b>Tips:</b> Rescheduling is ideal for routine test validations or to shift tests to a new window (e.g., after business hour changes).<br><br>

2. <b>Delete Scheduled Job</b><br>
<b>Purpose:</b> Removes old, unwanted, or no-longer-needed scheduled test cases. Keeps the UI organized and prevents accidental execution.<br>
<b>How to Use:</b> Select the test case job by radio button. Click <b>Delete</b> (red button). Confirm deletion if prompted.<br>
<b>Use Case:</b> Optimize by removing clutter and obsolete test jobs.<br><br>

3. <b>Generate Test Case Output</b><br>
<b>Purpose:</b> Instantly regenerates the result file for a previously scheduled test case job, without rerunning or re-scheduling the whole process.<br>
<b>How to Use:</b> Select the scheduled job of interest. Click <b>Generate</b> (green button). Choose a save path; results are exported (typically as Excel).<br>
<b>Tips:</b> Use for audit, historical analysis, or if the previous file was misplaced.<br><br>

<b>Additional Features:</b><br>
• <b>Search Bar:</b> Quickly locate scheduled jobs by User, Test Case, Schedule Name, or other columns.<br>
• <b>User Dropdown:</b> Filter scheduled jobs by user for multi-user management.<br>
• <b>Refresh:</b> Keep the job list up to date with latest changes.<br><br>

<b>Typical Workflow – Flowchart:</b><br>
<pre>
+-----------------------------+
| Show Schedule Jobs          |
+-----------------------------+
          |
+---------+---------+---------+
|         |         |         |
[Edit]   [Delete]  [Generate]
|         |         |
Select Job Select Job Select Job
|         |         |
Edit timing Confirm  Generate/export
and schedule delete job Excel results file
|         |         |
SCHEDULE done  UI cleans up Save Excel
</pre><br>

Or in "steps arrows" visual form:<br>
<pre>
[Select Test Case]
|
+---------+---------+---------+
|         |         |         |
Edit     Delete    Generate   Search/Filter
|         |         | 
Edit form Remove    Download   Find job fast
|         |
Reschedule Clean   Excel file
</pre><br>

<b>Best Practices:</b><br>
• <b>Housekeeping:</b> Regularly delete unwanted or expired scheduled jobs to keep the environment fast, secure, and clutter-free.<br>
• <b>Quick Edits:</b> Use Edit instead of deleting/recreating jobs when only times/frequencies change.<br>
• <b>Audit Ready:</b> Use Generate to export or re-create historical results for compliance or review.<br>
• <b>Search Proactively:</b> Use the search bar to filter and act on jobs rapidly, especially in busy environments.
"""
}
    
    
    
    }