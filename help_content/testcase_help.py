# help_content/testcase_help.py

def get_testcase_content():
    """Test case related help content - focused only on test case operations"""
    return {

# --------------------------------         Create Test Cases          ---------------------------

"Create Test Case": {
    "title": "Create Test Case",
    "description": """
<b>Create Test Case – Help Guide</b><br><br>

This feature allows you to configure, map, and prepare <b>data validation scenarios</b> (test cases) comparing source and target tables/columns across your connected databases.<br>
Follow the steps below to ensure correct, repeatable, and robust test cases.<br><br>

<b>Steps</b>
<ol>
  <li><b>Test Case Setup</b>
  <br>
    <table style="width:100%; border-collapse: collapse; margin-bottom: 14px; border:1px solid #334155;">
      <tr style="background:#1e293b; color:#38bdf8; text-align:left;">
        <th style="padding:8px; border:1px solid #334155;">Action</th>
        <th style="padding:8px; border:1px solid #334155;">Details</th>
      </tr>
      <tr><td style="padding:6px; border:1px solid #334155;">Access Create Test Case Panel</td><td style="padding:6px; border:1px solid #334155;">From the left menu, click <b>Create Test Case</b>.</td></tr>
      <tr><td style="padding:6px; border:1px solid #334155;">Enter Test Case Name</td><td style="padding:6px; border:1px solid #334155;">Input a unique name.<br><b>Best Practice:</b> Use underscores (e.g., Customer_Validation_2025). Spaces may cause failures.</td></tr>
      <tr><td style="padding:6px; border:1px solid #334155;">Select Source Connection</td><td style="padding:6px; border:1px solid #334155;">Choose the source DB connection (Databricks, Snowflake, etc.) from the dropdown.</td></tr>
      <tr><td style="padding:6px; border:1px solid #334155;">Fetch Source Tables</td><td style="padding:6px; border:1px solid #334155;">Click <b>Fetch Source Table</b>. Select the table(s) to validate.</td></tr>
      <tr><td style="padding:6px; border:1px solid #334155;">Choose Validation Type</td><td style="padding:6px; border:1px solid #334155;">Select Row Count, Column Data, Schema Validation, etc.</td></tr>
      <tr><td style="padding:6px; border:1px solid #334155;">Proceed</td><td style="padding:6px; border:1px solid #334155;">Click <b>Next</b> to go to table mapping.</td></tr>
    </table>
  </li>

  <li><b>Target Table Selection and Mapping</b>
  <br>
    <table style="width:100%; border-collapse: collapse; margin-bottom: 14px; border:1px solid #334155;">
      <tr style="background:#1e293b; color:#38bdf8; text-align:left;">
        <th style="padding:8px; border:1px solid #334155;">Action</th>
        <th style="padding:8px; border:1px solid #334155;">Details</th>
      </tr>
      <tr><td style="padding:6px; border:1px solid #334155;">Select Target Connection</td><td style="padding:6px; border:1px solid #334155;">Pick the target DB connection from dropdown.</td></tr>
      <tr><td style="padding:6px; border:1px solid #334155;">Fetch Target Tables</td><td style="padding:6px; border:1px solid #334155;">Click <b>Fetch Target Table</b> to view available tables.</td></tr>
      <tr><td style="padding:6px; border:1px solid #334155;">Map Tables</td><td style="padding:6px; border:1px solid #334155;">• Auto-mapping suggested; if not, drag & drop manually.<br>• Mapped tables appear under <b>Mapped Tables</b>.</td></tr>
      <tr><td style="padding:6px; border:1px solid #334155;">Unmap Function</td><td style="padding:6px; border:1px solid #334155;">• Click <b>Unmap</b> to remove mapping (if required).<br>• Click <b>Next</b> for column mapping.</td></tr>
    </table>
  </li>

  <li><b>Column Mapping and Filtering</b>
  <br>
    <table style="width:100%; border-collapse: collapse; margin-bottom: 14px; border:1px solid #334155;">
      <tr style="background:#1e293b; color:#38bdf8; text-align:left;">
        <th style="padding:8px; border:1px solid #334155;">Action</th>
        <th style="padding:8px; border:1px solid #334155;">Details</th>
      </tr>
      <tr><td style="padding:6px; border:1px solid #334155;">Review Columns</td><td style="padding:6px; border:1px solid #334155;">• Source & Target columns shown side-by-side.<br>• Auto-mapped if names match.</td></tr>
      <tr><td style="padding:6px; border:1px solid #334155;">Set Primary Key</td><td style="padding:6px; border:1px solid #334155;">• Required for Column Data Validation.<br>• Auto-selected if present; else select manually.</td></tr>
      <tr><td style="padding:6px; border:1px solid #334155;">Apply Filters</td><td style="padding:6px; border:1px solid #334155;">• Add filter conditions (column, operator, value).<br>• Supports multiple filters.</td></tr>
      <tr><td style="padding:6px; border:1px solid #334155;">Save Mapping</td><td style="padding:6px; border:1px solid #334155;">Click <b>Save</b> to save mappings.</td></tr>
      <tr><td style="padding:6px; border:1px solid #334155;">Execute</td><td style="padding:6px; border:1px solid #334155;">• Click <b>Execute</b> to run test case.<br>• Choose location to save Excel result file.</td></tr>
    </table>
  </li>
</ol>

<br>

<b>Tips & Notes</b>
<ul>
  <li>Use underscores in test case names.</li>
  <li>Primary Key is mandatory for Column Data Validation.</li>
  <li>Drag & drop for manual mappings.</li>
  <li>Filters support flexible conditions.</li>
  <li>Results exported as Excel.</li>
  <li>Use <b>Previous</b> to revise selections.</li>
</ul>

<br>

<b>Workflow Diagram</b><br>
<img src="flowcharts/create_test_case1.png" alt="Create Test Case Diagram" style="max-width: 400px; max-height: 100px; width: 100%; height: auto;"><br><br>

<i>Following this guide ensures your test cases are created accurately, mapped correctly, and ready for automated/manual execution in InfoFiscus Data Validation Tool.</i>
"""
}

,

# --------------------------------          Show test cases           ---------------------------

"Show Test Case": {
    "title": "Show Test Case",
    "description": """
<b>Show Test Case – Help Guide</b><br><br>

<b>Overview</b><br>
The Show Test Case feature is your command center for test case lifecycle management. Here you can review, update (Edit), or remove (Delete) existing test cases, ensuring your validation suite stays organized, accurate, and agile as your data and business rules evolve.<br><br>

<b>Main Functionalities</b>
<ol>
  <li><b>Edit Test Case</b>
    <ul>
      <li>It modify any previously created test case to adapt to changing requirements, data sources, or validation logic without starting from scratch.</li>
      <li>When to Use:
        <ul>
          <li>Business requirements change</li>
          <li>New columns/tables need validation</li>
          <li>Validation type needs to be updated</li>
          <li>Table or column mappings need adjustment</li>
          <li>To add/remove filters, or reset the primary key for column validation</li>
        </ul>
      </li>
    </ul>
  </li>

  <li><b>Delete Test Case</b>
    <ul>
      <li>Permanently remove obsolete, irrelevant, or duplicate test cases to keep your UI clean and ensure only relevant jobs are retained.</li>
    </ul>
  </li>
</ol>

<br>

<b>How to Use – Step-by-Step Workflow</b>
<ol>
  <li><b>Finding and Selecting a Test Case</b>
    <ul>
      <li><b>Search:</b> Use the search bar to find test cases by name, connection, or partial keyword. This is especially helpful in large environments.</li>
      <li><b>Select:</b> Choose the desired test case by clicking the corresponding row/radio button in the list.</li>
    </ul>
  </li>

  <li><b>Edit Workflow</b>
    <ul>
      <li><b>Click Edit:</b> After selecting a test case, click the Edit button.</li>
      <li>This opens the editing interface (similar to <b>Create Test Case</b> wizard).</li>
      <li><b>Adjust Configuration:</b>
        <ul>
          <li>Change validation type (Schema, Row Count, Column Data, or combinations).</li>
          <li>Select/deselect tables as required.</li>
        </ul>
      </li>
      <li><b>Table Mapping:</b> Click <b>Table Mapping</b> to map or unmap source/target tables (drag-and-drop or auto-mapping).</li>
      <li><b>Column Mapping:</b> Click <b>Column Mapping</b> to pair columns, update primary keys (mandatory for column data validation), and define filters.</li>
      <li><b>Save & Execute:</b> Save to update the test case. Optionally, execute immediately to validate with new settings and download results.</li>
      <li><i>Note:</i> Only validation, logic, and mappings can be edited—test case name and source connection usually stay fixed.</li>
    </ul>
  </li>

  <li><b>Delete Workflow</b>
    <ul>
      <li><b>Select & Delete:</b> Choose an unwanted test case and click Delete.</li>
      <li><b>Confirm:</b> Approve the prompt to remove it permanently.</li>
      <li>The test case is removed from the list, keeping your UI clean.</li>
    </ul>
  </li>
</ol>

<br>

<b>Visual Workflow Diagram</b><br>
<img src="flowcharts/show_test_case1.png" alt="Show Test Case Diagram" style="max-width: 400px; max-height: 100px; width: 100%; height: auto;"><br><br>

<b>Feature Comparison Table</b><br>
<table style="width:100%; border-collapse: collapse; margin-top:10px;">
<tr style="background-color:#1e293b; color:#38bdf8; text-align:left;">
  <th style="padding:6px; border:1px solid #334155;">Function</th>
  <th style="padding:6px; border:1px solid #334155;">Purpose</th>
  <th style="padding:6px; border:1px solid #334155;">Main Actions</th>
  <th style="padding:6px; border:1px solid #334155;">When to Use</th>
</tr>
<tr>
  <td style="padding:6px; border:1px solid #334155;"><b>Edit</b></td>
  <td style="padding:6px; border:1px solid #334155;">Update an existing test case</td>
  <td style="padding:6px; border:1px solid #334155;">Modify validation, mapping, logic</td>
  <td style="padding:6px; border:1px solid #334155;">When requirements/data change or optimization is needed</td>
</tr>
<tr>
  <td style="padding:6px; border:1px solid #334155;"><b>Delete</b></td>
  <td style="padding:6px; border:1px solid #334155;">Remove test case</td>
  <td style="padding:6px; border:1px solid #334155;">Select & confirm deletion</td>
  <td style="padding:6px; border:1px solid #334155;">When test case is obsolete, duplicated, or no longer needed</td>
</tr>
</table><br><br>

<b>Best Practices & Tips</b>
<ul>
  <li>Edit instead of recreate when possible—this preserves links, history, and supporting data.</li>
  <li>Always review mappings and primary key selections after schema or column changes.</li>
  <li>Use search to quickly locate and act on test cases.</li>
  <li>Delete test cases regularly to avoid clutter.</li>
  <li>After deleting, check for downstream dependencies that may rely on the removed test case.</li>
  <li>All validations, mapping requirements, and filter logic from <b>Create Test Case</b> guidance still apply.</li>
</ul>


<br>

<i>For detailed help on column mapping, validation requirements, and filters, see the “Create Test Case – Help Guide”.</i>
"""
}
,

# --------------------------------          Show Test Result           ---------------------------

"Show Test Results": {
    "title": "Show Test Results",
    "description": """
<b>Show Test Results – Help Guide</b><br><br>

<b>Overview</b><br>
The Show Test Results section is your dashboard for reviewing all completed test case executions. It provides detailed insights into tests that succeeded or failed, enabling you to understand the health of your data pipelines and validation efforts.<br><br>

<b>Key Features and Usage</b>
<ul>
  <li><b>View All Results:</b> Lists all test runs created by the current user, showing status (pass/fail), execution time, associated test case, and summary info.</li>
  <li><b>Status Indicators:</b> Quickly identify failures or successes to prioritize troubleshooting.</li>
  <li><b>Regenerate Reports:</b> Select prior test executions and regenerate Excel reports without re-running tests—useful for sharing or archiving.</li>
  <li><b>Search and Filter:</b> Use the search bar and filters to find specific executions by name, date, or status.</li>
</ul>

<br>

<b>Typical Workflow</b>
<ol>
  <li>Navigate to <b>Show Test Results</b> from the main menu.</li>
  <li>Browse or search for the relevant test executions.</li>
  <li>Review status and execution metadata.</li>
  <li>Select one or more results to regenerate reports.</li>
  <li>Click <b>Regenerate</b> to export Excel files for auditing or sharing.</li>
</ol>

<br>

<b>Benefits</b>
<ul>
  <li>Centralized access to all validation results.</li>
  <li>Simplifies compliance with easy report re-generation.</li>
  <li>Saves time by avoiding re-execution for report generation.</li>
  <li>Focuses attention on failing tests for faster resolution.</li>
</ul>

<br>

<b>Best Practices</b>
<ul>
  <li>Regularly review results post-execution to catch issues early.</li>
  <li>Use search and filters to efficiently manage large volumes.</li>
  <li>Maintain consistent, descriptive test case naming for ease of use.</li>
  <li>Regenerate reports as needed for stakeholders or compliance.</li>
</ul>

<br>

<b>Visual Workflow Diagram</b><br>
<img src="flowcharts/show_test_result1.png" alt="Show Test Results Diagram" style="max-width: 400px; max-height: 300px; width: 100%; height: auto;"><br><br>

<b>Task Summary Table</b><br>
<table style="width:100%; border-collapse: collapse; margin-top:10px;">
<tr style="background-color:#1e293b; color:#38bdf8; text-align:left;">
  <th style="padding:6px; border:1px solid #334155;">Step</th>
  <th style="padding:6px; border:1px solid #334155;">Description</th>
  <th style="padding:6px; border:1px solid #334155;">User Action</th>
</tr>
<tr>
  <td style="padding:6px; border:1px solid #334155;">Open Results</td>
  <td style="padding:6px; border:1px solid #334155;">Access Show Test Results page</td>
  <td style="padding:6px; border:1px solid #334155;">Navigate via main menu</td>
</tr>
<tr>
  <td style="padding:6px; border:1px solid #334155;">Search / Filter</td>
  <td style="padding:6px; border:1px solid #334155;">Narrow down results by criteria</td>
  <td style="padding:6px; border:1px solid #334155;">Use search bar and filters</td>
</tr>
<tr>
  <td style="padding:6px; border:1px solid #334155;">Select Test Run</td>
  <td style="padding:6px; border:1px solid #334155;">Highlight one or multiple test executions</td>
  <td style="padding:6px; border:1px solid #334155;">Click row(s)</td>
</tr>
<tr>
  <td style="padding:6px; border:1px solid #334155;">Review Status</td>
  <td style="padding:6px; border:1px solid #334155;">Check pass/fail or in-progress indicators</td>
  <td style="padding:6px; border:1px solid #334155;">View status icons</td>
</tr>
<tr>
  <td style="padding:6px; border:1px solid #334155;">Regenerate Report</td>
  <td style="padding:6px; border:1px solid #334155;">Export latest or prior test execution reports</td>
  <td style="padding:6px; border:1px solid #334155;">Click Regenerate button</td>
</tr>
<tr>
  <td style="padding:6px; border:1px solid #334155;">Use Reports</td>
  <td style="padding:6px; border:1px solid #334155;">Download and share Excel files</td>
  <td style="padding:6px; border:1px solid #334155;">Save to local storage</td>
</tr>
</table>

"""
}

       
}

