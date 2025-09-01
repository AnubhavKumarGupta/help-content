# help_content/testcase_help.py

def get_testcase_content():
    """Test case related help content - focused only on test case operations"""
    return {

# --------------------------------   Create Test Cases      ---------------------

"Create Test Case": {
    "title": "Create Test Case",
    "description": """
<b>Create Test Case – Help Guide</b><br>

This feature allows you to configure, map, and prepare <b>data validation scenarios</b> (test cases) comparing source and target tables/columns across your connected databases.<br>
Follow the steps below to ensure correct, repeatable, and robust test cases.<br><br>

<b>Step 1: Test Case Setup</b><br>
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
</table><br>

<b>Step 2: Target Table Selection and Mapping</b><br>
<table style="width:100%; border-collapse: collapse; margin-bottom: 14px; border:1px solid #334155;">
<tr style="background:#1e293b; color:#38bdf8; text-align:left;">
<th style="padding:8px; border:1px solid #334155;">Action</th>
<th style="padding:8px; border:1px solid #334155;">Details</th>
</tr>
<tr><td style="padding:6px; border:1px solid #334155;">Select Target Connection</td><td style="padding:6px; border:1px solid #334155;">Pick the target DB connection from dropdown.</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Fetch Target Tables</td><td style="padding:6px; border:1px solid #334155;">Click <b>Fetch Target Table</b> to view available tables.</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Map Tables</td><td style="padding:6px; border:1px solid #334155;">Auto-mapping suggested; if not, drag & drop manually.<br>Mapped tables appear under <b>Mapped Tables</b>.</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Unmap Function</td><td style="padding:6px; border:1px solid #334155;">Click <b>Unmap</b> to remove mapping.<br>Click <b>Next</b> for column mapping.</td></tr>
</table><br>

<b>Step 3: Column Mapping and Filtering</b><br>
<table style="width:100%; border-collapse: collapse; margin-bottom: 14px; border:1px solid #334155;">
<tr style="background:#1e293b; color:#38bdf8; text-align:left;">
<th style="padding:8px; border:1px solid #334155;">Action</th>
<th style="padding:8px; border:1px solid #334155;">Details</th>
</tr>
<tr><td style="padding:6px; border:1px solid #334155;">Review Columns</td><td style="padding:6px; border:1px solid #334155;">Source & Target columns shown side-by-side.<br>Auto-mapped if names match.</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Set Primary Key</td><td style="padding:6px; border:1px solid #334155;">Required for Column Data Validation.<br>Auto-selected if present; else select manually.</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Apply Filters</td><td style="padding:6px; border:1px solid #334155;">Add filter conditions (column, operator, value).<br>Supports multiple filters.</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Save Mapping</td><td style="padding:6px; border:1px solid #334155;">Click <b>Save</b> to save mappings.</td></tr>
<tr><td style="padding:6px; border:1px solid #334155;">Execute</td><td style="padding:6px; border:1px solid #334155;">Click <b>Execute</b> to run test case.<br>Choose location to save Excel result file.</td></tr>
</table><br>

<b>Tips & Notes:</b><br>
• Use underscores in test case names.<br>
• Primary Key is mandatory for Column Data Validation.<br>
• Drag & drop for manual mappings.<br>
• Filters support flexible conditions.<br>
• Results exported as Excel.<br>
• Use <b>Previous</b> to revise selections.<br><br>

<b>Typical Workflow Diagram:</b><br>
<pre>
[Create Test Case]
   |
   v
[Enter Name] --> [Select Source Connection] --> [Fetch Source Table]
      |                  |
      v                  v
[Select Validation Type] [Select Source Table(s)]
   |
   v
[Next → Target Selection]
   |
   v
[Select Target Connection] --> [Fetch Target Table]
   |
   v
[Auto/Manual Table Mapping]
   |
   v
[Next → Column Mapping]
   |
   v
[Auto/Manual Column Map] — [Primary Key] — [Set Filters]
   |
   v
[Save Mapping]
   |
   v
[Execute] --> [Choose Excel Save Path]
</pre><br>

<i>Following this guide ensures your test cases are created accurately, mapped correctly, and ready for automated/manual execution in InfoFiscus Data Validation Tool.</i>
"""
}


# "Create Test Case": {
#     "title": "Create Test Case",
#     "description": """
# <b>Create Test Case – Help Guide</b><br><br>

# <b>Overview:</b><br>
# The Create Test Case feature allows you to configure, map, and prepare data validation scenarios (test cases) comparing source and target tables/columns across your connected databases. Follow the steps below to ensure correct, repeatable, and robust test cases for scheduled validation.<br><br>

# <b>Step 1: Test Case Setup</b><br>
# 1. <b>Access the Create Test Case Panel:</b> From the left menu, click <b>Create Test Case</b>.<br>
# 2. <b>Enter a Test Case Name:</b> Input a unique name for the test case.<br>
# <b>Best Practice:</b> Do not use spaces – use underscores instead (e.g., Customer_Validation_2025). Test cases with spaces in the name may fail during scheduling/execution.<br><br>

# 3. <b>Select Source Connection:</b> Click the Select Connection dropdown. Choose the source database connection (e.g., Databricks, Snowflake, etc.).<br>
# 4. <b>Fetch Source Tables:</b> Click <b>Fetch Source Table</b>. All tables available in your selected source connection will appear. Select the table(s) you want to use as the data source.<br>
# 5. <b>Choose Validation Type:</b> From the validation type dropdown, choose the kind of comparison or data check you want to perform (e.g., row count, column data, etc.). Select relevant tables for validation.<br>
# 6. <b>Proceed to the Next Step:</b> Click <b>Next</b> to move to table mapping.<br><br>

# <b>Step 2: Target Table Selection and Mapping</b><br>
# 7. <b>Select Target Connection:</b> Use the Target Connection dropdown to pick the database where your target tables are located.<br>
# 8. <b>Fetch Target Tables:</b> Click <b>Fetch Target Table</b>. Target tables will be displayed in a list.<br>
# 9. <b>Map Tables:</b> The system will attempt to automatically map source tables to matching target tables. If not automatically mapped, drag and drop tables from the left (source) to the right (target) to define the mapping. Mapped tables will be displayed in the "Mapped Tables" column.<br>
# 10. <b>Unmap Functionality:</b> You can "unmap" any table if you wish to remove a pairing. Click <b>Next</b> to move to column mapping.<br><br>

# <b>Step 3: Column Mapping and Filtering</b><br>
# 11. <b>Review Source and Target Columns:</b> You’ll see columns from the source and target tables shown side-by-side. The system auto-maps columns with matching names (case-insensitive). Manual mapping can be done by dragging and dropping if necessary.<br>
# 12. <b>Set Primary Key (Column Data Validation only):</b> For column data validation scenarios, primary keys must be set before mapping can be saved. If the primary key is defined in the table it will be auto-selected; if not, manually select the primary key column(s) by checking the corresponding boxes.<br>
# 13. <b>Apply Filters (Optional):</b> Click the Filter button to add filtering conditions. In the popup, choose the column, operator (e.g., >, <, =, !=, LIKE), and value. Click Add to add more filter conditions, then Save.<br>
# 14. <b>Save Mapping:</b> Once satisfied with table and column mappings (and filters), click <b>Save</b>. The mapping configuration saves your test case logic.<br>
# 15. <b>Execute Test Case:</b> Click <b>Execute</b> to run the test validation immediately. The system will prompt you to select a path to save the executed Excel result file.<br><br>

# <b>Tips & Important Notes:</b><br>
# • Unique Test Case Names: Use only underscores, avoid spaces for compatibility with scheduling/execution.<br>
# • Primary Key Required: For column data validation, primary keys must always be set (auto or manual).<br>
# • Drag-and-Drop: Use for manual mapping where auto-matching fails or for custom mapping scenarios.<br>
# • Filter Logic: Supports multi-condition, flexible filtering for focused test scenarios.<br>
# • Excel Export: After execution, results are exported as Excel files for reporting/audit.<br>
# • Navigation: Use the Previous button to step back and revise source/target selections if needed.<br><br>

# <b>Typical Workflow Diagram:</b><br>
# <pre>
# [Create Test Case]
# |
# v
# [Enter Name] --> [Select Source Connection] --> [Fetch Source Table]
# |                               |
# v                               v
# [Select Validation Type]         [Select Source Table(s)]==|
# |
# v
# [Next → Target Selection]
# |
# v
# [Select Target Connection] --> [Fetch Target Table]
# |
# v
# [Auto/Manual Table Mapping]
# |
# v
# [Next → Column Mapping]
# |
# v
# [Auto/Manual Column Map] — [Primary Key] — [Set Filters]
# |
# v
# [Save Mapping]
# |
# v
# [Execute] --> [Choose Excel Save Path]
# </pre><br>

# <i>Following this step-by-step guide ensures your test cases are created accurately, mapped correctly, and ready for robust automated or manual execution within InfoFiscus Data Validation Tool.</i>
# """
# }

,

# ----------------------------------   Show test cases      -------------------------

"Show Test Case": {
    "title": "Show Test Case",
    "description": """
<b>Show Test Case – Help Guide</b><br><br>

<b>Overview</b><br>
The Show Test Case feature is your command center for test case lifecycle management. Here you can review, update (Edit), or remove (Delete) existing test cases, ensuring your validation suite stays organized, accurate, and agile as your data and business rules evolve.<br><br>

<b>Main Functionalities</b><br>

1. <b>Edit Test Case</b><br>
<b>Purpose:</b> Modify any previously created test case to adapt to changing requirements, data sources, or validation logic without starting from scratch.<br>
<b>When to Use:</b><br>
• Business requirements change<br>
• New columns/tables need validation<br>
• Validation type needs to be updated<br>
• Table or column mappings need adjustment<br>
• To add/remove filters, or reset the primary key for column validation<br><br>

2. <b>Delete Test Case</b><br>
<b>Purpose:</b> Permanently remove obsolete, irrelevant, or duplicate test cases to keep your UI clean and ensure only relevant jobs are retained.<br><br>

<b>How to Use – Step-by-Step Workflow</b><br>

A. <u>Finding and Selecting a Test Case</u><br>
• <b>Search:</b> Use the search bar to find test cases by name, connection, or partial keyword. This is especially helpful in large environments.<br>
• <b>Select:</b> Choose the desired test case by clicking the corresponding row/radio button in the list.<br><br>

B. <u>Edit Workflow</u><br>
• <b>Click Edit:</b> After selecting a test case, click the Edit button.<br>
• This opens the editing interface (similar to <b>Create Test Case</b> wizard).<br>
• <b>Adjust Configuration:</b><br>
  – Change validation type (Schema, Row Count, Column Data, or combinations).<br>
  – Select/deselect tables as required.<br>
• <b>Table Mapping:</b> Click <b>Table Mapping</b> to map or unmap source/target tables (drag-and-drop or auto-mapping).<br>
• <b>Column Mapping:</b> Click <b>Column Mapping</b> to pair columns, update primary keys (mandatory for column data validation), and define filters.<br>
• <b>Save & Execute:</b> Save to update the case. Optionally, execute immediately to validate with new settings and download results.<br>
<i>Note:</i> Only validation, logic, and mappings can be edited—test case name and source connection usually stay fixed.<br><br>

C. <u>Delete Workflow</u><br>
• <b>Select & Delete:</b> Choose an unwanted case and click Delete.<br>
• <b>Confirm:</b> Approve the prompt to remove it permanently.<br>
• The case is removed from the list, keeping your UI clean.<br><br>

<b>Visual Workflow Diagram</b><br>
<pre>
[Show Test Case Page]
|
+---------------------+
|        |            |
[Edit]  [Delete]
|        |
[Load Editable   [Confirm deletion]
Test Case UI]     |
|                 [Case removed]
|
[Adjust settings, mappings]
|
[Table Mapping] → [Column Mapping]
|
[Save]/[Execute]
</pre><br>

<b>Feature Comparison Table</b><br>
<table border="1" cellpadding="5" cellspacing="0">
<tr><th>Function</th><th>Purpose</th><th>Main Actions</th><th>When to Use</th></tr>
<tr><td><b>Edit</b></td><td>Update an existing test case</td><td>Modify validation, mapping, logic</td><td>When requirements/data change or optimization is needed</td></tr>
<tr><td><b>Delete</b></td><td>Remove test case</td><td>Select & confirm deletion</td><td>When case is obsolete, duplicated, or no longer needed</td></tr>
</table><br><br>

<b>Best Practices & Tips</b><br>
• Edit instead of recreate when possible—this preserves links, history, and supporting data.<br>
• Always review mappings and primary key selections after schema or column changes.<br>
• Use search to quickly locate and act on test cases.<br>
• Delete test cases regularly to avoid clutter.<br>
• After deleting, check for downstream dependencies that may rely on the removed test case.<br>
• All validations, mapping requirements, and filter logic from <b>Create Test Case</b> guidance still apply.<br><br>

<b>Summary</b><br>
Show Test Case puts lifecycle management at your fingertips:<br>
• Adapt tests as your data grows<br>
• Remove anything redundant<br>
• Update instantly while keeping auditability and quality intact<br><br>

<i>For detailed help on column mapping, validation requirements, and filters, see the “Create Test Case – Help Guide”.</i>
"""
},


# -------------------------------      Show Test Result  ---------------------------

"Show Test Results": {
    "title": "Show Test Results",
    "description": """
<b>Show Test Results – Help Guide</b><br><br>

<b>Overview</b><br>
The Show Test Results section is your dashboard for reviewing all completed test case executions. It provides detailed insights into tests that succeeded or failed, enabling you to understand the health of your data pipelines and validation efforts.<br><br>

<b>Key Features and Usage</b><br>
• <b>View All Results:</b> Lists all test runs created by the current user, showing status (pass/fail), execution time, associated test case, and summary info.<br>
• <b>Status Indicators:</b> Quickly identify failures or successes to prioritize troubleshooting.<br>
• <b>Regenerate Reports:</b> Select prior test executions and regenerate Excel reports without re-running tests—useful for sharing or archiving.<br>
• <b>Search and Filter:</b> Use the search bar and filters to find specific executions by name, date, or status.<br><br>

<b>Typical Workflow</b><br>
1. Navigate to <b>Show Test Results</b> from the main menu.<br>
2. Browse or search for the relevant test executions.<br>
3. Review status and execution metadata.<br>
4. Select one or more results to regenerate reports.<br>
5. Click <b>Regenerate</b> to export Excel files for auditing or sharing.<br><br>

<b>Benefits</b><br>
• Centralized access to all validation results.<br>
• Simplifies compliance with easy report re-generation.<br>
• Saves time by avoiding re-execution for report generation.<br>
• Focuses attention on failing tests for faster resolution.<br><br>

<b>Best Practices</b><br>
• Regularly review results post-execution to catch issues early.<br>
• Use search and filters to efficiently manage large volumes.<br>
• Maintain consistent, descriptive test case naming for ease of use.<br>
• Regenerate reports as needed for stakeholders or compliance.<br><br>

<b>Diagram: Flowchart of User Actions</b><br>
<pre>
[Show Test Results Screen]
|
+-----+--------+-----------+
|     |        |           |
[Search] [Select Test] [View List]
  |         |         |
  |     +---+----+    |
  |     |        |    |
[Filter] [View Details] [Status (Pass/Fail)]
|
+-----+-----+
|           |
[Regenerate] [Close]
|
[Export Excel Report]
</pre><br>

<b>Task Summary Table</b><br>
<table border="1" cellpadding="5" cellspacing="0">
<tr><th>Step</th><th>Description</th><th>User Action</th></tr>
<tr><td><b>Open Results</b></td><td>Access Show Test Results page</td><td>Navigate via main menu</td></tr>
<tr><td><b>Search / Filter</b></td><td>Narrow down results by criteria</td><td>Use search bar and filters</td></tr>
<tr><td><b>Select Test Run</b></td><td>Highlight one or multiple test executions</td><td>Click row(s)</td></tr>
<tr><td><b>Review Status</b></td><td>Check pass/fail or in-progress indicators</td><td>View status icons</td></tr>
<tr><td><b>Regenerate Report</b></td><td>Export latest or prior test execution reports</td><td>Click Regenerate button</td></tr>
<tr><td><b>Use Reports</b></td><td>Download and share Excel files</td><td>Save to local storage</td></tr>
</table><br><br>

<b>Summary</b><br>
The Show Test Results page provides an essential interface for monitoring and leveraging your data validation outcomes. Through seamless search, detailed status views, and easy report regeneration, it supports ongoing data quality assurance and regulatory compliance in your organization.
"""
}
    }