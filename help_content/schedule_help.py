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


# ------------------------------------          Show Scheduled Jobs          -------------------------- 

        "Show Scheduled Jobs": {
            "title": "📋 Show Scheduled Jobs",
            "description": """
<b>Show Scheduled Jobs - Help Guide</b><br><br>

This page displays all saved schedules in a <b>tabular format</b>. 
It allows you to review, edit, delete, or generate reports for scheduled jobs.<br><br>

<b>Table Columns (UI Reference):</b><br>
• <b>Select:</b> Checkbox to pick a schedule for action.<br>
• <b>User ID:</b> Creator of the schedule.<br>
• <b>Test Case:</b> Name of the scheduled test case.<br>
• <b>Schedule Name:</b> Auto-generated name of the schedule.<br>
• <b>Start Time:</b> Exact execution time.<br>
• <b>Start Date / End Date:</b> Duration of schedule validity.<br>
• <b>Frequency:</b> Once / Hourly / Daily / Weekly / Monthly / Custom.<br>
• <b>Last Run:</b> Timestamp of last execution.<br>
• <b>Status:</b> Shows execution status (Success / Failed).<br>
• <b>Platform:</b> Execution environment (Airflow Local / Astronomer).<br><br>

<b>Actions (Buttons Below):</b><br>
• <b>Edit:</b> Modify selected schedule (opens Edit window).<br>
• <b>Delete:</b> Remove a schedule permanently.<br>
• <b>Generate Report:</b> Export report for selected schedule(s).<br><br>

<b>Best Practices:</b><br>
• Always refresh the table to get latest status updates.<br>
• Use search bar for quick filtering.<br>
• Check status column to track success/failures.<br><br>

<i>This section gives you full visibility and control over your scheduled tasks.</i>
            """
        },


# ------------------------------------           Show Schedule               ---------------------------


        "Edit Schedule": {
            "title": "✏️ Edit Schedule",
            "description": """
<b>Edit Schedule - Help Guide</b><br><br>

This option allows modification of an already created schedule.<br><br>

<b>Steps:</b><br>
1. Select a schedule from the job table.<br>
2. Click <b>Edit</b> button.<br>
3. Update required fields (time, frequency, dates, platform, etc.).<br>
4. Save changes.<br><br>

<b>Notes:</b><br>
• Only valid schedules can be edited.<br>
• End Date cannot be earlier than Start Date.<br>
• Editing may overwrite previous configurations.<br>
• Updated schedules appear instantly in the job table.<br>
            """
        },


        "Delete Schedule": {
            "title": "🗑 Delete Schedule",
            "description": """
<b>Delete Schedule - Help Guide</b><br><br>

Use this option to permanently remove schedules from the system.<br><br>

<b>Steps:</b><br>
1. Select one or more schedules from the job table.<br>
2. Click <b>Delete</b> button.<br>
3. Confirm deletion in popup.<br><br>

<b>Important:</b><br>
• Deleted schedules cannot be recovered.<br>
• Ensure you export a report if data is required before deletion.<br>
            """
        },


        "Generate Report": {
            "title": "📊 Generate Report",
            "description": """
<b>Generate Report - Help Guide</b><br><br>

This feature exports detailed information of selected schedules into a report format.<br><br>

<b>Steps:</b><br>
1. Select one or more schedules from the job table.<br>
2. Click <b>Generate Report</b> button.<br>
3. System generates a report (PDF/Excel) with full details.<br><br>

<b>Report Contains:</b><br>
• User ID<br>
• Test Case Name<br>
• Schedule Name<br>
• Frequency<br>
• Start/End Dates<br>
• Last Run<br>
• Status<br>
• Platform<br><br>

<b>Use Cases:</b><br>
• Audit of scheduled jobs.<br>
• Sharing execution details with team.<br>
• Record keeping for compliance.<br><br>

<i>Reports provide a structured view of scheduling history for analysis and documentation.</i>
            """
        }
    }
