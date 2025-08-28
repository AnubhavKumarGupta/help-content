# help_content/testcase_help.py

def get_testcase_content():
    """Test case related help content - focused only on test case operations"""
    return {
        "Create Test Case": {
            "title": "📝 Create Test Case – Help Guide",
            "description": """
<b>Create Test Case - Help Guide</b><br><br>

This section guides you through creating a new test case with the following fields:<br><br>

<b>Form Fields:</b><br>
• <b>Test Case Name:</b> Enter a descriptive name for the test case.<br>
• <b>Source Connection:</b> Select the source database connection from the dropdown.<br>
• <b>Fetch Source Table:</b> Click this button to fetch available tables from the selected connection.<br>
• <b>Validation Types:</b> Choose one of the following options based on what you want to validate:<br>
&nbsp;&nbsp;&nbsp;&nbsp; • Schema Validation<br>
&nbsp;&nbsp;&nbsp;&nbsp; • Row Count Validation<br>
&nbsp;&nbsp;&nbsp;&nbsp; • Schema Validation + Row Count Validation<br>
&nbsp;&nbsp;&nbsp;&nbsp; • Column Data Validation<br><br>

<b>Table Mapping:</b><br>
This screen lets you map your source tables to target tables in the selected connection. 
Mappings enable data synchronization and integration between systems.<br><br>

<b>How to Use Table Mapping:</b><br>
• Choose a <b>Target Connection</b> from the top dropdown to select where data will be mapped.<br>
• Click <b>Fetch Target Table</b> to load the available tables from the selected connection.<br>
• The <b>Source Table Name</b> panel (left) lists your source tables.<br>
• The <b>Target Tables</b> panel (right) shows the tables available in your target connection and their current mappings (see "Mapped Tables").<br>
• Mapped pairs appear in the <b>Mapped Tables</b> column. You can only map each target table to one source table.<br>
• To remove an existing mapping, click the <b>Unmap</b> button in the Action column.<br>
• Use <b>Previous</b> to go back, or <b>Next</b> to continue to the next step when all desired mappings are done.<br><br>

<b>Next Steps:</b><br>
After filling all required details and selecting the appropriate validation type, 
click <b>Save</b> to create and store the test case.<br><br>

<i>Tip: Use clear and descriptive names for your test cases to make them easier to identify later. Review mappings carefully to avoid misalignment between source and target tables.</i>
            """
        }
,

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