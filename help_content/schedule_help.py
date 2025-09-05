# help_content/schedule_help.py

def get_schedule_content():
    """Schedule and jobs related help content - adjusted with UI references"""
    return {

# -----------------------------------------      Schedule     -----------------------------------        

"Schedule": {
            "title": "Schedule",
            "description": """
<b>Schedule a Test Case – Help Guide</b><br><br>

<b>Overview</b><br><br>
The Schedule feature allows you to automate test case executions on either your local Airflow server or on Astronomer. 
This enables flexible, repeatable, and timed data validation, analysis, and reporting - supporting complex validation 
workflows, monitoring, and automated alerting.<br><br>

<b>Platforms Supported</b>
<ul>
  <li><b>Airflow Local Server:</b> Run and schedule tests directly using an Airflow instance that runs on your own machine (WSL/Ubuntu).</li>
  <li><b>Astronomer:</b> Schedule test cases on a managed Astronomer (cloud-native Airflow) platform.</li>
</ul>
Select your desired platform from the Platform dropdown menu at the top of the Schedule page.<br><br>

<b>Pre-requisites</b>
<ul>
  <li><b>For Airflow Local Server:</b>
    <ul>
      <li>Ubuntu WSL and Airflow must be installed on your system.</li>
      <li>If not installed, simply click the buttons provided in the UI (WSL Install, Install Ubuntu, Airflow Install)  and follow steps - they automate the setup for you. </li>
      <li>You only need to install these components once per machine.</li>
    </ul>
  </li>

  <li><b>For Astronomer:</b>
    <ul>
      <li>First click the Astro Install button from the UI - this ensures Astro CLI is installed in your system (you only need to install this component once per machine).</li>
      <li>Simply click the Astro Setup button before scheduling - this ensures necessary back-end setup for Astronomer integration.</li>
    </ul>
  </li>
</ul>

<br>

<b>Step-by-Step Guide</b>
<ol>
  <li><b>Select Platform:</b>
    <ul>
      <li>Use the Platform dropdown to choose Airflow Local Server or Astronomer.</li>
      <li>The form will adjust based on your selected platform.</li>
    </ul>
  </li>
  <li><b>Complete Platform Setup (if needed):</b>
    <ul>
      <li><b>For Airflow Local Server:</b> Ensure WSL, Ubuntu, and Airflow are all installed using the setup buttons.</li>
      <li><b>For Astronomer:</b> Ensure Astro CLI is installed using the setup button and then click Astro Setup for one-time environment configuration. </li>
    </ul>
  </li>
  <li><b>Select Test Case:</b>
    <ul>
      <li>In Test Case Name, start typing the name or use the search bar to find the test case you want to schedule.</li>
      <li><i>Note: You must create the test case in advance (see the separate "Create Test Case" help guide).</i></li>
    </ul>
  </li>
  <li><b>Fill Scheduling Details:</b>
    <ul>
      <li><b>Task Name:</b> (Optional) Enter a recognizable name for your scheduled task.</li>
      <li><b>Timezones:</b> Select or start typing your timezone. The dropdown supports search for convenience.</li>
      <li><b>Timezones:</b> Select or start typing your timezone. The dropdown supports search for convenience.</li>
      <li> <b>Frequency of Scheduling:</b>
      <ul> 
        <li> Once (default) - runs just one time </li>
        <li> Hourly, Daily, Weekly, Monthly – regular intervals </li>
        <li> Custom – set your own frequency rules</li>
      </ul>
      <li><b>Start Time:</b> Set the exact time when the test should begin on the chosen days.</li>
    </ul>
  </li>
  <li><b>Schedule the Test Case:</b>
    <ul>
      <li>Click the <b>SCHEDULE</b> button.</li>
      <li><b>For Airflow Local Server:</b>
        <ul>
          <li> After your first test case scheduling in a session (or after login), two additional buttons will appear: <b>Airflow Server</b> and <b>Airflow Webserver</b>.</li>
          <li> Click both buttons, one after the other. This action starts the Airflow server and brings up the webserver UI. </li>
          <li> This step is only needed the first time you schedule after starting or logging into the application. On subsequent schedules (in the same session), simply click <b>SCHEDULE</b>. </li>
          <li> <i>Note: If you log out and back in, you must repeat this two-button process at the start of each new session.</i> </li>
        </ul>
      </li>
      <li><b>For Astronomer:</b>
        <ul>
          <li>Setup is one-time: after clicking Astro Setup once (if needed), proceed to SCHEDULE as above.</li>
        </ul>
      </li>
    </ul>
  </li>
</ol>

<br>
<br>

<b>Summary of Process (Airflow Local Server)</b>
<ul>
  <li>Select or install WSL, Ubuntu, and Airflow (use buttons if not installed)..</li>
  <li>Search and select the test case.</li>
  <li>Set timezone, scheduling frequency, start/end dates, start time.</li>
  <li>Click <b>SCHEDULE</b>.</li>
  <li>(First test case of the session) Click <b>Airflow Server → Airflow Webserver</b>. </li>
  <li>For all subsequent test case schedules in the same session, just click <b>SCHEDULE</b>. </li>
</ul>

<br>

<b>Summary of Process (Astronomer)</b>
<ul>
  <li>Select or Install Astro (use button if not installed).</li>
  <li>Click <b>Astro Setup</b> (one-time each session, as prompted).</li>
  <li>Search/select the test case, set schedule details, and click <b>SCHEDULE</b>.</li>
</ul>

<br>

<b>Best Practices</b>
<ul>
  <li>Always ensure system time and selected timezone match your scheduling intentions.</li>
  <li>Only schedule as frequently as operationally necessary to avoid resource conflicts.</li>
  <li>Use descriptive task names for easy job identification and audit.</li>
  <li>Double-check test case selection to avoid running the wrong test scenario.</li>
</ul>

<br>

<b>Troubleshooting</b>
<ul>
  <li>If scheduling fails, ensure all required installations are complete and running.</li>
  <li><b>Airflow Server</b> and <b>Airflow Webserver</b> buttons may need to be clicked again if the application has been restarted or after logout/login.</li>
  <li>For Astronomer, confirm Astro Setup is complete before first scheduling action.</li>
</ul>

<i>Using the Schedule feature, you can automate and orchestrate your data validation workflows across platforms-ensuring consistent, policy-driven execution and peace of mind.</i>
"""
        },


# --------------------------------------       Show Schedule        -------------------------- 
   
"Show Scheduled Jobs": {
            "title": "Show Scheduled Jobs",
            "description": """
<b>Show Schedule Jobs – Help Guide</b><br><br>

<b>Overview</b><br><br>
The Show Schedule Jobs page provides a comprehensive view and control of all scheduled test case jobs in INFOFISCUS 
Data Validation Tool. Users can review, search, edit, delete, or re-generate test executions quickly and efficiently.<br><br>

<b>Key Functionalities</b>
<ol>
  <li><b>Edit Scheduled Job</b>
    <br>
    <b>Purpose:</b>
        <p> Edit allows users to reschedule an already existing job—updating its timing, frequency, or timezone without recreating it from scratch.</p>
    <b>How to Use: </b>
    <ul>
      <li>Select the desired scheduled job from the table by clicking its row (radio button).</li>
      <li>Click <b>Edit</b> (blue button).</li>
      <li>You'll navigate to the scheduling form</b>.</li>
      <li>Change the Timezone, Start Date, End Date, Frequency (Once, Hourly, Daily, Weekly, Monthly, Custom), and Start Time as needed. </li>
      <li> Click <b>Schedule</b> to save and re-schedule the test case.</li>
    </ul>
    <i> <b>Tips:</b> Rescheduling is ideal for routine test validations that need an updated execution window. Use this to shift tests to a new window (e.g., after a business hour change or to avoid overlaps). </i>
  </li>
  <br>

  <li><b>Delete Scheduled Job</b>
  <br>
     <b>Purpose:</b>
        <p>Removes old, unwanted, or no-longer-needed scheduled test cases. Keeps the UI organized and prevents accidental execution.</p>
    <b>How to Use: </b>
    <ul>
      <li>Select the test case job you wish to remove by radio button.</li>
      <li>Click the <b>Delete</b> (red button).</li>
      <li>Confirm deletion if prompted.</li>
    </ul>
    <i> <b>Use Cases:</b> Optimize by removing clutter and test jobs that are obsolete or redundant.</i>
  </li>
  <br>
  <li><b>Generate Test Case Output</b>
      <br>
    <b>Purpose:</b>
        <p> Instantly regenerates the result file for a previously scheduled test case job, without rerunning or re-scheduling the whole process.</p>
    <b>How to Use: </b>
    <ul>
      <li>Select the scheduled job of interest.</li>
      <li>Click the <b>Generate</b> (green button).</li>
      <li>The system will prompt you to choose a save path and will export the results (typically as an Excel file).</li>
    </ul>
    <i> <b>Tips:</b> Leverage this for audit, historical analysis, or if the previous file was misplaced. </i>
  </li>
</ol>

<br>

<b>Additional Features</b>
<ul>
  <li><b>Search Bar:</b> Instantly search by User, Test Case, Schedule Name, or any other column to quickly locate any scheduled job—especially helpful in large environments.</li>
  <li><b>User Dropdown:</b> Admins can filter scheduled jobs by user, making management in multi-user environments faster.</li>
  <li><b>Refresh:</b> Keeps your job list up to date with latest changes.</li>
</ul>

<br>

<b>Visual Workflow Diagram</b><br>
<img src="flowcharts/show_schedule_jobs1.png" alt="Show Scheduled Jobs Diagram" style="max-width: 500px; max-height: 300px; width: 100%; height: auto;"><br><br>

<b>Best Practices</b>
<ul>
  <li><b>Housekeeping:</b> Regularly delete unwanted or expired scheduled jobs—keeps the environment fast, secure, and clutter-free.</li>
  <li><b>Quick Edits:</b> Use Edit instead of deleting/recreating jobs when only times/frequencies change.</li>
  <li><b>Audit Ready:</b> Use Generate to quickly export or re-create historical results for compliance or review.</li>
  <li><b>Search Proactively:</b> Use the search bar to filter and act on jobs rapidly, especially in busy environments.</li>
</ul>
"""
        }
    }
