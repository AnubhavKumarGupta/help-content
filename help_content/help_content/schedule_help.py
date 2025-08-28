# help_content/schedule_help.py

def get_schedule_content():
    """Schedule and jobs related help content - adjusted with UI references"""
    return {
        "Schedule": {
            "title": "📅 Schedule",
            "description": """
<b>Schedule Test Cases - Help Guide</b><br><br>

This page allows you to <b>create schedules</b> for running test case tasks automatically. 
You can configure platforms, test cases, execution frequency, and time zones.<br><br>

<b>Form Fields & Options:</b><br>
• <b>User ID:</b> Current logged-in user, auto-filled.<br>
• <b>Platform:</b> Platform: Choose the platform where the task will be scheduled (e.g., Airflow Local Server, Astronomer).<br>
• <b> WSL Airflow / Ubuntu Airflow / Install Airflow:</b> Provides options to install and configure Airflow environments if required. <br>
• <b>Test Case Name:</b> Dropdown list to select an existing test case for scheduling.<br>
• <b>Task Name:</b> Automatically filled based on the selected test case.<br>
• <b>Time Zone:</b> Use this button to finalize and save the schedule. <br>
• <b>Start Date / End Date:</b> Automatically filled based on the selected test case. <br>
• <b>Start Time:</b> Exact time for task execution.<br>
• <b>Frequency Options:</b><br>
&nbsp;&nbsp;• Once → Run the task only once.<br>
&nbsp;&nbsp;• Hourly → Specify the number of hours between runs.<br>
&nbsp;&nbsp;• Daily → Choose one or more days for daily execution. <br>
&nbsp;&nbsp;• Weekly → Schedule tasks to run every week.<br>
&nbsp;&nbsp;• Monthly → Configure execution on specific days of the month. <br>
&nbsp;&nbsp;• Custom → Enter a <b>Cron Expression</b> for advanced scheduling.<br>
• <b>Schedule Button:</b> Use this button to finalize and save the schedule.<br><br>

<b>Additional Notes:</b><br>
• Click on <b>Airflow Server</b> and <b>Airflow Webserver</b> to enable localhost if you are scheduling using <b>Airflow Local Server</b>.<br>
• Users can automate test execution, optimize resource usage, and ensure consistent validation cycles using schedules.<br>
• The flexibility of frequency options allows both simple and advanced scheduling needs.<br><br>

<b>Best Practices:</b><br>
• Verify timezone and frequency before saving.<br>
• Keep schedules simple and avoid overlaps.<br>
• Ensure <b>Airflow</b> is installed and properly configured before scheduling tasks.<br>
• Use <b>Cron Expressions</b> for complex, custom scheduling patterns.<br>
• Regularly review schedules in <b>Show Schedule Jobs</b>.<br><br>

<i>Proper scheduling ensures automation, timely testing, and efficient resource usage.</i>
            """
        },

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
