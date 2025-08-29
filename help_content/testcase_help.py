# help_content/testcase_help.py

def get_testcase_content():
    """Test case related help content - focused only on test case operations"""
    return {

# ---------------------------   Create Test Cases   ---------------------

"Create Test Case": {
    "title": "📝 Create Test Case",
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
#     "title": "📝 Create Test Case",
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

# -----------------------------------   Show test cases   -------------------------

"Show Test Case": {
    "title": "📋 Show Test Case",
    "description": """
<b>Show Test Case - Help Guide</b><br><br>

This page displays a list of all <b>test cases created by the user</b>. 
From here, you can search, review, edit, or delete existing test cases.<br><br>

<b>Search & Filter:</b><br>
• <b>Search Box:</b> Quickly filter test cases by name or keyword.<br><br>

<b>Columns Displayed:</b><br>
• <b>Name:</b> The test case name.<br>
• <b>Source / Target:</b> Systems involved in validation.<br>
• <b>Validation Type:</b> Type of check (Schema or Column Data).<br>
• <b>User ID:</b> Creator of the test case.<br>
• <b>Created Date:</b> When the test case was added.<br><br>

<b>Actions:</b><br>
• <b>Edit:</b> Select a test case and click Edit to update its details.<br>
• <b>Delete:</b> Select a test case and click Delete to remove it permanently.<br><br>

<b>User-Specific View:</b><br>
• Only test cases created by you will be displayed here.<br><br>

<b>Tips:</b><br>
• Use search and filters for quick access.<br>
• Keep test cases updated to ensure accurate validation.<br>
• Review execution status regularly to track test health.<br><br>

<i>Managing test cases effectively ensures accurate and reliable validations.</i>
    """
},

"Show Test Results": {
    "title": "📊 Show Test Results",
    "description": """
<b>Show Test Results - Help Guide</b><br><br>

This table displays all executed test cases and their results. 
It provides details about the test configuration, validation type, execution status, and performance metrics.<br><br>

<b>Table Columns:</b><br>
• <b>S. No.:</b> Sequential number of each test case in the list.<br>
• <b>Select:</b> Radio button to choose a test case for generating a report.<br>
• <b>Client ID:</b> Identifier of the client for which the test case was executed.<br>
• <b>User ID:</b> Identifier of the user who initiated or owns the test case.<br>
• <b>Test Case Name:</b> The descriptive name of the test case.<br>
• <b>Source DB:</b> The source database against which the test case was executed.<br>
• <b>Target DB:</b> The target database for comparison or validation.<br>
• <b>Validation Type:</b> Specifies the type of validation performed:<br>
&nbsp;&nbsp;&nbsp;&nbsp; • Row Count Validation<br>
&nbsp;&nbsp;&nbsp;&nbsp; • Schema Validation<br>
&nbsp;&nbsp;&nbsp;&nbsp; • Column Data Validation<br>
• <b>Status:</b> Current state of execution (Passed, Failed, In Progress).<br>
• <b>Execution Time:</b> Duration taken for the test case execution.<br>
• <b>Source Name:</b> The specific source system or connection name used.<br>
• <b>Target Name:</b> The specific target system or connection name used.<br><br>

<b>User Actions:</b><br>
• Review results and analyze failures.<br>
• Monitor performance metrics of each execution.<br>
• Select a test case to inspect in detail or generate reports.<br><br>

<b>Tips:</b><br>
• Use filters and sorting to quickly locate specific test results.<br>
• Execution details provide insights into data consistency and validation coverage.<br>
• Regular review ensures data accuracy, system reliability, and compliance with standards.<br><br>

<i>Analyzing test results regularly helps maintain high-quality validation and system trustworthiness.</i>
    """
}
    }